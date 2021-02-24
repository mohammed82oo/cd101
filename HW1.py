X=input("write how much are the composers: ")
name=[]
family=[]
ages=[]
n=int (X)
for x in range(n):
    N=input('write name:')
    name.append(N)
    F=input("write family: ")
    family.append(F)
    B=input('write year of birth')
    D=input('write year of deth')
    ages.append(int(D)-int(B))
t=0
for x in range(n):
    t=t+ages[x]
m=t/n
for x in range(n):
    print(f"the name: {name[x]}, the family: {family[x]}, the age: {ages[x]}")
print(m)