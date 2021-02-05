'''#'jan','cream','phu','bam','aom','pee','bas','kong','da','james'
friend = ['jan','cream','phu','bam','aom','pee','bas','kong','da','james'] #นับตำเเหน่งเป็น 0,1,2,3,4,5,6,7,8,9
friend[9]="may" 
friend[3]="boat"
print(friend[3:8])
print(friend[-3]) #นับจากข้างหลัง '''

'''friend = ["Jan","Cream","Phu","Bam","Aom","Pee","Bas","Kong","Da","James"]
#friend[9] = "May"
#friend[3] = "Boat"
friend.append("Dome")
friend.append("Poondang")
friend.insert(1,"Z-Sa")
friend.insert(8,"Ped")
friend.remove("Aom")
friend.pop()
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)'''

animal={"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","cabibara","spider","wombat","penguin","crocodile"])
print(animal)