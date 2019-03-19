import os
def rename_files():
    file_list = os.listdir("/Users/macbook/Desktop/prank") 
    print (file_list)
    saved_file = os.getcwd()
    os.chdir("/Users/macbook/Desktop/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate
    print("current working is " +saved_file)
rename_files()