import sys
import os

current_dir = os.path.dirname( os.path.realpath(__file__))
import_path = '/'.join(current_dir.split('/')[:-1])
sys.path.append( import_path )
print( import_path )


from lib import mylib

mylib.somefunc()
