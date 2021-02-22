# def print_character(x,y):
# 	for i in range(y):
# 		for j in range(i+1):
# 			print(x,end="")
# 		print("\n")

# character=input("enter the character ")
# number=int(input("enter the number "))
# print_character(character,number)
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print(myList)

n = 5
pypart(n)