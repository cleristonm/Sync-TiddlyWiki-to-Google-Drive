#!/usr/bin/env python3

# Directory where your original file is stored
# Put the / at the end
tw_dir = 'PATH_OF_YOUR_TIDDLY_WIKI_FILE/'

# Name of your TiddlyWiki file
tw_file = 'NAME_OF_YOUR_TIDDLY_WIKI_FILE'

# Name of your rclone remote 
rclone_remote_name = 'REMOTE_CONFIGURED_ON_RCLONE'

# Name of your remote folder where your
# TiddlyWiki is stored
# Put the / at the end
gdrive_tw_folder = '/GOOGLE_DRIVE_FOLDER/'

temp_dir = "/tmp/"

import os
import subprocess

def save_remotely():
    os.system("rclone copy "+tw_dir+tw_file+" "+rclone_remote_name+":"+gdrive_tw_folder)
    print("TiddlyWiki saved remotely")

def save_localy():
    os.system("rclone copy "+rclone_remote_name+":"+gdrive_tw_folder+tw_file+" "+tw_dir+tw_file)
    print("TiddlyWiki saved localy")

# Check if file exists remotely
exists_remotely = os.system(
            "rclone lsf "+rclone_remote_name+":"+gdrive_tw_folder+tw_file)

exists_localy = os.system(
            "ls "+tw_dir+tw_file)

if exists_remotely != 0 & exists_localy != 0:
    print("It is impossible to syncronize. The file does not exist localy and remotely ")
elif exists_remotely != 0:
    save_remotely()
elif exists_localy != 0:
    save_localy()
else: 
    
    output = subprocess.check_output(
                "rclone copy "+rclone_remote_name+":"+gdrive_tw_folder+tw_file+" "+temp_dir, 
                shell=True)

    mtime_tw_file = os.path.getmtime(tw_dir+tw_file)
    mtime_temp_tw_file = os.path.getmtime(temp_dir+tw_file)

    if mtime_tw_file > mtime_temp_tw_file:
        save_remotely()
    elif mtime_tw_file < mtime_temp_tw_file:
        save_localy()
    else:
        print("Files are syncronized")

   
