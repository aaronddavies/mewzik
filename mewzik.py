import os
import subprocess

DEST = '/media/adavies/4418-C39F'

for root, dirs, files in os.walk('/tmp/Music'):
    files.sort()
    for name in files:
        if name == ".DS_Store" or name == "DG1__DS_DIR_HDR" or name == "desktop.ini":
            continue
        src = os.path.join(root, name)
        dest = '/'.join([DEST] + src.split('/')[3:])
        print("Copy", src, "to", dest)
        subprocess.run(['cp', src, dest])
    dirs.sort()
    for name in dirs:
        src = os.path.join(root, name)
        dest = '/'.join([DEST] + src.split('/')[3:])
        print("Create", dest)
        subprocess.run(['mkdir', dest])

subprocess.run(['sync'])
