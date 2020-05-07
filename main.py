import sys
import getopt
from scripts.directory_structure import build_directory_structure

input_dir = 'input'
output_dir = 'output'


def main(argv):
    global input_dir
    global output_dir
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["idir=", "odir="])
    except getopt.GetoptError:
        print('main.py -i <input_dir> -o <output_dir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--idir"):
            input_dir = arg
        elif opt in ("-o", "--odir"):
            output_dir = arg


# read parameter from command line
if __name__ == "__main__":
    main(sys.argv[1:])

# build directory structure with html pages
build_directory_structure(input_dir, output_dir)

