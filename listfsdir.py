from os import environ,path,listdir
from sys import argv

def printdir(parent,level=0):
    try:
        for x in listdir(parent):
            full_path = parent+"/"+x
            if path.isdir(full_path): 
                print("-"*level+" "+x)
                printdir(full_path,level+1)
    except PermissionError:
        print(f"{parent} denied")



if __name__ == "__main__":

    if len(argv) == 2:
        if path.isdir(argv[1]): printdir(argv[1])
        else: print(f"{argv[1]} is not a dir")
    else:
        printdir(environ["DATADIR"])
