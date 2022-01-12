#############################
# Three's a crowd: pt. 1 / pt. 2 

people = ['Matt', 'Mark', 'Luke', 'Ringo']

def test_crowd(people):
    if len(people) > 3:
        print("This room's crowded!")
    else:
        print("Room's all good.")

test_crowd(people)

people.pop()

test_crowd(people)

#############################
# Six is a Mob

people = ['Matt', 'Mark', 'Luke', 'Ringo', 'Daphne', 'Lilly']

def test_mob(people):
    if len(people) > 5:
        print("There's a MOB in this room!")
    elif len(people) >= 3:
        print("This room's crowded!")
    elif len(people) > 0:
        print("Room's all good.")
    else:
        print("Room's empty")

test_mob(people)
test_mob(people[0:3])
test_mob(people[0:1])   