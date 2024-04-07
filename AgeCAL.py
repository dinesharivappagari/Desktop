from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    print("Welcome to the Age Calculator!")
    print("Please enter your birthdate (YYYY-MM-DD):")
    birthdate_str = input()
    
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
        age = calculate_age(birthdate)
        print("Your age is:", age)
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()