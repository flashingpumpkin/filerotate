import os
import __version__

__version__ = __version__.__version__

def forward(files):
    files.sort()
    files.reverse()

    for file in files:
        try:
            name, ext = os.path.splitext(file)
            os.rename(file, "{0}.{1}".format(name, int(ext[1:]) + 1))
        except ValueError: # Not a number extension
            os.rename(file, "{0}.{1}".format(file, 0))    
            
def backward(files):
    files.sort()

    for file in files:
        try:
            name, ext = os.path.splitext(file)
            ext = int(ext[1:])
            if ext == 0:
                os.rename(file, name)
            else:
                os.rename(file, "{0}.{1}".format(name, ext - 1))
        except ValueError: # Not a number extension, nothing to rotate
            pass

def rotate():
    from __main__ import opts, files

    if opts.back:
        backward(files)
    else:
        forward(files)
    

if __name__ == "__main__":
    rotate()