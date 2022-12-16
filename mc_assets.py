from json import load
from pathlib import Path
from os import makedirs

# from os import listdir

VERBOSE = False
ASSETS_ROOT = Path("path/to/.minecraft/assets")
INDEX = ASSETS_ROOT / "indexes" / "1.18.json"
OBJECTS = ASSETS_ROOT / "objects"
SAVE = Path("./Minecraft assets/")
assert ASSETS_ROOT.is_dir()
assert INDEX.is_file()
assert OBJECTS.is_dir()
assert SAVE.is_dir()


with open(INDEX) as f:
    index = load(f)
index: dict = index["objects"]

for mapped, value in index.items():
    mapped: str
    mapped_path = SAVE / mapped
    if not mapped_path.parent.is_dir() and not VERBOSE:
        makedirs(mapped_path.parent)
    hash: str = value["hash"]
    orig_path = OBJECTS / hash[0:2] / hash
    assert orig_path.is_file()
    print(f"{orig_path} -> {mapped_path}")
    if not VERBOSE:
        with open(orig_path, 'rb') as f:
            content = f.read()
        with open(mapped_path, 'wb') as f:
            f.write(content)
