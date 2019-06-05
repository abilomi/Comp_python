filename = Aby\my_name_is.txt"
import time
import sys

day = "Today"
day_of_week = "Tuesday"
day_of_month = 28
month = "May"
month_num = 5
birthday_month_num = 8
year = 2019
is_rainy = True
location = "Rockville"
is_am = False

print("")


def cal_month_diffrence(current_month, bithday_month):
    diff = bithday_month - current_month
    if diff < 0:
        return diff + 12
    else:
        return diff

words =  f"\n{day} is {day_of_week}, {month} {day_of_month},{year}. It is {cal_month_diffrence(month_num,birthday_month_num)} months until my birthday."
 
for char in words:
  time.sleep(0.05) #
  sys.stdout.write(char)
  sys.stdout.flush()

  time.sleep(1)

if (not is_rainy or is_am):
    print("please bring unbrilla;)")
