# WAV-Phoneme-Data-Copier
A tool to copy lip sync [Phoneme] data from HL2 audio files to mods in bulk
# Miku Voice Mod Development Tools

Follow me on the [Steam Workshop](https://steamcommunity.com/id/Ongezell/myworkshopfiles/)

While developing the Miku voice mod, I encountered a roadblock: there was no good way to bulk copy lip sync data from Half-Life 2 audio files to mod files. To solve this, I created software that can do just that.

[Check it out on Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3371696083)

---

## Features

- Copy phoneme/lip sync data from original Half-Life 2 files to your mod files
- Process entire directory structures at once (including subdirectories)
- Match files based on relative paths and names
- Preserve the original VDAT chunk format used by the Source engine

---

## Usage Example

Original files: `hl2/sound/vo/`  
Modified files: `mod/sound/vo/`

1. Download and run the program.
2. Select your source folder (HL2 or original game files).
3. Select your destination folder (your mod's files).
4. Click **"Process Files"** and wait for completion.

![Preview](https://steamuserimages-a.akamaihd.net/ugc/38620824/Untitled.png)

**Important:**  
Both directories must maintain the same structure, and files must have matching names.

---

## Download

[Download WAV Phoneme Data Copier](https://onge.org/software/WAV_Phoneme_Data_Copier.zip)

---

## Tips

- Always back up your files before processing.
- Ensure your mod follows the same folder structure as the original game.
- The program only processes `.wav` files.
- Files must have identical names to be matched.

---

## Credits

- **Me** - [http://onge.org](https://onge.org)  
- **Valve Software [Source SDK 2013]** - [https://github.com/ValveSoftware/source-sdk-2013](https://github.com/ValveSoftware/source-sdk-2013)  
- **Bing** for the cover

[h2]Tips[/h2]
[list]
[*]Always backup your files before processing
[*]Make sure your mod follows the same folder structure as the original game
[*]The program will only process .wav files
[*]Files must have identical names to be matched
[/list]


[h2]Credits[/h2]
Me- [url=https://onge.org]http://onge.org[/url]
Valve Software [Source SDK 2013] - [url=https://github.com/ValveSoftware/source-sdk-2013]https://github.com/ValveSoftware/source-sdk-2013[/url]
Bing for the cover
