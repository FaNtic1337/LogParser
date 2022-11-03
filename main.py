from argparse import ArgumentParser
from pathlib import Path
from datetime import datetime

# Setup arguments for LogParser
AP = ArgumentParser()

# Filepath for parsing file, required
AP.add_argument('-p', '--path', help='Enter the path to your directory with log files', required=True)
# RegExp mask to parse inside file/files, required
AP.add_argument('-re', '--regexp', help='Enter the mask of regular expression for parsing inside log file', required=True)
# File RegExp mask to parse inside directory current files to parse, optional
AP.add_argument('-fre', '--fileregexp', help='Enter the mask of regular expression to define log files for parsing')
# Filepath for saving results, optional
AP.add_argument('-sf', '--savefile', help='Enter the absolute path for save file,'
                ' by deafult it is Result <time>.txt in same directory with main.py',
                default=f'Result {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.txt')

args = AP.parse_args()


def parseLogs(filepath, reg_exp, file_reg_exp, savefile):
    path = Path(filepath)

    if path.suffix == '.log' or path.suffix == '.txt':
        print(f'Read file at path ({path}), parse file by RegExp ({reg_exp}), save in file at path ({savefile})')
    elif path.suffix == '':
        print(f'Read all files at path ({path}), parse files by FileRegExp ({file_reg_exp}), parse current files by RegExp ({reg_exp}), save in file at path ({savefile})')
    else:
        print('Incorrect path to file')


if __name__ == '__main__':
    parseLogs(args.path, args.regexp, args.fileregexp, args.savefile)
