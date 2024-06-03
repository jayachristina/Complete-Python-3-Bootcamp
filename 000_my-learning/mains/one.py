#one.py

def func():
    print ("func() in one.py")

print("top in one.py")
if __name__ == '__main__':
    print('one.py is run directly')
else:
    print('one.py has been imported')