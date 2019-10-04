import os
from shutil import copyfile

# function to rename multiple files
def main():
    # make new folder if necessary
    path = os.getcwd()
    try: 
        os.makedirs(path + '/new_emojis')
        print('Directory created.')
    except:
        print('Directory already exists.')

    # go through file structure to rename and reduce the number of folders
    # destination_file is inside new_emojis rather than being nested in another folder
    destination_file = ''
    for root, dirs, files in os.walk('./emojis', topdown=False):
        if (len(files)>0):
            source_file = root + '/' + files[0]
            # filters for png, gif, and jpg
            if source_file.endswith('.png' or '.gif' or '.jpg'):
                destination_file = 'new_emojis/' + root[9:] + source_file[-4:]          
                copyfile(source_file, destination_file)


# driver code and call for main() fn
if __name__ == "__main__":
    main()
