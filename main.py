import random
import pandas as pd

def roll_dise():
    roll_no = random.randint(1,6)
    return roll_no

def player(dice_roll, pos_his, win_status, final_roll):
    roll = roll_dise()
    if sum(dice_roll) + roll > size:
        pos_his.append(sum(dice_roll))
        final_roll.append(roll)
    elif sum(dice_roll) + roll == size:
        pos_his.append(size)
        final_roll.append(roll)
        win_status = 1
    elif sum(dice_roll) + roll < size:
        pos_his.append(sum(dice_roll) + roll)
        final_roll.append(roll)
        dice_roll.append(roll)
    return dice_roll, pos_his, win_status, final_roll
    


grid = int(input("Enter the Grid is size: "))

size = grid*grid

p1 = {}
dice_roll_1 = []
final_roll_1 = []
pos_his_1 = []
win_status_1 = 0

p2 = {}
dice_roll_2 = []
final_roll_2 = []
pos_his_2 = []
win_status_2 = 0

p3 = {}
dice_roll_3 = []
final_roll_3 = []
pos_his_3 = []
win_status_3 = 0

p4 = {}
dice_roll_4 = []
final_roll_4 = []
pos_his_4 = []
win_status_4 = 0


while True:
    dice_roll_1, pos_his_1, win_status_1, final_roll_1 = player(dice_roll_1, pos_his_1, win_status_1, final_roll_1)
    if win_status_1==1:
        break
    dice_roll_2, pos_his_2, win_status_2, final_roll_2 = player( dice_roll_2, pos_his_2, win_status_2, final_roll_2)
    if win_status_2==1:
        break
    dice_roll_3, pos_his_3, win_status_3, final_roll_3 = player(dice_roll_3, pos_his_3, win_status_3, final_roll_3)
    if win_status_3==1:
        break
    dice_roll_4, pos_his_4, win_status_4, final_roll_4 = player( dice_roll_4, pos_his_4, win_status_4, final_roll_4)
    if win_status_4==1:
        break
    
    
    
    
p1["final_roll"] = final_roll_1
p1["pos_his"] = pos_his_1
p1["win_status"] = win_status_1

p2["final_roll"] = final_roll_2
p2["pos_his"] = pos_his_2
p2["win_status"] = win_status_2

p3["final_roll"] = final_roll_3
p3["pos_his"] = pos_his_3
p3["win_status"] = win_status_3

p4["final_roll"] = final_roll_4
p4["pos_his"] = pos_his_4
p4["win_status"] = win_status_4

print(p1)
print(p2)
print(p3)
print(p4)
# p1 = {'final_roll': [2, 6], 'pos_his': [2, 8], 'win_status': 0}
# p2 = {'final_roll': [6, 2], 'pos_his': [6, 8], 'win_status': 0}
# p4 = {'final_roll': [5, 4], 'pos_his': [5, 9], 'win_status': 1}
# p3 = {'final_roll': [3], 'pos_his': [3], 'win_status': 0}

# df = pd.DataFrame({"p1": p1,"p2" : p2,"p3":p3,"p4":p4})
# output =
# print(output)
