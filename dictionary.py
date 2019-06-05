#dictionary example keys onthe left 
#values on the right side Key value pairs
addresses = {
	"Hiwi":"Shantly",
	"Sam":"Potomac",
	"Ermi":"Silver Spring",
	"Maki":"Beltsvill"
}
print(addresses)

for k in addresses.keys():
  print(k,"is in",addresses.get(k),end=".\n")
'''key's are the once 
in the left side and they are unique'''
#for v in addresses.values():
#	print(v)

  #print(k,"is in",addresses.get(k),".")
