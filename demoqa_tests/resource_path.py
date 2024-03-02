from pathlib import Path


def path_photo(name):
    return str(Path(__file__).parent.joinpath('resources', name))
print("Полный путь к файлу:", path_photo('123.jpeg'))
