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
for i in items:
	print(i[0], i[1])

with open('product.csv', 'w', encoding='UTF-8') as f:
	f.write('商品,價格\n')
	for i in items:
		f.write(i[0] + ',' + str(i[1]) + '\n')
