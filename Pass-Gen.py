import numbers
import random
from secrets import choice
import string
import msvcrt

print("""


""")
print("██████╗░░█████╗░░██████╗░██████╗░░░░░░░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██╔══██╗██╔══██╗██╔════╝██╔════╝░░░░░░██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("██████╔╝███████║╚█████╗░╚█████╗░█████╗██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
print("██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗╚════╝██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print("██║░░░░░██║░░██║██████╔╝██████╔╝░░░░░░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
print("╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")

print("""

Password time


1)Small
2)Big
3)God Password""")


Small_Password =  random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)  + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)  +  choice(["!","@","#","$","%","^","&","*","(",")","_"]) + choice(["!","@","#","$","%","^","&","*","(",")","_"]) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
Big_Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)+ random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)  + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + choice(["!","@","#","$","%","^","&","*","(",")","_"]) +  choice(["!","@","#","$","%","^","&","*","(",")","_"]) + choice(["!","@","#","$","%","^","&","*","(",")","_"]) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
God_Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)+ random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)  + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) +  choice(["!","@","#","$","%","^","&","*","(",")","_"]) +  choice(["!","@","#","$","%","^","&","*","(",")","_"]) +  choice(["!","@","#","$","%","^","&","*","(",")","_"]) +  choice(["!","@","#","$","%","^","&","*","(",")","_"]) + choice(["!","@","#","$","%","^","&","*","(",")","_"]) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)  + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)

respuesta = int(input())

unicas_res = ["1","2","3"]

if respuesta == 1:
    print("Password:   " + Small_Password )
elif respuesta == 2:
    print("Password:   " + Big_Password)
elif respuesta == 3:
    print("Password:   "   + God_Password)
elif respuesta not in unicas_res:
    print(respuesta + "Invalid password type")

 

msvcrt.getch()

