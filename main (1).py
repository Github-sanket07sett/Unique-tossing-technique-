import random
user_win=0
comp_win=0
list=[1,2,3,4,5]
list1=[0,1]
while True:
    sum=0
    random_n=random.choice(list1)
    user_pick=int(list1[random_n])
    print("user picked:",user_pick)
    user_input=int(input("Type any number:-"))

    if(user_input==-1):
        print("the game is end")
        break
    random_num=random.choice(list)
    comp_pick=int(list[random_num])
    print("computer picked:",comp_pick)
    sum=(user_input+comp_pick)
    if sum % 2 == 0:
        if user_pick==1:
            print("user win")
            user_win+=1
        else:
            print("user loose")
            comp_win+=1
    else :
        if user_pick==0:
            print("user jitbe")
            user_win+=1
        else:
            print("comp jitbe")
            comp_win+=1
    print("user wins", user_win,"times")   
    print("comp wins", comp_win,"times")
