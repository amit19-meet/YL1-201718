list1= [3,6,11,7]
def new_list(list1):
	new_list= [list1[0], list1[-1]]
	print(new_list)

new_list(list1)
a = [1, 1, 6, 3, 5, 8, 2, 21, 34, 55, 89]

def less_than_5(a):
	for value in a:
		if(value<5):
			print(value)


		

less_than_5(a)

def new_list2(a):
	new_list3= []
	for i in a:
		if(i<5):
			new_list3.append(i)

	print(new_list3)

new_list2(a)








