temperatures=[33.4,56.7,12.9,56.0,97.5]
total=0
for temp in temperatures:
    total+=temp

average=total/len(temperatures)
print(average)