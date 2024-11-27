import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import threading
import struct
import webbrowser

class PhonemeDataCopier:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("WAV Phoneme Data Copier")
        self.window.geometry("800x650")
        
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        watermark_frame = ttk.Frame(main_frame)
        watermark_frame.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        
        url_label = ttk.Label(
            watermark_frame,
            text="https://onge.org/",
            foreground="blue",
            cursor="hand2",
            font=("Arial", 10, "underline")
        )
        url_label.grid(row=0, column=1, padx=5)
        url_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://onge.org/"))
        
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5
        )

        ttk.Label(main_frame, text="Original WAV Files Root Folder:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.original_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.original_path, width=70).grid(row=3, column=0, padx=5)
        ttk.Button(main_frame, text="Browse...", command=self.browse_original).grid(row=3, column=1)
        
        ttk.Label(main_frame, text="Modded WAV Files Root Folder:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.modded_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.modded_path, width=70).grid(row=5, column=0, padx=5)
        ttk.Button(main_frame, text="Browse...", command=self.browse_modded).grid(row=5, column=1)
        
        ttk.Button(main_frame, text="Process Files", command=self.start_processing).grid(row=6, column=0, columnspan=2, pady=20)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.log_text = tk.Text(main_frame, height=20, width=80)
        self.log_text.grid(row=8, column=0, columnspan=2, pady=10)
        
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar.grid(row=8, column=2, sticky=(tk.N, tk.S))
        self.log_text['yscrollcommand'] = scrollbar.set
        
        try:
            if hasattr(sys, '_MEIPASS'):
                icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
            else:
                icon_path = 'icon.ico'
            
            if os.path.exists(icon_path):
                self.window.iconbitmap(icon_path)
        except Exception:
            pass


    def browse_original(self):
        folder = filedialog.askdirectory()
        if folder:
            self.original_path.set(folder)
            
    def browse_modded(self):
        folder = filedialog.askdirectory()
        if folder:
            self.modded_path.set(folder)
            
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def find_chunk(self, data, chunk_id):
        pos = 0
        size = len(data)
        
        while pos < size:
            if data[pos:pos + 4] == chunk_id:
                chunk_size = struct.unpack('<I', data[pos + 4:pos + 8])[0]
                return pos, chunk_size
            pos += 1
        return -1, 0

    def extract_vdat_chunk(self, data):
        vdat_pos, vdat_size = self.find_chunk(data, b'VDAT')
        
        if vdat_pos == -1:
            version_marker = b'VERSION 1.0'
            version_pos = data.find(version_marker)
            if version_pos == -1:
                return None, None
            
            return None, data[version_pos:]
            
        vdat_chunk = data[vdat_pos:vdat_pos + vdat_size + 8]
        vdat_data = data[vdat_pos + 8:vdat_pos + vdat_size + 8]
        
        return vdat_chunk, vdat_data

    def create_vdat_chunk(self, phoneme_data):
        if not phoneme_data.startswith(b'VERSION 1.0'):
            phoneme_data = b'VERSION 1.0\r\n' + phoneme_data

        chunk_id = b'VDAT'
        chunk_size = len(phoneme_data)
        chunk_size_bytes = struct.pack('<I', chunk_size)
        
        return chunk_id + chunk_size_bytes + phoneme_data

    def copy_phoneme_data(self, original_wav_path, modded_wav_path):
        try:
            with open(original_wav_path, 'rb') as f:
                original_data = f.read()
                
            vdat_chunk, phoneme_data = self.extract_vdat_chunk(original_data)
            
            if phoneme_data is None:
                self.log(f"WARNING: No phoneme data found in {os.path.basename(original_wav_path)}")
                return False

            with open(modded_wav_path, 'rb') as f:
                modded_data = f.read()
            
            vdat_pos, _ = self.find_chunk(modded_data, b'VDAT')
            if vdat_pos != -1:
                modded_data = modded_data[:vdat_pos]
            
            riff_size_pos = 4
            riff_size = struct.unpack('<I', modded_data[riff_size_pos:riff_size_pos + 4])[0]
            
            if vdat_chunk is None:
                vdat_chunk = self.create_vdat_chunk(phoneme_data)
            
            new_riff_size = riff_size + len(vdat_chunk)
            new_riff_size_bytes = struct.pack('<I', new_riff_size)
            
            with open(modded_wav_path, 'wb') as f:
                f.write(modded_data[:riff_size_pos])
                f.write(new_riff_size_bytes)
                f.write(modded_data[riff_size_pos + 4:])
                f.write(vdat_chunk)
            
            with open(modded_wav_path, 'rb') as f:
                final_data = f.read()
                if b'VERSION 1.0' in final_data and b'PLAINTEXT' in final_data:
                    self.log(f"Success! Added phoneme data to {os.path.basename(modded_wav_path)}")
                    return True
                else:
                    self.log(f"ERROR: Failed to verify phoneme data in {os.path.basename(modded_wav_path)}")
                    return False
                    
        except Exception as e:
            self.log(f"Error processing {os.path.basename(modded_wav_path)}: {str(e)}")
            return False

    def get_all_wav_files(self, root_dir):
        wav_files = {}
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.lower().endswith('.wav'):
                    rel_path = os.path.relpath(dirpath, root_dir)
                    if rel_path == '.':
                        rel_path = ''
                    wav_files[os.path.join(rel_path, filename).lower()] = {
                        'full_path': os.path.join(dirpath, filename),
                        'rel_path': rel_path
                    }
        return wav_files

    def process_files(self):
        try:
            original_root = self.original_path.get()
            modded_root = self.modded_path.get()
            
            if not original_root or not modded_root:
                messagebox.showerror("Error", "Please select both root folders")
                return
                
            self.log("Scanning directories...")
            original_files = self.get_all_wav_files(original_root)
            modded_files = self.get_all_wav_files(modded_root)
            
            matching_files = set(original_files.keys()) & set(modded_files.keys())
            total_files = len(matching_files)
            
            if total_files == 0:
                self.log("No matching WAV files found in directory structure")
                return
                
            self.log(f"Found {total_files} matching WAV files")
            self.log("Starting processing...")
            
            processed = 0
            successful = 0
            
            for rel_path in matching_files:
                original_info = original_files[rel_path]
                modded_info = modded_files[rel_path]
                
                modded_dir = os.path.dirname(modded_info['full_path'])
                os.makedirs(modded_dir, exist_ok=True)
                
                self.log(f"\nProcessing {rel_path}...")
                
                if self.copy_phoneme_data(original_info['full_path'], modded_info['full_path']):
                    successful += 1
                
                processed += 1
                self.progress_var.set((processed / total_files) * 100)
                self.window.update_idletasks()
                
            self.log(f"\nProcessing complete!\nSuccessfully processed {successful} out of {total_files} files")
            messagebox.showinfo("Complete", f"Processing complete!\nSuccessfully processed {successful} out of {total_files} files")
            self.progress_var.set(0)
            
        except Exception as e:
            self.log(f"Critical error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def start_processing(self):
        self.log_text.delete(1.0, tk.END)
        thread = threading.Thread(target=self.process_files)
        thread.daemon = True
        thread.start()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PhonemeDataCopier()
    app.run()