# product practice
# create empty array
items = []
# open csv file
with open('product.csv', 'r', encoding='UTF-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # skip rest of action this time
		name, price = line.strip().split(',')
		items.append([name, price])
print(items)

newFile = input('Any new file? y/n: ')
if newFile == 'y':
	while True:
		name = input('Enter item name: ')
		if name == 'q':
			break
		price = input('Enter price of item: ')
		price = int(price)
#	product = [name, price]
#	product.append(name)
#	product.append(price)
		items.append([name, price])
	print(items)
	print(len(items) - 1, 'products in total.')

with open('product.csv', 'w', encoding='UTF-8') as f:
	for i in items:
		f.write(i[0] + ',' + str(i[1]) + '\n')
