try:
    string = 'asdfg'
    print(string[9])
except Exception as e:
    print(isinstance(e, IndexError))
    print('IndexError')