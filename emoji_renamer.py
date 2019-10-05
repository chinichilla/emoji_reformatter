import os
from shutil import copyfile

# function to rename multiple files
def main():
    # make new folder called new_emojis if necessary
    path = os.getcwd()
    try: 
        os.makedirs(path + '/new_emojis')
        print('new_emojis folder created.')
    except:
        print('new_emojis folder already exists.')

    # go through file structure to rename and reduce the number of folders
    # destination_file is inside new_emojis rather than being nested in another folder
    for root, dirs, files in os.walk('./emojis', topdown=False):
        if len(files) > 0:
            print(files)
            source_file = root + '/' + files[0]
            # filters for png, gif, and jpg
            if (source_file.endswith('.png') or source_file.endswith('.gif') or source_file.endswith('.jpg')):
                print(files)
                destination_file = 'new_emojis/' + root[9:] + source_file[-4:]          
                copyfile(source_file, destination_file)

    print('The emoji_renamer has finished running.')


# driver code and call for main() fn
if __name__ == "__main__":
    main()
