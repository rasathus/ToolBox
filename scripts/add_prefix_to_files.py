import sys
import os
import shutil
import argparse

default_ignores = ['.DS_Store']

parser = argparse.ArgumentParser(description='Add the prefix to all files in the designated path, if not on the ignores list.')
parser.add_argument("--ignores", action='append', dest='ignores')
parser.add_argument('--path', help='source path', dest='path', required=True)
parser.add_argument('--prefix', help='file prefix', dest='prefix', required=True)

args = parser.parse_args()

if args.ignores is None:
    ignores = default_ignores
else:
    ignores = default_ignores + args.ignores

file_prefix = args.prefix
folder_root = args.path

for file_name in os.listdir(folder_root):
    if file_name in ignores:
        continue
    else:
        original_path = os.path.join(folder_root, file_name)
        file_name_with_prefix = "{0}{1}".format(file_prefix, file_name)
        new_path = os.path.join(folder_root, file_name_with_prefix)
        print "Moving {0} to {1}".format(original_path, new_path)
        shutil.move(original_path, new_path)
