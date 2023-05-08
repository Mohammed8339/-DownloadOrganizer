import shutil
import pathlib
import time
from pathlib import Path
import os
from os import scandir

loopIntervals = 10
pathToDownload = str(os.path.join(Path.home(), "Downloads"))

def checkDwn():
    print(pathToDownload)
    os.system(f'cd {pathToDownload}')
    dir_entries = scandir(f'{pathToDownload}')
    for entry in dir_entries:
        if entry.is_file():
            extension = pathlib.Path(entry).suffix
            clipped = extension.replace('.', '')
            dir_move = (f'{pathToDownload}/Folders/{clipped}')

            if os.path.isdir(dir_move):
                shutil.move(entry, dir_move)
            else:
               pass




while True:
    time.sleep(loopIntervals)
    print("scanned")
    checkDwn()
