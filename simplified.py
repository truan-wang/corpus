import os
import opencc


converter = opencc.OpenCC('t2s.json')


def simplified_file(filename):
    new_content = ""

    with open(filename, "r", encoding="utf-8") as ifp:
        for line in ifp:
            new_content += converter.convert(line)

    with open(filename, "w", encoding="utf-8") as ofp:
        ofp.write(new_content)


def simlified_all_txt_files_in_dir(dir):
    for name in os.listdir(dir):
        new_name = converter.convert(name)
        if new_name != name:
            os.rename(os.path.join(dir, name), os.path.join(dir, new_name))
        full_name = os.path.join(dir, new_name)
        if os.path.isdir(full_name):
            simlified_all_txt_files_in_dir(full_name)
        elif name.lower().endswith(".txt"):
            simplified_file(full_name)


def simlified_all():
    dir = os.path.dirname(os.path.abspath(__file__))
    simlified_all_txt_files_in_dir(dir)


if __name__ == "__main__":
    simlified_all()
