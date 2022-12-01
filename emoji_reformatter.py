import os
from shutil import copyfile

# function to reformat multiple files
def main():
    # check if emojis folder exists and print message if false
    rootDir = './emojis'
    if(os.path.isdir(rootDir)):
        # make reformatted folder called reformatted_emojis if necessary
        path = os.getcwd()
        try: 
            os.makedirs(path + '/reformatted_emojis')
            print('reformatted_emojis folder created.')
        except:
            print('reformatted_emojis folder already exists.')
        
        reformatted_files = 0
        unformatted_dirs = []
        # go through file structure to reformat and reduce the number of folders in rootDir
        # destination_file is inside reformatted_emojis rather than being nested in another folder
        for root, dirs, files in os.walk(rootDir, topdown=False):
            # checks for at least one file in an array (there should only be one in this case)
            if len(files) > 0:
                source_file = root + '/' + files[0]
                # filters for png, gif, and jpg (let me know if slack uses other file types)
                if (source_file.endswith('.png') or source_file.endswith('.gif') or source_file.endswith('.jpg')):
                    reformatted_files += 1
                    root_converted = root[len(rootDir)+1:].replace("%27", "'")
                    destination_file = 'reformatted_emojis/' + root_converted + source_file[-4:]
                    copyfile(source_file, destination_file)
                else:
                    unformatted_dirs.append(root[len(rootDir)+1:])
            else:
                unformatted_dirs.append(root[len(rootDir)+1:])
        print('The emoji_reformatter has finished running. ' + str(reformatted_files) + ' of ' + str(len(dirs)) + ' files have been reformatted.')
        # troubleshooting: give folder names for files that still need to be reformatted (>1 since ./emojis is always added to the array)
        if (len(unformatted_dirs) > 1):
            separator = ', '
            print('The following folders were not reformatted: ' + str(separator.join(unformatted_dirs))[:-2])
    else:
        print('The emojis folder does not exist. Please copy it into the emoji_reformatter folder or look at the README.')




# driver code and call for main() fn
if __name__ == "__main__":
    main()
