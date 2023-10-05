import os
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description="\
    mewwwwwwzik copier to make songs appear in right album order on the screen \
    from a flash drive inserted into the 2020 EX honda civic hatchback infotainment system"
)
parser.add_argument('--dest', '-d', type=str, required=True, help="destination folder")
parser.add_argument('--src', '-s', type=str, required=True, help="source folder")
args = parser.parse_args()

subprocess.run(['mkdir', args.dest])

for root, dirs, files in os.walk(args.src):
    files.sort()
    for name in files:
        if name == ".DS_Store" or name == "DG1__DS_DIR_HDR" or name == "desktop.ini":
            continue
        src = os.path.join(root, name)
        dest = '/'.join([args.dest] + src.split('/')[3:])
        print("Copy", src, "to", dest)
        subprocess.run(['cp', src, dest])
    dirs.sort()
    for name in dirs:
        src = os.path.join(root, name)
        dest = '/'.join([args.dest] + src.split('/')[3:])
        print("Create", dest)
        subprocess.run(['mkdir', dest])

subprocess.run(['sync'])
