hint = ("""
    room1 - to go in room1
    room2 - to go in room2
    room3 - to go in room3
    forward - to go forward
    left - to go left
    right - to go right
    quit - to quit room
""")
list_of_rooms = ["you are in room1", "you are in room2", "you are in room3"]
start = input("Welcome to the adventure game. There are three rooms to go in. To get hints say: hint")

if start.lower() == "hint":
    print(hint)
else:
    pass

limit_reached = False
counter1 = 0
counter_l = 0
counter_r = 0
counterl1 = 0
counterr1 = 0
counterl2 = 0
counterr2 = 0

dir = ("What direction do you choose?")

while counter1 < 99:
    choose_room = input("Ok then. Please choose room. Where to go?")

    if choose_room.lower() == "room1":
        print(list_of_rooms[0])
        while counter_l < 3:
            dir1 = input(dir)
            if dir1.lower() == "left":
                print("You have moved left")
                counter_l += 1
            elif dir1.lower() == "right":
                print("You have moved right")
                counter_l -= 1
            elif dir1.lower() == "quit":
                counter_l -= counter_l
                break
            if counter_l == 3:
                left_limit = input("Left limit. Change room or direction. ")
                if left_limit.lower() == "left":
                    print("You have reached the wall. You are going to choose room again. ")
                    counter_l -= counter_l
                    break
                elif left_limit.lower() == "right":
                    counter_l += -1
                    print("You have moved one step away from the left side.")
                elif left_limit.lower() == "quit":
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You are leaving the room")
                    break
            if counter_l == - 3:
                right_limit = input("Right limit. Change room or direction")
                if right_limit.lower() == "right":
                    counter_l -= counter_l
                    print("You have reached the wall. You are going to choose room again. ")
                    break
                elif right_limit.lower() == "left":
                    counter_l += 1
                    print("You have moved one step away from the right side.")
                elif right_limit.lower() == "quit":
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You are leaving the room")
                    break


    if choose_room.lower() == "room2":
        print(list_of_rooms[1])
        while counter_l < 3:
            dir1 = input(dir)
            if dir1.lower() == "left":
                print("You have moved left")
                counter_l += 1
            elif dir1.lower() == "right":
                print("You have moved right")
                counter_l -= 1
            elif dir1.lower() == "quit":
                counter_l -= counter_l
                break
            if counter_l == 3:
                left_limit = input("Left limit. Change room or direction. ")
                if left_limit.lower() == "left":
                    print("You have reached the wall. You are going to choose room again. ")
                    counter_l -= counter_l
                    break
                elif left_limit.lower() == "right":
                    counter_l += -1
                    print("You have moved one step away from the left side.")
                elif left_limit.lower() == "quit":
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You are leaving the room")
                    break
            if counter_l == - 3:
                right_limit = input("Right limit. Change room or direction")
                if right_limit.lower() == "right":
                    counter_l -= counter_l
                    print("You have reached the wall. You are going to choose room again. ")
                    break
                elif right_limit.lower() == "left":
                    counter_l += 1
                    print("You have moved one step away from the right side.")
                elif right_limit.lower() == "quit":
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You are leaving the room")
                    break

    if choose_room.lower() == "room3":
        print(list_of_rooms[2])
        while counter_l < 3:
            dir1 = input(dir)
            if dir1.lower() == "left":
                print("You have moved left")
                counter_l += 1
            elif dir1.lower() == "right":
                print("You have moved right")
                counter_l -= 1
            elif dir1.lower() == "quit":
                counter_l -= counter_l
                break
            if counter_l == 3:
                left_limit = input("Left limit. Change room or direction. ")
                if left_limit.lower() == "left":
                    print("You have reached the wall. You are going to choose room again. ")
                    counter_l -= counter_l
                    break
                elif left_limit.lower() == "right":
                    counter_l += -1
                    print("You have moved one step away from the left side.")
                elif left_limit.lower() == "quit":
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You are leaving the room")
                    break
            if counter_l == - 3:
                right_limit = input("Right limit. Change room or direction")
                if right_limit.lower() == "right":
                    counter_l -= counter_l
                    print("You have reached the wall. You are going to choose room again. ")
                    break
                elif right_limit.lower() == "left":
                    counter_l += 1
                    print("You have moved one step away from the right side.")
                elif right_limit.lower() == "quit":
                    counter_l -= counter_l
                    break
                else:
                    counter_l -= counter_l
                    print("Wrong command. You are leaving the room")
                    break

    counter1 += 1




