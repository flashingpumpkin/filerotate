__version__ = "1.0.0"

import optparse
import os


parser = optparse.OptionParser()
parser.usage = '%prog [glob]'
opts, files = parser.parse_args()

def rotate():
    files.sort()
    files.reverse()
    
    for file in files:
        try:
            name, ext = os.path.splitext(file)
            os.rename(file, "{0}.{1}".format(name, int(ext[1:]) + 1))
        except ValueError: # Not a number extension
            os.rename(file, "{0}.{1}".format(file, 0))
    

if __name__ == "__main__":
    rotate()