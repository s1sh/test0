def year1(year):
    if  (year % 4) == 0 :
         if (year % 100) == 0:
            print("not a leap year")
         else :
            print("leap year")
    else :
        print("not a leap year")

a = int(input("enter year  "))

year1(a)


