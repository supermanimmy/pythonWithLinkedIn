"""
Example file working with date information.
"""
from datetime import date 
from datetime import time
from datetime import datetime

def main():
    # Date objects
    # Get today's date from the today() function from the date  class.
    today = date.today()
    print("Today's date is ", today)

    # Print out the data's individual components
    print ("Date componnents: ", today.day, today.month, today.year )

    # Retrieve today's weekday (0 = Monday, 6 = Sunday).
    print ("Today's weekday # is: ", today.weekday())

    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print ("Which is a:", days[today.weekday()])

    #Datetime objects

    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today)

if __name__ == '__main__':
    main()