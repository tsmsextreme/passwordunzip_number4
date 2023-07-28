import zipfile
import os
import itertools
from concurrent.futures import ThreadPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger
passtr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
passwordlist = list(itertools.product(passtr, repeat=4)) + list(itertools.product(passtr, repeat=3))

dir_path = "./input/"
files = os.listdir(dir_path)

def unpacking(strnum, filena):
    filename = "./input/" + filena
    path = "./output/" + filena
    passwd = strnum
    with zipfile.ZipFile(filename, "r") as zp:
        try:
            zp.extractall(path=path, pwd=passwd.encode("utf-8"))
            print(filena + " : " + passwd +  " is complete.")
        except RuntimeError as e:
            pass
            

def main():
    with ThreadPoolExecutor(max_workers=1600, thread_name_prefix="thread") as executor:
        for file in files:
            for numb in passwordlist:
                strnumb = "".join(numb)
                executor.submit(unpacking, strnumb, file)

if __name__ == "__main__":
    main()