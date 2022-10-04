# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_count = lower_name1.count("t") + lower_name2.count("t") 
r_count = lower_name1.count("r") + lower_name2.count("r") 
u_count = lower_name1.count("u") + lower_name2.count("u") 
e_count = lower_name1.count("e") + lower_name2.count("e")

true_total_count = t_count + r_count + u_count + e_count

l_count = lower_name1.count("l") + lower_name2.count("l") 
o_count = lower_name1.count("o") + lower_name2.count("o") 
v_count = lower_name1.count("v") + lower_name2.count("v")

love_total_count = l_count + o_count + v_count + e_count

total_score = str(true_total_count) + str(love_total_count)

if((int(total_score) < 10) or (int(total_score) > 90)):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif((int(total_score) > 40) and (int(total_score) < 50)):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
    