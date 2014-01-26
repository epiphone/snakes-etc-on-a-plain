import os
import re
from distutils.core import setup
import py2exe

datafiles = []

for files in os.listdir('./resources/'):
    f1 = './resources/' + files
    if os.path.isfile(f1):
        f2 = 'resources', [f1]
        datafiles.append(f2)
    else:
        if files == 'audio':
            for filest in os.listdir('./resources/audio/'):
                f2 = './resources/audio/' + filest
                if os.path.isfile(f2):
                    f3 = 'resources/audio', [f2]
                    datafiles.append(f3)

for files in os.listdir('./'):
    matchObj = re.search( r'map\d.txt', files, re.M|re.I)
    f1 = './' + files
    if matchObj:
        f2 = '', [f1]
        datafiles.append(f2)

setup(windows=['game.py'],
      data_files = datafiles,
      name="snakes-etc-on-a-plain",
      options={
        "py2exe": {
            "dist_dir": "../release/win32",
            "optimize": 2,
            "bundle_files": 2
        }
})
