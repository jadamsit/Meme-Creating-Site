#!/usr/bin/env python2

import os
import zipfile
import shutil

#copy files to a target folder
def docopy(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            #print os.path.join(subdir, file)
            shutil.copy2(os.path.join(subdir, file), target_folder)

#copy to backup folder
source_folder = '../assets/images'
target_folder = '/home/webadmin/backups/images'
docopy(source_folder, target_folder)
