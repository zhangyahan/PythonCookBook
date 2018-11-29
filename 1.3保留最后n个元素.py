from collections import deque  
"""
q = deque(maxlen=n): 返回一个长度为n的固定队列,
                     当队列满时,去除最老的那一条数据,
q.append(element):   添加元素
q.del(element):      删除元素
q.appendleft():      向最左边添加元素
q.pop():             弹出元素
q.popleft():         弹出最左边的元素
"""


def search(lines, pattern, history=5):
    pervious_lines = deque(maxlen=history)
    # 创建一个索引为maxlen的固定列表
    for line in lines:
        # 遍历一行文本文本
        if pattern in line:
            # 如果指定文本在内, 返回行和列表
            yield line,pervious_lines
        pervious_lines.append(line)


if __name__ == "__main__":
    with open('./1.3demo.txt') as f:
        for line, pervious_lines in search(f.readlines(), 'python', 1):
            for pline in pervious_lines:
                print('pline',pline, end='')
            print('line',line, end='')
            print('-'*20)

