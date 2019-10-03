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
        print ('Directory ', dir_name, ' already exist.')

    # go through file structure to rename different
    for filenames in os.walk('./emojis'):
        for file_list in filenames:
            for file_name in file_list:
                if file_name.endswith(('.png')):
                    root, dirs, files = filenames
                    source_file = root + '/' + files[0]
                    destination_file = 'new_emojis/' + root[9:] + '.png'
                    print source_file, destination_file
                    copyfile(source_file, destination_file)
  
# driver code and call for main() fn
if __name__ == '__main__': 
    main() 