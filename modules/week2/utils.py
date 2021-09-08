from io import TextIOWrapper
import os
from typing import List

OUTPUT = "files/output.csv"
FOLDER = "modules/week2/folders"


def get_file_names(folderpath, out=OUTPUT):
    """takes a path to a folder and writes all filenames in the folder to a specified output file"""
    dir_list = os.listdir(folderpath)
    with open(out, "w") as file:
        for line in dir_list:
            file.write(line + "\n")


def get_all_file_names(folderpath, out=OUTPUT):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

    def write_dir_to_file(file: TextIOWrapper, dir: List[str], folderpath: str):
        for line in dir:
            path_to_file = f"{folderpath}/{line}"
            if os.path.isdir(path_to_file):
                write_dir_to_file(file, os.listdir(path_to_file), path_to_file)
                continue
            file.write(line + "\n")

    with open(out, "w") as file:
        write_dir_to_file(file, os.listdir(folderpath), folderpath)


def print_line_one(file_names: List[str]):
    """takes a list of filenames and print the first line of each"""
    for file_name in file_names:
        with open(file_name) as file:
            print(file.readline())


def print_emails(file_names: List[str]):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file_name in file_names:
        with open(file_name) as file:
            for line in file.readlines():
                if "@" in line:
                    print(line)


def write_headlines(md_files: List[str], out=OUTPUT):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    with open(out, "w") as output_file:
        for md_file in md_files:
            with open(md_file) as file:
                for line in file.readlines():
                    if line.startswith("#"):
                        output_file.write(line)
