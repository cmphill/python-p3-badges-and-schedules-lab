def badge_maker(name):
    badge = (f"Hello, my name is {name}.")
    return badge

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    i = 0
    assignment = []
    for room in range(1,9):
        assignment.append((f"Hello, {names[i]}! You'll be assigned to room {room}!"))
        i+=1
    return assignment
            

    

def printer(names):
    for badge in batch_badge_creator(names):
       print(badge)
    for assignment in assign_rooms(names):
        print(assignment)

