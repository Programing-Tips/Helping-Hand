import datetime

#user_inp = input("Kedy ste sa narodili? (format: 25.5.2009)")

def count_days(bday):
    today = datetime.date.today()
    return today - bday

birthday = datetime.date(2003, 6, 11)
today = datetime.date.today()
print(today - birthday)