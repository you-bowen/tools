import os
import sys

file = sys.argv[1]
os.system('pyinstaller -F --noupx {}'.format(file))
