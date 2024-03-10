#!/usr/bin/env python

import sys
import os
import re
from argparse import ArgumentParser, FileType
import time  



PRETTY_RED = '\033[91m'
END_COLOR = '\033[0m'

def color_find(pattern, string, ignore_case):
    """Find all matches of pattern in string. Returns colored string, or empty string if not found."""
    flags = re.IGNORECASE if ignore_case else 0
    pattern_regex = re.compile(pattern, flags)
    return pattern_regex.sub(f"{PRETTY_RED}{pattern}{END_COLOR}", string)

def grep_stdin(pattern, color, ignore_case, print_lineno, count):
    """Search input from standard input."""
    matched_lines_count = 0
    for lineno, line in enumerate(sys.stdin, start=1):
        if re.search(pattern, line, re.IGNORECASE if ignore_case else 0):
            matched_lines_count += 1
            if print_lineno:
                sys.stdout.write(f"{lineno}: ")
            sys.stdout.write(color_find(pattern, line, ignore_case))
            sys.stdout.write('\n')
    if count:
        sys.stdout.write(f"Total matched lines: {matched_lines_count}\n")

def grep_file(filename, pattern, color, ignore_case, print_lineno, count):
    """Search a single file."""
    try:
        matched_lines_count = 0
        with open(filename, 'r') as f:
            for lineno, line in enumerate(f, start=1):
                if re.search(pattern, line, re.IGNORECASE if ignore_case else 0):
                    matched_lines_count += 1
                    if print_lineno:
                        sys.stdout.write(f"{lineno}: ")
                    sys.stdout.write(color_find(pattern, line, ignore_case))
                    sys.stdout.write('\n')
        if count:
            sys.stdout.write(f"Total matched lines in {filename}: {matched_lines_count}\n")
    except FileNotFoundError:
        sys.stderr.write(f"grep: {filename}: No such file or directory\n")
    except IsADirectoryError:
        sys.stderr.write(f"grep: {filename}: Is a directory\n")

def grep_files(paths, pattern, recurse, color, ignore_case, print_lineno, count):
    """Search files and directories."""
    for path in paths:
        if os.path.isfile(path):
            grep_file(path, pattern, color, ignore_case, print_lineno, count)
        elif os.path.isdir(path):
            if recurse:
                more_paths = [os.path.join(path, child) for child in os.listdir(path)]
                grep_files(more_paths, pattern, recurse, color, ignore_case, print_lineno, count)
            else:
                sys.stderr.write(f"grep: {path}: Is a directory\n")

def setup_parser():
    """Configure command line argument parser object."""
    github_link_info = "Created by Rushi Chaganti checkout some other projects here: https://github.com/RushiChaganti/"
    
    description = 'Find matches of a pattern in lines of file(s).' +"\n"+ github_link_info
    parser = ArgumentParser(description=description, add_help=False)
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('pattern', type=str, help='the pattern to find (enclose in quotes)')
    parser.add_argument('FILES', metavar='FILES', nargs='*', default=['-'], help="the files(s) to search.")

    group = parser.add_argument_group('options')
    group.add_argument('--color', '--colour', action='store_true', help='highlight matches')
    group.add_argument('-h', '--no-filename', action='store_false', help='suppress printing filenames when multiple files are searched')
    group.add_argument('-i', '--ignore-case', action='store_true', help='case-insensitive search')
    group.add_argument('-n', '--line-number', action='store_true', help='print line numbers')
    group.add_argument('-c', '--count', action='store_true', help='print only a count of matched lines per file')
    group.add_argument('-R', '-r', '--recursive', action='store_true', help='recursively search directories')

    return parser

def main():
    start_time = time.time() 
    parser = setup_parser()
    args = parser.parse_args()

    pattern = args.pattern.strip('"')  

    if '|' in pattern:
        sub_patterns = pattern.split('|')
        pattern = '|'.join([re.escape(sub_pattern) for sub_pattern in sub_patterns])

    files = args.FILES

    print_lineno = args.line_number
    count = args.count


    if files == ['-']:
        grep_stdin(pattern, args.color, args.ignore_case, print_lineno, count)
    else:
        grep_files(files, pattern, args.recursive, args.color, args.ignore_case, print_lineno, count)

    end_time = time.time()  
    elapsed_time = end_time - start_time 
    print(f"Query time: {elapsed_time:.2f} seconds")  

if __name__ == '__main__':
    main()
