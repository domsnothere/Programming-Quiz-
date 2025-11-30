print("Do you want to add or subtract? a/s")
choice = input()
first_number = input ("Pick your First Number")
second_number = input ("Pick your Second Number")
int_first_number = int(first_number)
int_second_number = int(second_number)
if choice == "a":
    solution = (int_first_number + int_second_number)
    print ("The solution to the addition problem is: ",solution)
else:
    solution = (int_first_number - int_second_number)
    print ("The solution to the subtraction problem is:",solution) 
