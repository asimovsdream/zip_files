import zipfile
import pathlib


def make_zip(filepaths, dest_dir):
    path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_zip(filepaths=["bonus2.py", "bonus1.py"], dest_dir="dest")
