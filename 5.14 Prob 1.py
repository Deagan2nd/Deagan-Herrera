#-------------------------------------------------------------------------------
# Name:        5.14 prob 1
# Purpose:
#
# Author:      drherrera
#
# Created:     23/09/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
day = input("What's the day? (Enter a number 0-6): ")
if day == "0":
    print("Sunday")
elif day == "1":
    print("Monday")
elif day == "2":
    print("Tuesday")
elif day == "3":
    print("Wednesday")
elif day == "4":
    print("Thursday")
elif day == "5":
    print("Friday")
elif day == "6":
    print("Saturday")
else:
    print("Invalid choice.")