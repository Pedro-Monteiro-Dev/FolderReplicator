# FolderReplicator

Python script for synchronizing two folders! This tool can be used to create a backup (replica) of a source folder, which will automatically stay in sync as files are added, removed, or modified.

![image](https://github.com/user-attachments/assets/4efdd8b4-20fb-4d25-89a9-6aec4d61d681)

## Features:
- Automatically synchronize folders at the specified interval.
- Is able to detect and update new, modified, or deleted files.
- Provides logging of the synchronization tasks.

## Installation:
- Clone this repository or download the Python script.

### How To Run:

You can run the program by using the command line with the following syntax: 

```bash
python program.py [path to source] [path to replica] [interval time (in seconds)] [path to logfile]
```
(You can use relative paths or absolute paths, both will work).

Example: 

```bash
python program.py source replica 3 logfile.txt
```


![image](https://github.com/user-attachments/assets/6fd307c2-099f-42f7-8d25-fb69953aaa91)





