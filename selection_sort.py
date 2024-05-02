unsorted_list=[]
n=int(input ("Enter no. of elements :- "))
for i in range(0, n):
    ele = int(input('Element {} -> '.format(i+1)))
    unsorted_list.append(ele)

print("Entered Unsorted List is - ")
print(unsorted_list)

for i in range (len(unsorted_list)):
    min_idx=i
    for j in range(i+1,len(unsorted_list)):
        if unsorted_list[min_idx]>unsorted_list[j]:
            min_idx=j
    
    unsorted_list[i],unsorted_list[min_idx]=unsorted_list[min_idx],unsorted_list[i]
    print(" ")
    for i in range(len(unsorted_list)):
        if i < len(unsorted_list) - 1:
            print(unsorted_list[i],end=",")
        else:
            print(unsorted_list[i])

        
print("Here we have the sorted list")