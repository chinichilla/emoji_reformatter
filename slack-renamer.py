# Pythono3 code to rename multiple files in a directory or folder 
# References:
# https://www.geeksforgeeks.org/rename-multiple-files-using-python/ 


# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("xyz"): 
        dst ="Hostel" + str(i) + ".jpg"
        src ='xyz'+ filename 
        dst ='xyz'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 