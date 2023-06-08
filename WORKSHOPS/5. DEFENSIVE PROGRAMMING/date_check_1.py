    
user_date = input("Please enter your birth date: \n") # 05-06-1995

if len(user_date) == 10 and user_date[2] == user_date[5] == "-"\
    and user_date.replace("-", "").isnumeric():
    print(f"Your birthday is on {user_date}!")  
else:
    print("Date not correctly entered!")
    