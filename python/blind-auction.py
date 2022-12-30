logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

end_auction = False
user_data = []

print(logo)

while not end_auction:

    user_name = input("What is your name ?  ")
    user_bid = int(input("How much you want to bid ?  $"))

    user_dict = {"name": user_name, "bid": user_bid}

    user_data.append(user_dict)
    bidder_left = input("Do any other bidder left ?")
    if bidder_left == "no" or bidder_left != "yes":
        end_auction = True

max = {"name": "", "bid": 0}

for bid in user_data:
    if int(bid["bid"]) > max["bid"]:
        max["name"] = bid["name"]
        max["bid"] = bid["bid"]

print(f'This unique and antic product goes to {max["name"]} for ${max["bid"]}')
