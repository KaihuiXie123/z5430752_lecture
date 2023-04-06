""" lec_fileio.py
Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')

# ----------------------------------------------------------------------------
#   Writing content to a file
# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")



with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is a another line')
print_lines(DSTFILE)



# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
# ----------------------------------------------------------------------------
def print_lines_rstrip(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: '{line.rstrip()}'")

#
with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is a another line')
print_lines_rstrip(DSTFILE)
#


# ----------------------------------------------------------------------------
#   Quiz: Create the save_open function here
# ----------------------------------------------------------------------------
def safe_open(pth, mode):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.
    Will not open a file in writing mode if the file already exists and has
    some content.
    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
    """
    pass