# Great Python program to display the calendar of the month


import sys
import calendar

viewCalendar = lambda yy, mm:print("\n\n Calendar > \n %s\n" % calendar.month(yy, mm))

while True:
        if str(input("[+] Star [Y/N] ? ")).strip().lower() == "y":
                try:
                      viewCalendar(int(input("\nYear: ")), int(input("Month: ")))
                except IndexError:
                        print("   -> Try Again! with vaild numbers!\n")
        else:
                print("\nSee Ya Soon! :D ")
                sys.exit(0)                       


