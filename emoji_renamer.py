import os
import os.path
from shutil import copyfile

# function to rename multiple files
def main():
    # check if emojis folder exists and print message if false
    if(os.path.isdir('./emojis')):
        # make new folder called new_emojis if necessary
        path = os.getcwd()
        try: 
            os.makedirs(path + '/new_emojis')
            print('new_emojis folder created.')
        except:
            print('new_emojis folder already exists.')
        # go through file structure to rename and reduce the number of folders in rootDir
        # destination_file is inside new_emojis rather than being nested in another folder
        rootDir = './emojis'
        for root, dirs, files in os.walk(rootDir, topdown=False):
            # checks for at least one file in an array (there should only be one in this case)
            if len(files) > 0:
                source_file = root + '/' + files[0]
                # filters for png, gif, and jpg (let me know if slack uses other file types)
                if (source_file.endswith('.png') or source_file.endswith('.gif') or source_file.endswith('.jpg')):
                    destination_file = 'new_emojis/' + root[len(rootDir)+1:] + source_file[-4:]          
                    copyfile(source_file, destination_file)
        print('The emoji_renamer has finished running.')
    else:
        print('The emojis folder does not exist. Please copy it into the emoji_renamer folder or look at the README.')




# driver code and call for main() fn
if __name__ == "__main__":
    main()
