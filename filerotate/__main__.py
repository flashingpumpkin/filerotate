import __version__
import optparse
import sys

parser = optparse.OptionParser()
parser.usage = '%prog [glob]'
parser.add_option('-v', '--version', dest = 'version', action = 'store_true',
    help = "Display version and exit")
opts, files = parser.parse_args()

if opts.version:
    print __version__.__version__
    sys.exit(0)