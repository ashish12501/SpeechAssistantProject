# print("hellow world")
# charecter_name = "Tom"
# charecter_age = "45"
# print("there was a man named " + charecter_name)
# print("his age was " + charecter_age)
# charecter_name = "Lucy"
# print(charecter_name + " was not good at coading")




# my_name = -6
# print(abs(my_name))




# num = 4
# print(pow(num,2))



# name = input("Enter your name")
# age = input("Enter your age")
# print("Hey "+ name + "you are "+ age +"years old!")

# color = input("enter a color ")
# plural_noun = input ( "enter a plural noun ")
# celebrity = input("enter a celebruty name ")

# print("roses are " + color)
# print(plural_noun +" are blue " )
# print("I love you " + celebrity)




# lucky_nums = [2, 54,63,64, 23,23]
# friends = ["Ashish", "Aman", "Astha","Aparna", "Aditya", "Chetan", "Satyam" ]
# # print(friends [0])
# # print(friends[3:])
# # print(friends[3:6])
# friends.extend(lucky_nums)
# print(friends)

# def max_num (num1, num2, num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3

# print(max_num(49,6,200))



# n = int(input(""))

# if int(n%2==0):
#     print("Even")







# is_male = False
# if is_male:
#     print ("You are a male")
# else:
#     print ("You are a female")









# word = "Vector Academy"
# guess = ""
# guess_count = 0
# count_limit = 3
# status = False
    
# while guess_count<count_limit and status == False:
#     guess = input("Enter your guess : ")
#     guess_count +=1
#     if guess == word:
#         print ("You won!")
#         status = True
#     elif guess_count< count_limit and status==False:
#         print("Try again...")

# if status== False:
#     print("You lost...!")




# n= int(input("enter a number "))
# if n%2 != 0:
#     print("Weird")

# else :
#     print (" Not weird")





# def is_leap(year):
#     leap = False
#     if year%4==0 or year%100 != 0 or year%400==0 :
#         leap = True
#         return leap
#     else:
#         return leap
    
    

# year = int(input())
# print(is_leap(year))



# print(10%2)
# print(3/2)



if __name__ == '__main__':
    n = int(input())
    print()
    i=1
for num in range (1,n+1):
    print(num,end="")