# FolderReplicator

Python script for synchronizing two folders! This tool can be used to create a backup (replica) of a source folder, which will automatically stay in sync as files are added, removed, or modified.

![image](https://github.com/user-attachments/assets/4efdd8b4-20fb-4d25-89a9-6aec4d61d681)

## Features:
- Automatically synchronize folders at the specified interval.
- Is able to detect and update new, modified, or deleted files.
- Provides logging of the synchronization tasks.

## Requirements:
- Python 3.x

## Installation:
- Clone this repository or download the Python script.

## How To Run:

You can run the program by using the command line with the following syntax: 

```bash
python program.py [path to source folder] [path to replica folder] [interval time (in seconds)] [path to logfile]
```
(You can use relative paths or absolute paths, both will work).



### Example for Quick Testing: 
Tip: You can copy-paste this directly into your command line and try out the script. For this example, make sure you navigate to the directory where the script is saved using your command line (e.g., with the cd command)

```bash
python program.py source replica 3 logfile.txt
```

### Step 1:
Open the command line, make sure the directory is where the script is saved. You can use the cd command, or right click and choose "Open In Terminal" like shown below.

![image](https://github.com/user-attachments/assets/dda9f6b1-fce5-4053-9dbc-f7a7115224d9)

### Step 2:
Paste the command and have fun!

![image](https://github.com/user-attachments/assets/6fd307c2-099f-42f7-8d25-fb69953aaa91)





