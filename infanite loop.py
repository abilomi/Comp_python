asking = True

while asking:
    print("choices:\nl. Apple\n2. Orange\n3. Banana")
    choice = int(input("please choose a fruit (1, 2, or 3):"))
    print(f"you chose choice #{choice}")

    if choice == 1 or choice == 2 or choice == 3:
        asking = False
    else:
        print("please only type in 1,2,or 3;)")
    print("Thank you for making  a valid choice!")
