print("Welcome to rollercoaster ride")
height = int(input("What is your height ?\n"))

if(height>=120):
  print("You can ride rollercoaster.")
  age = int(input("What is you age ?\n"))
  if(age < 12):
    print("Please pay $5.")
  elif(age<=18):
    print("Please pay $7.")
  elif (age > 45 and age < 55):
    print("You can ride free of cost")
  else:
    print("Please pay $12.")
else:
  print("Sorry! You have to grow more to ride rollercoaster.")