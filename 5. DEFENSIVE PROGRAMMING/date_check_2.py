def validate_date(date):
    if check_length(date) and \
       check_numbers(date.replace("-", "")) and \
       check_symbols(date):
        return True
    return False
    
def check_numbers(date):
    if date.isnumeric():
        return True
    return False
    
def check_length(date):
    if len(date) == 10:
        return True
    return False

def check_symbols(date):
    if date[2] == date[5] == "-":
        return True
    return False
 
user_date = input("Please enter your birth date: \n")

if validate_date(user_date):
    print(f"Your birthday is on {user_date}!")  # 05-06-1995
else:
    print("Date not correctly entered!")

