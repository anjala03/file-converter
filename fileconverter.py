#Write a script to convert all files in a folder recursively to .txt format
import os
import shutil
#prints all the directories of os, print (dir(os))
# print (os.getcwd()) #gives you the curren working directory
# os.chdir('/root/interntask') #changing the directory as mentioned in the parameter
# print(os.listdir())#lists all the files in that directory
# os.mkdir('destination')# will throw error if try to make sub dir when creating  main directory
# os.makedirs('destination/files')#can make sub directory at the time of main directory formation



def file_converter_with_shutil(sourcefolder, destination_folder):
    try:
        if os.path.exists(sourcefolder):
            if os.path.exists(destination_folder):
                shutil.rmtree("destination/")
                #this is to handle manual removal of folder in case it already exists.
            shutil.copytree(sourcefolder,destination_folder)
            for dirpath, dirnames, filenames in os.walk(destination_folder):
                # print(f'"path_is:" {dirpath}, "directory:{dirnames}", "files:"{filenames}')
                for each_filename in filenames:
                    print("hiiii, this is before the conversion ")
                    print(each_filename)
                    newfile_name= each_filename.replace(each_filename.split('.')[1] , 'txt')
                    #the above will only convert the file name into txt form in terminal but changes is required in destination folder, so os.rename
                    newfile=os.rename(os.path.join(dirpath,each_filename), os.path.join(dirpath,newfile_name))
                    print("this is for file only inside the folder")
                    print(newfile)                                      
                        
        else:
            print("sourcefolder doesnot exists")

    except Exception as e:
        print("error message",e)


sourcepath=r"folder/"
destinationpath=r"destination/"
file_converter_with_shutil(sourcepath, destinationpath)