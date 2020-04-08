hint = {
    "to go into room_1": "room1",
    "to go into room_2": "room2",
    "to go into room_3": "room3",
    "to proceed forward": "forward",
    "to proceed left": "left",
    "to proceed right": "right",
    "to quit": "quit"
}

list_of_rooms = ["you are in room1", "you are in room2", "you are in room3"]
start = input("Welcome to the adventure game. There are three rooms to go in. To get hints say: hint")

if start.lower() == "hint":
    print(hint.items())
else:
    pass

counter1 = 0
counter_l = 0
counter_r = 0

dir = ("What direction do you choose?")

while counter1 < 99:
    choose_room = input("Ok then. Please choose room. Where to go?")

    if choose_room.lower() == "room1":
        print(list_of_rooms[0])

        while counter_l < 3:
            dir1 = input(dir)
            if dir1.lower() == hint["to proceed left"]:
                print("You have moved " + hint["to proceed left"])
                counter_l += 1
            elif dir1.lower() == hint["to proceed right"]:
                print("You have moved " + hint["to proceed right"])
                counter_l -= 1
            elif dir1.lower() == hint["to quit"]:
                counter_l -= counter_l
                break

            if counter_l == 3:
                left_limit = input(hint["to proceed left"] + " limit. Change room or direction. ")
                if left_limit.lower() == hint["to proceed left"]:
                    print("You have reached the wall. You are going to choose room again. ")
                    counter_l -= counter_l
                    break
                elif left_limit.lower() == hint["to proceed right"]:
                    counter_l += -1
                    print("You have moved one step away from the " + hint["to proceed left"] + " side.")
                elif left_limit.lower() == hint["to quit"]:
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    counter1 += 3
                    print("Wrong command. You loose 3 moves. You are leaving the room")
                    break

            if counter_l == - 3:
                right_limit = input(hint["to proceed right"] + " limit. Change room or direction")
                if right_limit.lower() == hint["to proceed right"]:
                    counter_l -= counter_l
                    print("You have reached the wall. You are going to choose room again. ")
                    break
                elif right_limit.lower() == hint["to proceed left"]:
                    counter_l += 1
                    print("You have moved one step away from the " + hint["to proceed right"] + " side.")
                elif right_limit.lower() == hint["to quit"]:
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You loose 3 moves. You are leaving the room")
                    counter1 += 3
                    break


    if choose_room.lower() == "room2":
        print(list_of_rooms[1])

        while counter_l < 3:
            dir1 = input(dir)
            if dir1.lower() == hint["to proceed left"]:
                print("You have moved " + hint["to proceed left"])
                counter_l += 1
            elif dir1.lower() == hint["to proceed right"]:
                print("You have moved " + hint["to proceed right"])
                counter_l -= 1
            elif dir1.lower() == hint["to quit"]:
                counter_l -= counter_l
                break

            if counter_l == 3:
                left_limit = input(hint["to proceed left"] + " limit. Change room or direction. ")
                if left_limit.lower() == hint["to proceed left"]:
                    print("You have reached the wall. You are going to choose room again. ")
                    counter_l -= counter_l
                    break
                elif left_limit.lower() == hint["to proceed right"]:
                    counter_l += -1
                    print("You have moved one step away from the " + hint["to proceed left"] + " side.")
                elif left_limit.lower() == hint["to quit"]:
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    counter1 += 3
                    print("Wrong command. You loose 3 moves. You are leaving the room")
                    break

            if counter_l == - 3:
                right_limit = input(hint["to proceed right"] + " limit. Change room or direction")
                if right_limit.lower() == hint["to proceed right"]:
                    counter_l -= counter_l
                    print("You have reached the wall. You are going to choose room again. ")
                    break
                elif right_limit.lower() == hint["to proceed left"]:
                    counter_l += 1
                    print("You have moved one step away from the " + hint["to proceed right"] + " side.")
                elif right_limit.lower() == hint["to quit"]:
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    counter1 += 3
                    print("Wrong command. You loose 3 moves. You are leaving the room")
                    break

    if choose_room.lower() == "room3":
        print(list_of_rooms[2])

        while counter_l < 3:
            dir1 = input(dir)
            if dir1.lower() == hint["to proceed left"]:
                print("You have moved " + hint["to proceed left"])
                counter_l += 1
            elif dir1.lower() == hint["to proceed right"]:
                print("You have moved " + hint["to proceed right"])
                counter_l -= 1
            elif dir1.lower() == hint["to quit"]:
                counter_l -= counter_l
                break

            if counter_l == 3:
                left_limit = input(hint["to proceed left"] + " limit. Change room or direction. ")
                if left_limit.lower() == hint["to proceed left"]:
                    print("You have reached the wall. You are going to choose room again. ")
                    counter_l -= counter_l
                    break
                elif left_limit.lower() == hint["to proceed right"]:
                    counter_l += -1
                    print("You have moved one step away from the " + hint["to proceed left"] + " side.")
                elif left_limit.lower() == hint["to quit"]:
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    counter1 += 3
                    print("Wrong command. You loose 3 moves. You are leaving the room")
                    break

            if counter_l == - 3:
                right_limit = input(hint["to proceed right"] + " limit. Change room or direction")
                if right_limit.lower() == hint["to proceed right"]:
                    counter_l -= counter_l
                    print("You have reached the wall. You are going to choose room again. ")
                    break
                elif right_limit.lower() == hint["to proceed left"]:
                    counter_l += 1
                    print("You have moved one step away from the " + hint["to proceed right"] + " side.")
                elif right_limit.lower() == hint["to quit"]:
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    counter1 += 3
                    print("Wrong command. You loose 3 moves. You are leaving the room")
                    break

    counter1 += 1




