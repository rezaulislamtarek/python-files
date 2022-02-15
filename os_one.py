import os


def display_cwd():
    cwd = os.getcwd()
    print(f"current working directory: {cwd}")


def up_one_directory_level():
    os.chdir("../")


def display_entries_in_directory(directory):
    print("------------------------Scandir Call-----------------------------")
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name of entry: ", entry.name)


if __name__ == "__main__":
    display_cwd()
    up_one_directory_level()
    display_cwd()
    display_entries_in_directory(os.getcwd()+"/PythonProject1")
