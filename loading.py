#pip install os
#pip install time
#pip install colorama
#pip install tqdm
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time

for i in tqdm (os.listdir("known_faces"),  
               desc=Fore.RED + "Loading. . .",  
               ascii=False, ncols=75): 
    time.sleep(0.01)       

#the Fore.GREEN adds colour to the loading bar
print(Fore.GREEN + "Complete. . .") 
time.sleep(1) 
#this will clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')