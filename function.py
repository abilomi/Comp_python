''' 
A program to demo what functions can do. 
'''
#we start with a function "defination"

def add_3(a,b,c):#1st line is called a header a,b,c being parameters
	return a+b+c 
	
print("=============================")	
#print(add(3,7))
#print(add(3.5,7.25)) #give your function good name.
#we then "call" (use) our function 
#and "pass" it "parameters"
print(add_3(3.5,7.25,2))
print(add_3("polar ","bear ","baby "))