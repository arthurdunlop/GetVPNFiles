from distutils.log import error
import shutil, os

input_source = input("Enter source path where you want to look for files:")
source = r"\\10.7.8.4\dpc\NF liberadas por TAX"

input_destination = input("Enter path where you wish to copy files for:")
destination = r"C:\Users\mmga\Desktop\Servi�os - Jurong"

input_files_names = input("Enter file names separeted with ',':")
files_names =  input_files_names.split(",")

try:
    
    for path, currentDirectory, files in os.walk(source):
        for file in files:
            
            pathComplete = os.path.join(path, file)
            print("Processing file: " + pathComplete)

            if(pathComplete.endswith(".pdf")):
          
                if any(substring.replace(" ","").lower() in file.replace(" ","").lower() for substring in files_names):

                    oldPath = os.path.join(destination, file)
                    
                    date = pathComplete[len(source): len(source) + 8].replace("\\", "")
                    newPath = os.path.join(destination,date + " - " + file)

                    newPathExists = os.path.exists(newPath)

                    if(newPathExists == False):

                        shutil.copy(pathComplete, destination)
                        os.rename(oldPath, newPath)

                        logStringSuccess = "Succeded to copy file to:" + newPath
                        print(logStringSuccess)
except Exception as error:
    print(error)


