# def length_of_string(string_1):
# 	print(len(string_1))

# string_1="jesso"
# length_of_string(string_1)



def check_pallindrone(word):

	if(word==word[::-1]):
		print("pallindrone")
	else:
		print("not pallindrone")
word="malayalam"
check_pallindrone(word)
