
import glob, os

#find_files in path
def readfiles(path,types):
   os.chdir(path)
   names = []
   for file in glob.glob("*{}".format(types)):

       names.append(file)
   return names
