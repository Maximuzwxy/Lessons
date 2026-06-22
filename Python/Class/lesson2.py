# print("欢迎来到《寻找失落的宝藏》冒险游戏！")
# name = input("给主角起个名吧！\n")
# print("主角的名字是" + name)
# print(name + "来到了一个神秘的岛屿，面前有两条道路：")
# choice = input("你想选择进入'丛林'还是'山脉'？请输入你的选择：")
# if choice == "丛林":
#     print(name + "进入了深密的丛林")
#     treasure_found = True
#     trap_encountered = True
#     if treasure_found:
#         print(name + "发现了一个宝箱！")
#     if trap_encountered:
#         print(name + "遇到了一个怪物！")
#     if not (treasure_found or trap_encountered):
#         print(name + "什么也没有发现。")
# if choice == "山脉":
#     print(name + "选择攀登险峻的山脉")
#     treasure_found = True
#     trap_encountered = True
#     if treasure_found:
#         print(name + "发现了一个宝箱！")
#     elif trap_encountered:
#         print(name + "遇到了一个怪物！")
#     else:
#         print(name + "什么也没有发现。")

# player1_choice = input()
# player2_choice = input()
# if player1_choice not in ['石头', '剪刀', '布'] or player2_choice not in ['石头', '剪刀', '布']:
#     print('input error, exit')
#     exit(0)
#
# if player1_choice == player2_choice:
#     print("平局！")
# elif player1_choice == "石头" and player2_choice == "剪刀":
#     print("player1赢了！")
# elif player1_choice == "剪刀" and player2_choice == "布":
#     print("player1赢了！")
# elif player1_choice == "布" and player2_choice == "石头":
#     print("player1赢了！")
# else:
#     print("player1输了！")

# player1_choice = input()
# player2_choice = input()
# if player1_choice == player2_choice:
#     print("平局！")
# elif (player1_choice == "石头" and player2_choice == "剪刀")\
#        or (player1_choice == "剪刀" and player2_choice == "布")\
#        or (player1_choice == "布" and player2_choice == "石头"):
#     print("player1赢了！")
# else:
#     print("player1输了！")

# a = input('input number: ')
# print(type(a))
# b = int(a)
# print(type(b))

# if b > 1:
#     print('> 1')
# else:
#     print('< 1')
#
# if b > 1:
#     print('> 1')
# if b > 10:
#     print('> 10')

# if b > 1:
#     print('> 1')
# elif b > 10:
#     print('> 10')
# else:
#     print('else')

# if b > 10:
#     print('> 10')
# elif b > 1:
#     print('> 1')
# else:
#     print('else')

# a = '剪刀'
# b = '石头'

# while True:
#     a = input('A: ')
#     b = input('B: ')
#
#     if a == b:
#         print('draw')
#     elif a == '石头' and b == '剪刀':
#         print('a win')
#     elif a == '剪刀' and b == '布':
#         print('a win')
#     elif a == '布' and b == '石头':
#         print('a win')
#     else:
#         print('a lose')

# a = '布'
# b = '石头'
#
# if a == b:
#     print('draw')
# elif (a == '石头' and b == '剪刀') or (a == '剪刀' and b == '布') or (a == '布' and b == '石头'):
#     print('a win')
# else:
#     print('a lose')

a = input('A: ')
b = input('B: ')

if a == b:
    print('tie')
elif a == 'rock' and b == 'scissors':
    print('a wins')
elif a == 'scissors' and b == 'paper':
    print('a wins')
elif a == 'paper' and b == 'rock':
    print('a wins')
else:
    print('a loses')

a = input('A: ')
b = input('B: ')

if a == b:
    print('tie')
elif (a == 'rock' and b == 'scissors') or (a == 'scissors' and b == 'paper') or (a == 'paper' and b == 'rock'):
    print('a win')
else:
    print('a lose')


