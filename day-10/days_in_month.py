def is_leap(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month > 12 and month < 1:
    return "Invalid month Entered!"
  elif month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












