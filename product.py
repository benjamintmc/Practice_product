# product practice
items = []
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
print(len(items), 'products in total.')

print('You bought these items: ')
for i in range(2):
	print(items[i][0], items[i][1])