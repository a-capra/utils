import glob, os, shutil
import argparse

# reference:
# https://stackoverflow.com/a/800201
def get_immediate_subdirectories(a_dir):
    a_dir.replace('\\','/')
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

# reference:
# https://stackoverflow.com/a/296184
def scan_subdirectories(a_dir,ext,dest):
    print(f'scanning {a_dir}')
    for dir in get_immediate_subdirectories(a_dir):
        mypath=a_dir+'/'+dir
        scan_subdirectories(mypath,ext,dest)
        files = glob.iglob(os.path.join(mypath, ext))
        for f in files:
             if os.path.isfile(f):
                 print(f'Copying {f} to {dest}') 
                 shutil.copy2(f, dest)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='copy_all_files')
    parser.add_argument('folder', help="origin and destination")
    args = parser.parse_args()

    file_types=["*.rwa","*.dta","*.json"]
    for ext in file_types:
        print('Copying',ext,'files...')
        scan_subdirectories(args.folder,ext,args.folder)
