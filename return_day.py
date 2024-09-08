# Write a function called return_day. this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None

# Hint: store the days of the week in a list (or dict using numbers as keys).
 

def return_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        return days[num-1]
    return None


# Here's a more advanced solution that involves error handling, which we have not covered yet.  It eliminates the need to check to see if num is a valid index in the list. We cover this in the debugging section, but I thought you may want to see if now.

# def return_day(num):
#     try:
#         return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
#     except IndexError as e:
#         return None