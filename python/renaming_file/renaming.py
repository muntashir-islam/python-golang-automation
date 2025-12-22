import os


def renaming_file(directory_path):
    files = os.listdir(directory_path)
    count = 1
    for filename in files:
        if filename.endswith('.txt'):
            old_path = os.path.join(directory_path, filename)
            new_name = f'newfile_{count:03d}.txt'
            new_path = os.path.join(directory_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            count += 1


if __name__ == '__main__':
    renaming_file(
        '/Users/muntashir/work/python/hackerrank/pythonProject/python-golang-automation/python/renaming_file/example')
