#!/usr/bin/python3

import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(sys.argv[0], 'input_file output_file')
        sys.exit(1)
    ifile = open(sys.argv[1]).read()
    if ifile != 'This is a binary output file.\n':
        print('Malformed input')
        sys.exit(1)
    ofile = open(sys.argv[2], 'w')
    ofile.write('This is a different binary output file.\n')
