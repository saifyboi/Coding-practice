#read file directory operations
def file_reader(path):
   try:
      with open(path, 'r') as file:
         content = file.read()
         print(f"the content of {path} is: \n{content}")
   except FileNotFoundError:
      print("Incorrect file name, or file does not exist.")
   except Exception as e:
      print(f"file exists, but something went wrong while reading it:{e}")
      
file_reader("/home/saify/Desktop/spl_letter")
