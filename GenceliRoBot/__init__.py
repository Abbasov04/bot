from os.path import dirname, basename, isfile, join
import glob

plugin = glob.glob(join(dirname(file), "*.py"))
all = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("init.py")
]
