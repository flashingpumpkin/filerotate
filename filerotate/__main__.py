import __version__
import optparse
import sys

parser = optparse.OptionParser()
parser.usage = '%prog [pattern]'
parser.add_option('-v', '--version', dest = 'version', action = 'store_true',
    help = "Display version and exit")
parser.add_option('-b', '--back', dest = 'back', action = 'store_true',
    help = "Rotate files that match the pattern back")
opts, files = parser.parse_args()

if opts.version:
    print __version__.__version__
    sys.exit(0)