lst = ['car', 'bike', 'bus', 'truck', 'boat', 'bicycle']

lst2 = lst + lst
lst3 = lst * 2
print(lst2)
print(lst3)
print(len(lst))         #--> length of list

print(lst[3])           #--> print element at given index
print(lst[2:5])         #--> print items from index 2 to 4
print(lst[-1])          #--> last item
print('skip : ', lst[::2])  #--> print alternative items (2 is for skip 1 item, means every 2nd item will be printed)
print(lst[-2])          #--> second last item
print(lst[-3:-1])       #--> print items from index -3 to -1

lst.append('train')     #--> adds an item to the end of the list
print(lst)

lst[1] = 'aeroplane'    #--> updating list
print(lst)

del(lst[2])             #--> deleting given indexed data from list
print(lst)

lst.append('bus')       #--> only one value append at a time
lst.append('bike')
print(lst)

print('pop() : ')
print(lst.pop(2))              #--> remove given index's item from list, and return that item from list
print(lst)

print(lst.remove('train'))     #--> remove given element from list, and return None, not an item like pop
print(lst)

lst.extend(['train','truck'])  #--> add items to end of the list
print(lst)

lst.insert(3, 'scooter')       #--> adds an item to the given position
print(lst)

print(sorted(lst))             #--> sorts the list

print(lst[::-1])               #--> reverses the list

lst2 = [1, 2, 3, 4, 5, 6, 4, 6, 4]
print(lst.count(4))			#--> prints occurrences of given elment. Here it is '4'

print(max(lst))
print(min(lst))
