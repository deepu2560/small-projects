print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

start_way = input("Which way you want to go left or right ?").lower()

if (start_way == "left"):
    swim_wait = input(
        "You reached at a lake. what do you want to do swim or wait?").lower()
    if (swim_wait == "wait"):
        door_choose = input(
            "You reached last step. In front of you there are 3 doors. Which one you will pick yellow, red or blue?").lower()
        if (door_choose == "yellow"):
            print("HOORAY you found the treasure.")
        elif (door_choose == "red"):
            print("GAME OVER. Behind this door there were tigers and you died")
        elif (door_choose == "blue"):
            print("GAME OVER. This rooms is filled of snakes and you died.")
        else:
            print("GAME OVER. You choose wrong path and fall in Canyon.")
    elif (swim_wait == "swim"):
        print("GAME OVER. You got eatten by shark")
    else:
        print("GAME OVER. You choose wrong path and fall in Canyon.")
else:
    print("GAME OVER. You fall in Canyon.")
