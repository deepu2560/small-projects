# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
isValid = False
price = 0

if(size == "S"):
    price+=15
    isValid = True
elif(size == "M"):
    price+=20
    isValid = True
elif(size == "L"):
    price+=25
    isValid = True
else:
    print("Please choose a valid pizza size (S, M, or L)")

if(add_pepperoni == "Y"):
    if(size == "S"):
        price+=2
    else:
        price+=3

if(extra_cheese == "Y"):
    price+=1

if(isValid == True):
    print(f"Your final bill is: ${price}.")