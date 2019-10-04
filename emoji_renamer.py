import os
from shutil import copyfile

# function to rename multiple files
def main():
    # make new folder if necessary
    path = os.getcwd()

    try: 
        # make new_emojis folder
        os.makedirs(path + '/new_emojis')
        print('Directory created.')
    except:
        print('Directory already exists.')

    # go through file strcuture to rename and reduce the number of folders
    destination_file = ''
    rootDir = './emojis'
    for root, dirs, files in os.walk(rootDir, topdown=False):
        if (len(files)>0):
            source_file = root + '/' + files[0]
            if source_file.endswith(('.png')):
                destination_file = 'new_emojis/' + root[9:] + '.png'
                copyfile(source_file, destination_file)
            elif source_file.endswith(('.jpg')):
                destination_file = 'new_emojis/' + root[9:] + '.jpg'
                copyfile(source_file, destination_file)
            elif source_file.endswith(('.gif')):
                destination_file = 'new_emojis/' + root[9:] + '.gif'
                copyfile(source_file, destination_file)


# driver code and call for main() fn
if __name__ == "__main__":
    main()