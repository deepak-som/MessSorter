#you better be lazy it makes you smart.

import os
from pathlib import Path
from tkinter import filedialog
from tkinter import *


DIRECTORIES = {"HTML":[".html5", ".html" , ".htm", ".xhtml"],
"IMAGES": [".jpeg",".jpg",".tiff",".gif",".bmp",".png",".bpg",".svg",".heif",".psd","jfif"],
"VIDEOS": [".avi",".flv",".wmv",".mov",".mp4",".webm",".vob",".mng",".qt",".mpg",".mpeg",".3gp",".mkv"],
"DOUCMUENTS": [".oxps" , ".epub", ".pages", ".docx",".doc",".fpf",".ods",".odt",".pwi",".xsn",".xps",".dotx",".docm",".dox",".rvg",".rtf",".rtfd",".wpd",".xls",".xlsx",".ppt",".pptx"],
"ARCHIVES": [".a",".ar",".cpio",".iso",".tar",".gz",".rz",".7z",".dmg",".rar",".xar",".zip"],
"AUDIO": [".aac", ".aa", ".dvf",".m4a",".mp4b",".mp4p",".mp3",".msv",".ogg",".oga",".raw",".vox",".wav",".wma"],
"APK": [".apk"],
"TORRENTS":[".torrent"],
"PLAINTEXT": [".txt",".in", ".out"],
"PDF": [".pdf"],
"PYTHON": [".py"],
"XML": [".xml"],
"EXE": [".exe"],
"SHELL": [".sh"],
"ARDUINO_FILES":[".ino"],
"PROTEUS_FILES":[".pdsclip", ".pdspnl", ".pdsprj"],
"EAGLE_FILES":[".brd", ".cam", ".dbl", ".dru", ",epf", ".sch", ".scr",".ulp"]

}


FILE_FORMATS = {file_format: directory
    for directory , file_formats in DIRECTORIES.items()
        for file_format in file_formats

}


def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format =file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])

            directory_path.mkdir(exist_ok = True)

        file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
                os.rmdir(dir)

            except:
                pass


try:
    root = Tk()
    target = filedialog.askdirectory()
    #print(target)
    #cwd = os.getcwd()
    #print(cwd)
    os.chdir(target)
    print("we just sorted the following folder -->", end = " ")
    print(os.getcwd())
    organize_junk()


except:
    print("Something is wrong either with path or with os let us know")
    print("we are really sorry task is not done")








#if __name__ == "__main__":
# organize_
# junk()
#print(DIRECTORIES.items())


#add missing file_types in DIRECTORIES, if there! is any, my appologies for that.                                                                           
                                                                                 #dee!(1101 1110 1110!)
