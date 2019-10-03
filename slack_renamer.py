# importing os module 
import os 
from shutil import copyfile

  
# Function to rename multiple files 
def main():
    # make new folder if necessary
    path = os.getcwd()
    dir_name = path + '/new_emojis'
    try: 
        # make new emojis folder 
        os.makedirs(path + '/new_emojis')
        print ('Directory ', dir_name, ' created')
    except:
        print('Directory ', dir_name, ' already exist.')
        

    # go through file structure to rename and reduce the number of folders
    destination_file = ''
    for filenames in os.walk('./emojis'):
        for file_list in filenames:
            for file_name in file_list:
                    root, dirs, files = filenames
                    source_file = root + '/' + files[0]
                    if file_name.endswith(('.png')):
                        destination_file = 'new_emojis/' + root[9:] + '.png'
                        copyfile(source_file, destination_file)
                    elif file_name.endswith(('.jpg')):
                        destination_file = 'new_emojis/' + root[9:] + '.jpg'
                        copyfile(source_file, destination_file)
                    elif file_name.endswith(('.gif')):
                        destination_file = 'new_emojis/' + root[9:] + '.gif'
                        copyfile(source_file, destination_file)
                    print source_file, destination_file

  
# driver code and call for main() fn
if __name__ == '__main__': 
    main() 