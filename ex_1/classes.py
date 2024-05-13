from pathlib import Path
import shutil
from threading import Thread


class Sorter:
    __source_path = None
    __destination_path = None

    def __init__(self, source_path: str, dest_path: str = "dist"):
        self.__source_path = Path(source_path)
        self.__destination_path = self.__source_path.parent.joinpath(Path(dest_path))

    def run(self):
        abs_path = self.__source_path.absolute()
        self.__sort_current_dir(abs_path)

    def __create_dest_location(self, path: Path, name: Path) -> Path:
        Path.mkdir(path.joinpath(Path(name)), parents=True, exist_ok=True)
        return path.joinpath(Path(name))

    def __sort_current_dir(self, path: Path):
        for item in path.iterdir():
            if item.is_dir():
                tr = Thread(name=f"thread_{item}", target=self.__sort_current_dir, args=(item,))
                tr.start()
                tr.join()
                Path.rmdir(item)
            else:
                tr = Thread(name=f"thread_{item}", target=self.__move_items,
                            args=(item, self.__destination_path, Path(item.suffix[1::])))
                tr.start()
                tr.join()

    def __move_items(self, item: Path, target_path: Path, target_name: Path):
        dest_dir = self.__create_dest_location(target_path, target_name)
        shutil.move(item, dest_dir)
