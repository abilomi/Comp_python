Countries = ["USA", "Ethiopia", "Canada", "France", "Mexico","Mexico", "Canada","France"]
print(Countries[4])#print only the 5th item 
for f in Countries: #print the entire list 
	print(f)
print(Countries)#Case sensitive 
sum = 0
for f in Countries:
	if f == "France":#don't forget to put sting in double quotation
		print("found") 
		sum = sum+1
print("France:", sum)
