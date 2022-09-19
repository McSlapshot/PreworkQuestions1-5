# Question 1
def hello_name(user_name):
    #""print a greeting to the username"""
    print(f"Hello {user_name}")
hello_name('Sia_McQ')

# Question 2
def first_odds():
    #""this will print all odd numbers from 1 - 100, but return nothing or none""
    for num in range(1,101):
        if num % 2 == 1:
            print(num)
first_odds


#Question 3
def max_num_in_list(a_list1):
    x = a_list1 [0]
    for A_max in a_list1:
        if A_max > x:
            x = A_max
    return x
a_list1 = [1, -2, 8, 15, 29]
max_in_list = max_num_in_list(a_list1)
print(max_in_list)

#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
a_year = 300
if is_leap_year(a_year):
    print(str(a_year) + " is a leap year!")
else:
    print(str(a_year) + " is not a leap year.")
    
#Question 5
def is_consecutive(a_list):  
    consectutive_list = list(range(min(a_list), max(a_list)+1))
    if a_list == consectutive_list:
        return True
    else:
        return False
a_list = [1,1,2,3,4,5,6] 
if is_consecutive(a_list):
    print(str(a_list)+ ' is consecutive')
else:
    print(str(a_list)+ ' is not consecutive')