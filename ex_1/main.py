import sys
from classes import Sorter

if __name__ == "__main__":
    if len(sys.argv) == 2:
        source = sys.argv[1]
        sorter = Sorter(source_path=source)
        sorter.run()
    elif len(sys.argv) == 3:
        source = sys.argv[1]
        dest = sys.argv[2]
        sorter = Sorter(source_path=source, dest_path=dest)
        sorter.run()

