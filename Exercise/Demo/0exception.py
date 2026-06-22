# print(0/0))
# print(2/0)

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5!')
# print(x)

# x = 10
# assert x < 5, 'The number should not exceed 5.'
# print(x)

# import sys
# print(sys.platform)
# assert 'Linux' in sys.platform, 'This code run on Linux only'

import sys
def linux_interaction():
    print(sys.platform)
    assert 'Linux' in sys.platform, 'This code run on Linux only'

def win32_interaction():
    print(sys.platform)
    assert 'win32' in sys.platform, 'This code run on win32 only'

# linux_interaction()

# try:
#     linux_interaction()
# except:
#     print('catch exception')

# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)

# try:
#     file = open('file.log', 'r')
#     data = file.read()
#     print(data)
#     file.close()
# except FileNotFoundError as error:
#     print(error)
#     print('could not find the file')

# try:
#     linux_interaction()
#     file = open('file.log', 'r')
#     data = file.read()
#     print(data)
#     file.close()
# except AssertionError as a_error:
#     print(a_error)
# except FileNotFoundError as f_error:
#     print(f_error)
#     print('could not find the file')

# try:
#     win32_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('okk')

# try:
#     win32_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log', 'r') as f:
#             print(f.read())
#     except FileNotFoundError as error:
#         print(error)

# try:
#     win32_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log', 'r') as f:
#             print(f.read())
#     except FileNotFoundError as error:
#         print(error)
# finally:
#     print('Finally Done')

def test():
    try:
        a = 5 / 0
        print('try')
        return 0
    except:
        print('except')
        return 1
    finally:
        print('finally')
        return 2

def test1():
    try:
        a = 5 / 0
        print('try')
    except:
        print('except')
    finally:
        print('finally')

def test2():
    try:
        a = 5 / 0
        print('try')
        return 0
    except:
        print('except')
        return 1
    print('finally')

# print('test:', test())
# print('test1:', test1())
print('test2:', test2())
























