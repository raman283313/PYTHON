list=[12,34,21,42,53,33,54,79]
even_count=0
odd_count=0
for i in list:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print("Total Even is: ",even_count,"\nTotal odd is: ",odd_count)
