import zipfile
import pathlib


def make_zip(filepaths, dest_dir):
    filepath = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(filepath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)  # removing the sub-folders in the path
