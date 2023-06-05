names = ["Pieter", "John", "David", "Brandon"]

for i, name in enumerate(names, 1):
    print(f"{i}: {name}")
    
user_choice = input("Please pick a name from the list: \n")
while not user_choice.isnumeric():
    user_choice = input("Please pick a name from the list: \n")

user_choice = int(user_choice)-1

if 0 <= user_choice < len(names):
    print(f"You have picked {names[user_choice]}")
