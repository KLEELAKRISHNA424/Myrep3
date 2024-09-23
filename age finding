from datetime import datetime  

def calculate_age(birth_date):  
    today = datetime.now()  
    age = today.year - birth_date.year  
    # Check if the birthday has not occurred yet this year  
    if (today.month, today.day) < (birth_date.month, birth_date.day):  
        age -= 1  
    return age  

# Input the birth date  
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")  

try:  
    # Parse the input string into a date object  
    birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")  
    age = calculate_age(birth_date)  
    print(f"You are {age} years old.")  
except ValueError:  
    print("Invalid date format. Please use YYYY-MM-DD.")
