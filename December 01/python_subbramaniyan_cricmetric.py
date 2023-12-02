#variable and array declearation 
r=[]
a=0
total=0
highest=0
y=0

#getting the input form the user
v=int(input("Enter The Number of Playres"))
for s in range(0,v):
    print("Enter Player",s+1,"score")
    a=int(input())
    r.append(a)

#To check higest runs using max()function
highest=max(r)
for s in range(0,v):
    if highest == r[s]:
        y=s

#calculating the total runs
for s in range(0,v):
    total+=r[s]

#Displaying the output
print("Total Team Score",total)
print("Higest score (index value)",y)

    


