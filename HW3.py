def writing (x):
    name=[]
    family=[]
    ages=[]
    while True:
        N=input('write name:')
        name.append(N)
        F=input("write family: ")
        family.append(F)
        B=input('write year of birth')
        D=input('write year of deth')
        ages.append(int(D)-int(B))
        print("do you want to stop? S for stop, C for complete")
        answer=input()
        if answer=="c":
            continue
        else:
            break
    return(name,family,ages)

j=1
Name , Family , Ages = writing (j)
t=0
for x in range(len(Ages)):
    t=t+Ages[x]
m=t/len(Ages)
for u in range(len(Name)):
    print(f"the name: {Name[u]}, the family: {Family[u]}, the age: {Ages[u]}")
print(m)