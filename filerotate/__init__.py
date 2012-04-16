import os
import __version__

__version__ = __version__.__version__

def forward(file):
    try:
        name, ext = os.path.splitext(file)
        os.rename(file, "{0}.{1}".format(name, int(ext[1:]) + 1))
    except ValueError: # Not a number extension
        os.rename(file, "{0}.{1}".format(file, 0)) 
            
def backward(file):
    try:
        name, ext = os.path.splitext(file)
        ext = int(ext[1:])
        if ext == 0:
            os.rename(file, name)
        else:
            os.rename(file, "{0}.{1}".format(name, ext - 1))
    except ValueError: # Not a number extension, nothing to rotate
        pass

def iter(files, rename):
    for file in files:
        if not os.path.isdir(file) and not os.path.isfile(file):
            continue
        rename(file)

def rotate():
    from __main__ import opts, files

    files.sort()
    
    if opts.back:
        iter(files, backward)
    else:
        files.reverse()
        iter(files, forward)
    

if __name__ == "__main__":
    rotate()