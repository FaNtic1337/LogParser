# LogParser

Arguments for main.py

usage: main.py [-h] -p PATH -re REGEXP [-fre FILEREGEXP] [-sf SAVEFILE]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Enter the path to your directory with log files - required
  -re REGEXP, --regexp REGEXP
                        Enter the mask of regular expression for parsing inside log file - required
  -fre FILEREGEXP, --fileregexp FILEREGEXP
                        Enter the mask of regular expression to define log files for parsing
  -sf SAVEFILE, --savefile SAVEFILE
                        Enter the absolute path for save file, by deafult it is Result <time>.txt in same directory with main.py
