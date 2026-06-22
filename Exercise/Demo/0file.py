# r只读，w只写且清空文件，r+读写，w+读写且清空文件，a只追加，a+追加和读，w，w+，a，a+都会创建文件
# read()是全部读出来
# 下面的代码，如果不加flush，读不到，因为没有真正写到问里面
# close的时候会执行flush
# a = open('aa.txt', 'w+')
# a.write('aaa')
# a.flush()
# b = open('aa.txt', 'r')
# print(b.read())
# a.close()
# b.close()

# 文件的指针会随着走
# a = open('aa.txt', 'r')
# print(a.read(4))
# print(a.read(2))
# a.close()

# with open('aa.txt', 'r') as f:
#     print(f.read())

# 二进制用'rb'，默认是t，比如'rt'等于'r'
# with open('aa.txt', 'rb') as f:
#     a = f.read()
#     print(a) # 输出：b'aaa\r\nbbb'
#     b = a.decode('utf-8')
#     print(b)

# readline返回str，readlines返回list
# with open('aa.txt', 'r') as f:
#     # print(f.readline())
#     print(f.readlines())

## list的生成表达式
# import os
# files = []
# print(os.getcwd())
# for file in os.listdir(os.getcwd()):
#     print(file)
#     if os.path.isfile(file) and file.endswith('.txt'):
#         files.append(file)
# print(files)
#
# files = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file) and file.endswith('.txt')]
# print(files)

# 文件路径操作
# import os
# path = os.getcwd()
# print(path)
# dir_path = os.path.dirname(path)
# print(dir_path)
#
# tmp_path = path + '/tmp'
# if not os.path.exists(tmp_path):
#     os.mkdir(tmp_path)
# lst = os.listdir(path)
# print(lst)
#
# os.chdir(tmp_path)
# print(os.getcwd())
# os.chdir(tmp_path + '/..')
# print(os.getcwd())
# os.rmdir(tmp_path)
# print(os.listdir(path))

# # DFS
# import os
# path = os.getcwd()
# dir_path = os.path.dirname(path)
#
# def list_dir_dfs(cur_path):
#     print(cur_path)
#     for item in os.listdir(cur_path):
#         tmp = os.path.join(cur_path, item)
#         if os.path.isfile(tmp):
#             print(item)
#         elif os.path.isdir(tmp):
#             list_dir_dfs(tmp)
#
# list_dir_dfs(dir_path)

## BFS
# import os
# path = os.getcwd()
# dir_path = os.path.dirname(path)
#
# def list_dir_bfs(cur_path):
#     lst = [cur_path]
#     while lst:
#         cur = lst.pop(0)
#         print(cur)
#         print(os.listdir(cur))
#
#         for item in os.listdir(cur):
#             tmp = os.path.join(cur, item)
#
#             if os.path.isfile(tmp):
#                 print(item)
#             elif os.path.isdir(tmp):
#                 lst.append(tmp)
#
# list_dir_bfs(dir_path)

# # 处理二进制文件
# import pickle
#
# # 定义各种类型的数据
# i = 13000000  # 整数
# a = 99.056  # 浮点数
# s = '中国人民123abc'  # 字符串
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 嵌套列表
# tu = (-5, 10, 8)  # 元组
# coll = {4, 5, 6}  # 集合
# dic = {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}  # 字典
#
# # 将所有数据整合到一个列表中
# data = [i, a, s, lst, tu, coll, dic]
#
# # 使用 with 语句安全地打开文件
# with open('sample_pickle.dat', 'wb') as f:
#     try:
#         # 首先写入数据项的数量
#         pickle.dump(len(data), f)
#
#         # 遍历并写入每个数据项
#         for item in data:
#             pickle.dump(item, f)
#
#         print("数据成功写入文件！")
#
#     except Exception as e:
#         # 捕获并处理可能的异常
#         print(f'写文件异常: {str(e)}')
#
# with open('sample_pickle.dat', 'rb') as f:
#     n = pickle.load(f)
#     for i in range(n):
#         x = pickle.load(f)
#         print(x)

