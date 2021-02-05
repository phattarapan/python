print("-"*30)
student_list = int(input("Please enter student : "))
print("-"*30)
a = 1
total_list =  [0 ,0 ,0 ,0 ,0 ,0]
score_list = ["90-100 :","80-89 :","70-79 :","60-69 :","50-59 :","0-49 :"]
for x in range(0,student_list) :
    i = int(input("Please enter score" + str(a) + " : "))
    a += 1
    if i <= 100 and i >= 90 :
        total_list [0] += 1
    elif i <= 90 and i >= 80 :
        total_list [1] += 1
    elif i <= 80 and i >= 70 :
        total_list [2] += 1
    elif i <= 70 and i >= 60 :
        total_list [3] += 1
    elif i <= 60 and i >= 50 :
        total_list [4] += 1
    elif i <= 50 and i >= 0 :
        total_list [5] += 1
for x in range(0,6) :
    print(score_list [x],"*"*total_list [x])