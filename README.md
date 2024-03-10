# pygrep

## Description
`pygrep` is a Python package that provides a simple command-line tool for searching text patterns within files using regular expressions.

## Installation
pygrep is now available as a standalone Windows application! You can download it from the releases section of this repository.

## Usage
Once downloaded, you can use pygrep from the command line to search for text patterns within files. Here's the basic usage syntax:

```
  pygrep [options] pattern file1 [file2 ...]
```


Replace `pattern` with the regular expression pattern you want to search for, and `file1`, `file2`, etc., with the paths to the files you want to search within.

For example, to search for the word "example" in a file named `example.txt`, you can use the following command:

```
pygrep "example" example.txt
```
For more options and detailed usage instructions, you can use the --help option:
```
pygrep --help
```