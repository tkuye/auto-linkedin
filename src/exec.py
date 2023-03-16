#!bin/bash/python3

import argparse
import os
import subprocess
import pathlib
parser = argparse.ArgumentParser(description='Timer')

## A script that runs all files in a directory at a certain time.
## This script is meant to be run as a cron job.

## The script takes in a directory and a time as arguments.

## The script will then run all files in the directory at the time specified.

## The script will also log the time it was run and the files it ran.

parser.add_argument('--directory', type=pathlib.Path, help='The directory to run files from', required=True)

args = parser.parse_args()

print(args.directory)

processes = []
if not os.path.isdir(args.directory):
    print('Directory does not exist')
    exit(1)
for file in os.listdir(args.directory):
    if os.path.isfile(args.directory / file):
        if os.access(args.directory / file, os.X_OK):
            print('Running file: ' + file)
            process = subprocess.Popen(args.directory / file)
            processes.append(process)
        else:
            print('File is not executable: ' + file)
    else:
        print('File is not in directory: ' + file)

for process in processes:
    process.wait()




