# 我们想要反向迭代序列中的元素

# 可以使用內建函数reversed()函数实现反向迭代
# a = [1, 2, 3, 4]
# for x in reversed(a):
#     print(x)


# 自定义
class Countdown:
    def __init__(self, start):
        self.start = start

    def __reversed__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    
    def __iter__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

a = Countdown(5)
for i in a:
    print(i)

for i in reversed(a):
    print(i)

                    
