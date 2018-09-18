# -*- coding: utf-8 -*
# Time    : 2018/9/18 9:52


# import queue
# py3下
import Queue
# py2下


data_q = Queue.Queue()

# 打印队列的存储地址
print(data_q)

'''['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'_get', '_init', '_put', '_qsize', 
'all_tasks_done', 'empty', 'full', 
'get', 'get_nowait', 
'join', 'maxsize', 'mutex', 'not_empty', 
'not_full', 
'put', 'put_nowait', 
'qsize'  查看队列长度, 
'queue', 'task_done', 'unfinished_tasks']'''
data_q.put("aaa")
print(data_q.not_empty())