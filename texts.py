name = "Abi"
day = "Thurday, May 30th"
message1 = f"My name is {name} and today is {day}."
message2 = "This is the 2nd line."
message3 = "This is the 3rd and final line."
messages =[message1, message2, message3]

filename = "Aby\poeml.txt"
file = open(filename, "w")
file.writelines(messages)
file.close()
with open(filename, 'w') as f:
    for m in messages:
        f.write(f"{m}\n")
