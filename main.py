from argparse import ArgumentParser
from pathlib import Path
from datetime import datetime
from progress.bar import IncrementalBar
import re, os

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


def parseFile(path, reg_exp, savefile):

    with open(path, 'r') as log:

        listed_log = [line.strip() for line in log]

        # Progress bar and info
        print(f'\nStart parse file "{path}"\n')
        bar = IncrementalBar(max=len(listed_log))

        with open(savefile, 'w+') as result:

            # Parsing info
            result.write(f"Parsing file: {path}\n\n")
            result.write(f"Parsing start time: {datetime.now()}\n\n")
            result.write(f"Regular expression mask: '{reg_exp}'\n\n")

            # Writing parse data in file
            for index, line in enumerate(listed_log):
                bar.next()
                if re.search(reg_exp, line):
                    result.write(f"{index}. {line}\n")
            bar.finish()

            print(f'\nParsing file "{path}" successfully ended!')
            print(f'Check your results in "{savefile}"\n')


def parseDir(path, reg_exp, file_reg_exp, savefile):

    writemode = 'w'

    if file_reg_exp is not None:
        log_files = []
        for file in os.listdir(path):
            if re.search(file_reg_exp, file):
                log_files.append(os.path.join(path, file))
    else:
        log_files = []
        for file in os.listdir(path):
            if file.endswith('.log') or file.endswith('.txt'):
                log_files.append(os.path.join(path, file))


    for i in range(len(log_files)):

        with open(log_files[i], 'r') as log:

            listed_log = [line.strip() for line in log]

            # Progress bar and info
            print(f'\nStart parse file "{path}"\n')
            bar = IncrementalBar(max=len(listed_log))

            if i > 0:
                writemode = 'a'

            with open(savefile, writemode) as result:

                # Parsing info
                result.write(f"Parsing file: {log_files[i]}\n\n")
                result.write(f"Parsing start time: {datetime.now()}\n\n")
                result.write(f"Regular expression mask: '{reg_exp}'\n\n")

                # Writing parse data in file
                for index, line in enumerate(listed_log):
                    bar.next()
                    if re.search(reg_exp, line):
                        result.write(f"{index}. {line}\n")
                bar.finish()
                result.write("\n" * 3)
                print(f'\nParsing file "{log_files[i]}" successfully ended!')


    print(f'Check your results in "{savefile}"\n')



def parseLogs(filepath, reg_exp, file_reg_exp, savefile):
    path = Path(filepath)

    if path.suffix == '.log' or path.suffix == '.txt':
        parseFile(path, reg_exp, savefile)
    elif path.suffix == '':
        parseDir(path, reg_exp, file_reg_exp, savefile)
    else:
        print('Incorrect path to file')


if __name__ == '__main__':
    parseLogs(args.path, args.regexp, args.fileregexp, args.savefile)
