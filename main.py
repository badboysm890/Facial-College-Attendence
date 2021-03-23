import face_recognition
import os
import pandas
current_found = []
current_notfound = []
for i in os.listdir("known_faces"):
    known_image = face_recognition.load_image_file("known_faces/"+i)
    for j in os.listdir("unknown_faces"): 
     unknown_image = face_recognition.load_image_file("unknown_faces/"+j)
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
     else:
          current_notfound.append(present_name)   
     print(current_found,current_found)

