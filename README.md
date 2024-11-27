# WAV-Phoneme-Data-Copier
A tool to copy lip sync [Phoneme] data from HL2 audio files to mods in bulk

Follow me on the Steam Workshop
https://steamcommunity.com/id/Ongezell/myworkshopfiles/

While developing the Miku voice mod, I encountered a roadblock. there was no good way to bulk copy lip sync data from Half-Life 2 audio files to mod files. To solve this, I created a software that can do just that.

https://steamcommunity.com/sharedfiles/filedetails/?id=3371696083

[h2]Features[/h2]
[list]
[*]Copy phoneme/lip sync data from original HL2 files to your mod files
[*]Process entire directory structures at once (including subdirectories)
[*]Match files based on relative paths and names
[*]Preserve the original VDAT chunk format used by Source engine
[/list]

[h2]Usage Example[/h2]
Original files: hl2/sound/vo/
Modified files: mod/sound/vo/

[olist]
[*]Download and run the program
[*]Select your source folder (HL2 or original game files)
[*]Select your destination folder (your mod's files)
[*]Click "Process Files" and wait for completion
[/olist]
[previewimg=38620824;sizeFull,floatLeft;Untitled.png][/previewimg]


[b]Important:[/b] Both directories must maintain the same structure, and files must have matching names.

[h2]Download[/h2]
[url=https://onge.org/software/WAV_Phoneme_Data_Copier.zip]Download WAV Phoneme Data Copier[/url]


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
