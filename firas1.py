
f_list = [9, 3, 5, 8, 4]
swapped = True
while swapped:
    swapped = False
    for i in range (len(f_list)-1):
         if f_list[i] > f_list[i+1]:
              swapped = True
              f_list[i],f_list[i+1] = f_list[i+1],f_list[i]
              
print(f_list)        
       