print("-"*20)
student_list = []
student_list = int(input("Please enter student : "))
print("-"*20)
score_list = ["90-100 :","80-89 :","70-79 :","60-69 :","50-59 :","0-49 :"]
for x in score_list :
    i = int(input("Please enter student : "+ x ))
    student_list.append(i)
for x in range(0,6) :
    print(score_list[x]+"*"*student_list[x])