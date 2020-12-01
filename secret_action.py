# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:04:45 2020

@author: Linter
"""
from art import logo
print(logo)
action_dict = {}
while True:
    name = input("what's your name: " )
    bid = float(input("what's your bid: " ))
    ask_more = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    action_dict[name] = bid
    print(action_dict)
    
    if ask_more == "yes":
        continue
    elif ask_more == "no":
        max_bid = 0 
        for key in action_dict:
            if max_bid < action_dict[key]:
                max_bid = action_dict[key]
        winner_index = list(action_dict.values()).index(max_bid)
        winner = list(action_dict.keys())[winner_index]
        print(f"The winner is {winner} ,bid is {max_bid}")
        break