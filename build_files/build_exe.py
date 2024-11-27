import PyInstaller.__main__
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'phoneme_copier.py', 
    '--onefile',         
    '--windowed', 
    '--name=WAV_Phoneme_Data_Copier',
    '--icon=icon.ico',   
    '--add-data=icon.ico;.', 
    '--noconsole',
    '--version-file=version.txt',
    '--clean',
])