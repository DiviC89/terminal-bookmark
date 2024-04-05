import os
import sys

from typer import Typer

app = Typer()


def getDivider():
    path_divider = "/"
    if os.name == "nt":
        path_divider = "\\"
    return path_divider


def checkBookmarks():
    home_path = os.path.expanduser("~")
    home_content = os.listdir(home_path)
    if not ".bookmarks" in home_content:
        print("No bookmarks made yet")
        return True
    return False


def setup(bookmark):
    if bookmark is not None:
        bookmark = bookmark.lower()
    current_dirr = os.getcwd()
    home_path = os.path.expanduser("~")
    if current_dirr is None or home_path is None:
        Exception("Could not find the current working directory or home directory.")
    return current_dirr, home_path, bookmark


@app.command()
def bookmark(bookmark: str):
    current_dirr, home_path, bookmark = setup(bookmark)
    home_content = os.listdir(home_path)
    path_divider = getDivider()
    if not ".bookmarks" in home_content:
        with open(f"{home_path}{path_divider}.bookmarks", "w") as file:
            file.write(f"{bookmark}:{current_dirr}")
    else:
        with open(f"{home_path}{path_divider}.bookmarks", "r") as file:
            for line in file.readlines():
                if bookmark in line or current_dirr in line:
                    print(
                        f"Already in use:\n{line.split(':')[0]}\n{':'.join(line.split(':')[1:])}"
                    )
                    return
            file = open(f"{home_path}{path_divider}.bookmarks", "a")
            file.write(f"\n{bookmark}:{current_dirr}")


@app.command()
def go(bookmark: str):
    err = checkBookmarks()
    if err:
        return
    _, home_path, bookmark = setup(bookmark)
    path_divider = getDivider()
    with open(home_path + path_divider + ".bookmarks", "r") as file:
        for line in file.readlines():
            if line.split(":")[0] == bookmark:
                sys.stdout.write(":".join(line.split(":")[1:]).strip("\n"))
                return
    print(bookmark + " was not found")


@app.command()
def list():
    err = checkBookmarks()
    if err:
        return
    _, home_path, bookmark = setup(None)
    path_divider = getDivider()
    with open(home_path + path_divider + ".bookmarks", "r") as file:
        for line in file.readlines():
            bookmark = line.split(":")[0]
            path = ":".join(line.split(":")[1:])
            print(f"Bookmark: {bookmark}\nPath: {path}\n")


@app.command()
def remove(bookmark):
    err = checkBookmarks()
    if err:
        return
    _, home_dirr, bookmark = setup(bookmark)
    path_divider = getDivider()
    with open(f"{home_dirr}{path_divider}.bookmarks", "r+") as file:
        copy = file.readlines()
        file.seek(0)
        for line in copy:
            if line.split(":")[0] != bookmark:
                file.write(line)
        file.truncate()
    print(f"{bookmark} has now been removed from your list")


if __name__ == "__main__":
    app()

