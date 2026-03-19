# strip
# s = ' Hello, World! '
# print(len(s))
# # print(s.split())
# s1 = s.strip()
# print(s1)
# print(len(s1))
#
# s2 = s.lstrip()
# print(s2)
# print(len(s2))
#
# s3 = s.rstrip()
# print(s3)
# print(len(s3))

# s = 'hello,world'
# sp = s.split(',')
# print(sp, type(sp))
#
# s = 'hello world   hola'
# print(s.split())

# s = 'Python is awesome'
# s1 = 'om'
#
# print(s.find(s1))
# print(s.find(s1, 2, 5))
# print(s.find(s1, 10))
#
# print(s.find('o'))
# print(s.rfind('o'))

# aa = '***'
# lst = ['apple', 'banana', 'pear']
# s = aa.join(lst)
# print(s)

# print(' and '.join(lst))
#
# b = 'Harry has a ballon'
# print(','.join(b))
#
# s = 'abcde'
# print(' '.join(s[::-1]))
# print(' '.join(reversed(s)))
#
# print(b.replace('has', 'had'))
# print(b.replace('a', 'A'))

# s = 'harry Hz Nx'
# print(s.upper())
# print(s.lower())
# print(s.capitalize())

# num = '5'
# letter = 'abcde'
#
# print(num.isnumeric())
# print(num.isalnum())
# print(num.isalpha())
# print(letter.isalpha())
# print(' d  '.isspace())

# movie = "2001: A SAMMY ODYSSEY"
# book = "A Thousand Splendid Sharks"
# poem = "sammy lived in a pretty how town"
#
# print(movie.islower())
# print(movie.isupper())
#
# print(book.istitle())
# print(book.isupper())
#
# print(poem.istitle())
# print(poem.islower())

# a = input()
# s = a.split()
# print(s)
# print(s[-1])



# def last_word(s):
#     lst = s.split()
#     if len(lst) == 0:
#         return ''
#     else:
#         return lst[-1]
#
# ss = input('str: ')
# print(len(last_word(ss)))

# def change(s):
#     if s.isupper():
#         return s.lower()
#     else:
#         return s.upper()
#
# ss = input('s: ')
# print(change(ss))

def compare_str(s1, s2):
    ret = 0
    if len(s1) != len(s2):
        ret = 1
    else:
        if s1 == s2:
            ret = 2
        else:
            if s1.upper() == s2.upper():
                ret = 3
            else:
                ret = 4

    return ret

# while True:
#     s1 = input('s1: ')
#     s2 = input('s2: ')
#     print(compare_str(s1, s2))


# while True:
#     lst = [0] * 26
#
#     s = input('s: ')
#     for i in s:
#         index = ord(i) - ord('a')
#         lst[index] += 1
#     l = lst[::-1]
#     print(ord('a'))
#     max_c = chr(ord('a') + 25 - l.index(max(l)))
#     print(max(l), max_c)



# palindrome
# s = input('s: ')

# if s == s[::-1]:
#     print(True)
# else:
#     print(False)

# ret = True
# for i in range(len(s) // 2):
#     if s[i] != s[len(s) - i - 1]:
#         ret = False
#         break
# print(ret)

# ret = True
# left, right = 0, len(s) - 1
# while left < right:
#     if s[left] != s[right]:
#         ret = False
#         break
#     left += 1
#     right -= 1
# print(ret)


# while True:
#     s = input('s: ')
#     if is_palindrome(s):
#         print(True)
#     else:
#         ret = False
#         for i in range(len(s)):
#             lst = list(s)
#             lst.pop(i)
#             s1 = ''.join(list(lst))
#             if s1 == s1[::-1]:
#                 ret = True
#         print(ret)



# s = 'abcedf'
# print(' '.join(s))
# print(''.join(reversed(s)))
