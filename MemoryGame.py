import random
from Utils import screen_cleaner as clear
from Utils import interval

def generate_sequance(difficulty):
    list_a = [random.randint(1,101) for i in range(difficulty)]
    print (list_a)
    #Dispaly numbers to player
    clear()
    print(list_a)
    for item in list_a:
        print(item)
        interval()
        clear()
    return list_a

def get_list_from_user(difficulty):
    print('After Seeing The NumbersEnter the Numbers you saw, each one separated with Enter.')
    b_list = []
    for item in range(difficulty):
        #hold temp value in a before insert to list
        a = input('Enter Your Number:')
        b_list.insert(item,int(a))
    #test input
    # for item in range(len(b_list)):
    #     print(b_list[item])
    return b_list

def is_list_equal(list_a,list_b):
    #align list to ignore insert order
    list_a.sort()
    list_b.sort()
    if list_a == list_b:
        print('True')
        return True
    else:
        print('False')
        return False

def play(difficulty):
    list_a = generate_sequance(difficulty)
    # print(list_a)
    list_b = get_list_from_user(difficulty)
    result = is_list_equal(list_a, list_b)
    return result

