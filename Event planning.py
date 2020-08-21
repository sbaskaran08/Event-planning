budget=list(map(int,input().split()))
hotel_Rent=[]
beds=[]
solution=0
for i in range(budget[2]):
    cost=int(input())
    hotel_Rent.append(cost)
    no_of_beds=list(map(int,input().split()))
    beds.append(no_of_beds)
for j in range(budget[2]):
    minimum=min(hotel_Rent)
    index1=hotel_Rent.index(minimum)
    count=0
    for k in beds[index1]:
        if(k>=budget[0]):
            solution=solution+(minimum*budget[0])
        count=count+1
        if(count==budget[3]):
            hotel_Rent.remove(minimum)
            beds.pop(index1)
            break
        if(solution!=0):
            break
    if(solution!=0):
        break
if(solution<=budget[1] and solution!=0):
    print(solution)
else:
    print('stay home')
