import face_recognition
import os
import pandas
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time
from operator import sub

current_found = []
current_notfound = []
for i in os.listdir("known_faces"):
    present_name = i.split(".")[0]
    current_notfound.append(present_name)

for i in tqdm (os.listdir("known_faces"),  
               desc=Fore.YELLOW + "Detection In Progress",  
               ascii=False, ncols=75):     
      
      for j in tqdm (os.listdir("unknown_faces"),  
               desc=Fore.RED + "Checking "+i.split(".")[0],  
               ascii=False, ncols=75):    
       known_image = face_recognition.load_image_file("known_faces/"+i)
       unknown_image = face_recognition.load_image_file("unknown_faces/"+j)
       try:
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        present_name = i.split(".")[0]
        absent = []
        if results[0]:
         if present_name in current_found:
             pass
         else:     
             current_found.append(present_name)
       except:
           pass
print(Fore.GREEN + "Completed. . .Loading List") 
# time.sleep(5) 
# os.system('cls' if os.name == 'nt' else 'clear')
print("presentList -->",current_found)     
print("AbsentList -->",list(set(current_notfound) - set(current_found)))
