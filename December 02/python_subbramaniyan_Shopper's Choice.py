#declearing the Variables and Arrays
a=[]
r=[]
l=[]
b=[]
t=0
count=0

#getting input form the user
v=int(input("Enter The Total Number of Item Sold"))
for s in range(0,v):
    t=int(input("Enter the product code"))
    a.append(t)
print(a)

#Arranging the elements in order using sort()
a.sort()

#Removing duplicates using dict.fromkeys()
l=list(dict.fromkeys(a))

#calculating the frequency of the element in array
for s in range(0,len(l)):
    count=0
    for j in range(0,v):
        if(l[s]==a[j]):
            count+=1
    r.append(count)
    
#displaying the output
print(r)
             
            
    
    
