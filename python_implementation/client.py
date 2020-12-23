from xmlrpc.client import ServerProxy
if __name__ == '__main__':
    s = ServerProxy('http://localhost:8000', allow_none=True)
    while True:
        print('Select an option: ')
        print('1. Get value from key')
        print('2. Set value from key')
        print('3. Delete key')
        print('4. Check if key exist')
        print('5. Show all keys')
        print('6. Exit')
        opt = int(input('Select an option: '))
        if opt == 1:
            key = input('Key: ')
            data = s.get(key)
            print(data)
        elif opt == 2:
            key = input('Key: ')
            value = input('Value: ')
            s.set(key, value)
            print('Data set!!')
        elif opt == 3:
            key = input('Key: ')
            data = s.delete(key)
            print('Data deleted!!')
        elif opt == 4:
            key = input('Key: ')
            data = s.exists(key)
            print(data)
        elif opt == 5:
            data = s.keys()
            print(data)
        elif opt == 6:
            print('Bye bye OwO')
            break
        else:
            print('Invalid option')