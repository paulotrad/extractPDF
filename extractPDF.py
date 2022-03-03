

def main():
   final=[]
   path=input("give directory for pdf files to iterate thru:")
   type=input('type of file: ')
   output_file=input('name of output file')
   textfields=input('textfields only? Y/N ')
   list_of_files=fr.readfiles(path,type)
   inter=1
   for file in list_of_files:


       # creating a pdf file object for each file
      pdfFileObj = open(file, 'rb')

      # creating a pdf reader object
      pdfReader= PyPDF2.PdfFileReader(
      pdfFileObj,
      strict=True,
      warndest=None,
      overwriteWarnings=True
      )
      # printing number of pages in pdf file
      print(pdfReader.numPages)
    # creating a page object
      pageObj = pdfReader.getNumPages()
             #print(pageObj.extractText())
    # extracting text from page
      try:
        forms=pdfReader.getFormTextFields()
      except:
        pass
      try:
        fields=pdfReader.getFields()
      except:
        pass

       # closing the pdf file object


      columns=[]
      everything=[]
      info=[]
      form={}
      time=datetime.time
      print(file)

      if fields!=None:
          for i,k in fields.items():
              try:
                print(fields[i]['/T'],"  ",fields[i]['/FT'],"    ",fields[i]['/V'])
              except:
                print(fields[i]['/T'], "  ", fields[i]['/FT'], "    ")





      if textfields=='Y':
          print(text_all(forms,file,output_file,type))
      else:
          print(fields_all(fields,file))





          for index,k in forms.items():
              columns.append(index.upper())#LIST FOR COLUMNS
              everything.append(k)
           #print(k)  #LIST OF ITEMS GOING INTO COLUMNS
          final.append(everything)    #Store each list in list next to each other
      return final,columns
      print(columns)

      pdfFileObj.close()
def fields_all(fields,file):

    with open('readme.txt', 'w') as f:
        f.write(str(fields))
    a="WRITING ALL FIELDS INTO TXT FILE"
    return a
def text_all(forms,file,output_file,type):

    file_name = "WRITING TEXT ENTRYS INTO TXT FILE FROM FILE:\n"+file

    file = open(output_file+".txt", "w")
    file.truncate(0)
    for key,value in forms.items():
       a=(60-len(key))
       modify = "_"
       for i in range(a):
           modify+="_"

       file.write(key+modify+str(value)+"\n")
    file.close()


    return file_name

if __name__ == "__main__":
 #importing required modules
   import os
   import glob, os
   import openpyxl
   import pandas as pd
   import PyPDF2
   import readfiles as fr
   import sqlite3
   import datetime
   final, columns = main()

   new_database = pd.DataFrame(data=final, columns=columns)
        # new_database=pd.concat(new_database,new,axis=1)

   new_database.to_excel("data.xlsx", index=False)

