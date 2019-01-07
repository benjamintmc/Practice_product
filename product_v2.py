import os
# define functions
item_list = []
def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            item_list.append([name, price])
    return item_list
def input_item(item_list):
    while True:
        name = input('Enter item name: (enter q to exit) ')
        if name == 'q':
            break
        price = input('Enter price of item: ')
        price = int(price)
        item_list.append([name, price])
    return item_list
def write_in_file(filename, item_list):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write('商品,價格\n')
        for i in item_list:
            f.write(i[0] + ',' + str(i[1]) + '\n')
    return item_list
def create_file(filename):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write('商品,價格\n')
# define real activities = main function
def main():
    filename = input('What is the file name? ')
    if os.path.isfile(filename):
        print('File found!')
        read_file(filename)
        print(item_list)
        if input('Any new items? y/n ') == 'y':
            input_item(item_list)
            write_in_file(filename, item_list)
            print('Updated as below,')
        print(item_list)
    else:
        print('No such file...')
        print('Creating new file...')
        create_file(filename)
        if input('Any new items? y/n ') == 'y':
            read_file(filename)
            input_item(item_list)
            write_in_file(filename, item_list)
        print('Updated as below,')
        print(item_list)
# run main 
if __name__ == '__main__':
    main()