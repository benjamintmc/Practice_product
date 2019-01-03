# product practice
import os # import Operating System
# create empty array
items = []
# if csv exists, open csv
if os.path.isfile('product.csv'):
	with open('product.csv', 'r', encoding='UTF-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # skip rest of action this time
			name, price = line.strip().split(',')
			items.append([name, price])
	print(items)
	# check if there is new file to add
	newFile = input('Any new file? y/n: ')
	if newFile == 'y':
		while True:
			name = input('Enter item name: ')
			if name == 'q':
				break
			price = input('Enter price of item: ')
			price = int(price)
			items.append([name, price])
	# buy history
		print(items)
		print(len(items), 'products in total.')
	# add new items into the existing sheet
	with open('product.csv', 'w', encoding='UTF-8') as f:
		f.write('商品,價格\n')
		for i in items:
			f.write(i[0] + ',' + str(i[1]) + '\n')
# if csv not exist, print error
else:
	print('No file founded...')
	createNew = input('Do you want to create a new CSV file? y/n: ')
	if createNew == 'y':
		while True:
			name = input('Enter item name: ')
			if name == 'q':
				break
			price = input('Enter price of item: ')
			price = int(price)
			items.append([name, price])
	# buy history
		print(items)
		print(len(items), 'products in total.')
		with open('product.csv', 'w', encoding='UTF-8') as f:
			f.write('商品,價格\n')
			for i in items:
				f.write(i[0] + ',' + str(i[1]) + '\n')