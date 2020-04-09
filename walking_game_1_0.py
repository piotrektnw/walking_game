import random

number = random.randrange(0, 20)

hint = {
    "to go into room_1 type: ": "room1",
    "to go into room_2 type: ": "room2",
    "to go into room_3 type:": "room3",
    "to proceed forward type:": "forward",
    "to proceed left type:": "left",
    "to proceed right type:": "right",
    "to move back type:": "back",
    "to quit type: ": "quit"
}

list_of_rooms = ["you are in room1", "you are in room2", "you are in room3"]
print("""
    Welcome to the adventure game. Your goal is to find a treasure which is hidden in one of the three rooms in the castle.
    In order to open the treasure you need to guess the number. You have five tries to open it. 
    Beware the walls - if you hit them you will loose 3 moves. To complete whole goal you have 50 moves. 
     """)

start = input("Are you ready? Let's start with some hints. Please type: hint\n"
              "> ")

if start.lower() == "hint":
    for x, y in hint.items():
        print(x, y)

counter1 = 0
counter_l = 0
counter_f = 0
counter_task = 0
task = False

dir = ("What direction do you choose?")

while counter1 < 50:
    if task:
        break
    choose_room = input("Ok then. Please choose room. Where to go?")

    if choose_room.lower() == "room1":
        print(list_of_rooms[0])

        while counter_l < 4 or counter_f < 4:
            dir1 = input(dir)
            if dir1.lower() == hint["to proceed left type:"]:
                print("You have moved " + hint["to proceed left type:"])
                counter_l += 1
                if counter_l == 3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to proceed right type:"]:
                print("You have moved " + hint["to proceed right type:"])
                counter_l -= 1
                if counter_l == -3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to proceed forward type:"]:
                print("You have moved " + hint["to proceed forward type:"])
                counter_f += 1
                if counter_f == 3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to move back type:"]:
                print("You have moved " + hint["to move back type:"])
                counter_f -= 1
                if counter_f == -3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to quit type: "]:
                counter_l -= counter_l
                counter_f -= counter_f
                break
            if counter_f == 4 or counter_f == -4 or counter_l == 4 or counter_l == -4:
                print("You have been warned. You have reached the wall. You loose 3 points and start from beginning.")
                counter1 += 3
                counter_l -= counter_l
                counter_f -= counter_f
                break

    if choose_room.lower() == "room2":
        print(list_of_rooms[1])
        while counter_l < 4 or counter_f < 4:
            dir1 = input(dir)
            if dir1.lower() == hint["to proceed left type:"]:
                print("You have moved " + hint["to proceed left type:"])
                counter_l += 1
                if counter_l == 3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to proceed right type:"]:
                print("You have moved " + hint["to proceed right type:"])
                counter_l -= 1
                if counter_l == -3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to proceed forward type:"]:
                print("You have moved " + hint["to proceed forward type:"])
                counter_f += 1
                if counter_f == 3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to move back type:"]:
                print("You have moved " + hint["to move back type:"])
                counter_f -= 1
                if counter_f == -3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to quit type: "]:
                counter_l -= counter_l
                counter_f -= counter_f
                break

            if counter_f == 2 and counter_l == 1:
                treasure_task = input("Congratulations. You have found the treasure. Do you wanna play a game? y/n? \n"
                                      "> ")
                if treasure_task == "y":
                    print("Your task is to guess the number. You have five chances and with each try you will receive "
                          "hint. Please choose number between 0 - 20")
                    while counter_task < 5:
                        treasure_try = input("Guess the number: ")
                        try:  
                            if int(treasure_try) < number:
                                print("The number is too low. Try again: ")
                                counter_task += 1
                            elif int(treasure_try) == number:
                                print("Congratulations! You win!")
                                task = True
                                break
                            elif int(treasure_try) > number:
                                print("The number is too high. Try again: ")
                                counter_task += 1
                        except:
                            print("Please use only numbers.")
                        if counter_task == 4:
                            print("Last chance or you will loose: ")
                        if counter_task == 5:
                            print("You loose!")
                            counter_task -= counter_task
                            task = True
                            break
                elif treasure_task == "n":
                    print("Coward!")
                    task = True
                    break
            if task:
                break

            if counter_f == 4 or counter_f == -4 or counter_l == 4 or counter_l == -4:
                print("You have been warned. You have reached the wall. You loose 3 points and start from beginning.")
                counter1 += 3
                counter_l -= counter_l
                counter_f -= counter_f
                break

    if choose_room.lower() == "room3":
        print(list_of_rooms[2])

        while counter_l < 4 or counter_f < 4:
            dir1 = input(dir)
            if dir1.lower() == hint["to proceed left type:"]:
                print("You have moved " + hint["to proceed left type:"])
                counter_l += 1
                if counter_l == 3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to proceed right type:"]:
                print("You have moved " + hint["to proceed right type:"])
                counter_l -= 1
                if counter_l == -3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to proceed forward type:"]:
                print("You have moved " + hint["to proceed forward type:"])
                counter_f += 1
                if counter_f == 3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to move back type:"]:
                print("You have moved " + hint["to move back type:"])
                counter_f -= 1
                if counter_f == -3:
                    print("One more movement in this direction and you will loose three points. Change direction.")
            elif dir1.lower() == hint["to quit type: "]:
                counter_l -= counter_l
                counter_f -= counter_f
                break
            if counter_f == 4 or counter_f == -4 or counter_l == 4 or counter_l == -4:
                print("You have been warned. You have reached the wall. You loose 3 points and start from beginning.")
                counter1 += 3
                counter_l -= counter_l
                counter_f -= counter_f
                break
if task:
    print("End of game")

    counter1 += 1
