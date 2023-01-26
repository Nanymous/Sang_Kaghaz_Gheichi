# Sang Kaghaz Gheichi!
# or player.lower() == "k" 
# or player.lower() == "s"
# or player.lower() == "s"
# or player.lower() == "g"
# or player.lower() == "g"
# or player.lower() == "k"
# or player.lower() == "g" 
# or player.lower() == "k"
# or player.lower() == "s"
import random as _GeNeRal_, os as Nanymous, time as MaMaD, sys as gx
from colorama import Fore as gl, Style as Gl
Nanymous.system("clear" and "cls")
Nanymous.system("pip install python")
Nanymous.system("pip install python3")
Nanymous.system("pip install python2")
Nanymous.system("pip install os")
Nanymous.system("pip install sys")
Nanymous.system("pip install random")
Nanymous.system("pip install time")
Nanymous.system("pip install colorama")
Nanymous.system("clear" and "cls")

tag = """  ____         _   _
 / ___|_  __  | \ | | __ _ _ __  _   _ _ __ ___   ___  _   _ ___
| |  _\ \/ /  |  \| |/ _` | '_ \| | | | '_ ` _ \ / _ \| | | / __|
| |_| |>  <   | |\  | (_| | | | | |_| | | | | | | (_) | |_| \__ )
 \____/_/\_\  |_| \_|\__,_|_| |_|\__, |_| |_| |_|\___/ \__,_|___/
                                 |___/
"""
print(gl.GREEN)
for g in tag:
    gx.stdout.write(g)
    gx.stdout.flush()
    MaMaD.sleep(0.01)
print(Gl.RESET_ALL)




print(gl.BLUE)
tim = input("Time Shoroue Mojadad Bazi Chand Sec Bashad?! Pishnahad Ma (2) >>> ")
tim = int(tim)
print(Gl.RESET_ALL)

g = """ID Channel Rubika: @Gx_Script
ID Creator: @Nanymous
ID Admins Channel: @Gx_Arnold, @GeNeRa1"""



while True:
    alamat = ["Sang", "Kaghaz", "Gheichi"]

    sys = _GeNeRal_.choice(alamat)
    print(gl.LIGHTMAGENTA_EX)
    for i in g:
        gx.stdout.write(i)
        gx.stdout.flush()
        MaMaD.sleep(0.01)
    print(Gl.RESET_ALL)
    print(gl.GREEN)

    player = input(" S, K, G, Help >>> ")

    print(Gl.RESET_ALL)
    
    if player.lower() == "exit":
        print(gl.YELLOW)
        print("Thanks For Use Me!")
        print(Gl.RESET_ALL)
        quit()
    if player.lower() == "s":
        player = "sang"
    elif player.lower() == "k":
        player = "kaghaz"
    elif player.lower() == "g":
        player = "gheichi"

    #print()
    print(gl.YELLOW + player)
    print()
    print(gl.CYAN + sys)
    print(Gl.RESET_ALL)
    if player.lower() == "help":
        print(gl.LIGHTMAGENTA_EX)
        print("In Bazi Bazie Sang Kaghaz Gheichi Ast! Bejaye Neveshtan Tamam Kalamat Anha Mitavanid Az Harf Aval Anha Niz Estefade Konid! Baray Khoroog (Exit)")
        print(Gl.RESET_ALL)

    color = gl.GREEN
    reset = Gl.RESET_ALL
    colorr = gl.RED

    if player.lower() == "kaghaz" and sys.lower() == "sang":
        print(color + "You Are Win!")
    elif player.lower() == "sang" and sys.lower() == "kaghaz":
        print(colorr +"You Are Failed!")
    if player.lower() == "sang" and sys.lower() == "gheichi":
        print(color + "You Are Win!")
    elif player.lower() == "gheichi" and sys.lower() == "sang":
        print(colorr + "You Are Failed")
    if player.lower() == "gheichi" and sys.lower() == "kaghaz":
        print(color + "You Are Win")
    elif player.lower() == "kaghaz" and sys.lower() == "gheichi":
        print(colorr + "You Are Failed")
    if player.lower() == "gheichi" and sys.lower() == "gheichi":
        print(color + "You = CPU")
    elif player.lower() == "kaghaz" and sys.lower() == "kaghaz":
        print(color + "You = CPU")
    elif player.lower() == "sang" and sys.lower() == "sang":
        print(color + "You = CPU")
    
    MaMaD.sleep(tim)
    Nanymous.system("clear" and "cls")
    #if player.lower() != "sang" or player.lower() != "s":
    #    print("Lotfan Az (Sang, Kaghaz, Gheichi) Va Ya (S, K, G) Estefade Konid!")
    #if player.lower() != "kaghaz" or player.lower() != "k":
    #    print("Lotfan Az (Sang, Kaghaz, Gheichi) Va Ya (S, K, G) Estefade Konid!")
    #if player.lower() != "gheichi" or player.lower() != "g":
    #    print("Lotfan Az (Sang, Kaghaz, Gheichi) Va Ya (S, K, G) Estefade Konid!")
    