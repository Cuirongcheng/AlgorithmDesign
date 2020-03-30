# 算法分析与设计实验
# 崔荣成 2020.3.13

import numpy as np

'''
	一、欧几里得算法
	问题描述：求两个不全为0的非负整数m和n的最大公约数
	算法名称：欧几里得算法
	算法介绍：两个不全为0的非负整数m和n的最大公约数记为gcd(m,n)，代表能够整除（即余数为0）m和n的最大正整数。
	欧几里得算法通过重复计算公式gcd(m,n)=gcd(n,m mod n)，直到m mod n等于0，m最后的取值也就是m和n的初值的最大公约数。
'''
print("算法一：")
def gcd(m,n):
    while n:
        r=m%n
        m=n
        n=r
    return m
print(gcd(60, 24))

'''
    二、埃拉托色尼筛选法
    问题描述：产生一个不大于给定整数n的连续质数序列
    算法名称：埃拉托色尼筛选法
    算法描述：该算法一开始初始化一个2~n的连续整数序列，作为候选质数。然后，在算法的第一个循环中，它将类似4和6这样的2的倍数从序列中消去。
    然后，它指向列表中的下一个数字3，又将其倍数消去。第三步处理序列中剩下的下一个元素5.该算法以这个方式不断做下去，直到序列中已经没有可消的元素为止。序列中剩下的整数就是我们要求的质数。
'''
print("算法二：")
def sieve_of_eratosthenes(n):#埃拉托色尼筛选法，返回少于n的素数
    primes = [True] * (n+1)#范围0到n的列表
    p = 2#这是最小的素数
    while p * p <= n:#一直筛到sqrt(n)就行了
        if primes[p]:#如果没被筛，一定是素数
            for i in range(p * 2, n + 1, p):#筛掉它的倍数即可
                primes[i] = False
        p += 1
    primes = [element for element in range(2, n) if primes[element]]#得到所有少于n的素数
    return primes
print(sieve_of_eratosthenes(100))

'''
    三、顺序查找 
    问题描述：在n个元素的列表中查找一个给定项
    算法名称：顺序查找算法
    算法描述：顺序查找，查找键K与列表中连续元素作比较，直到发现匹配查找键元素或者到达了列表的终点。
    为了简单起见，列表我们用数组来实现。如果判断数组下标是否越过上界的第一个条件为假则不会判断第二个条件A[i]≠K。
'''
print("算法三：")
A = [i for i in range(20)]
print(A)
i = 0
K = 8
n = len(A)
while i<n and A[i] != K:
    i = i+1
if i < n:
    print(i)
else:
    print(-1)

'''
    四、求给定数组中最大元素的值
    问题描述：从n个元素的列表中查找最大值
    算法描述：假设列表是用数组实现的，遍历数组中的值，然后找出最大的那个。
'''
print("算法四：")
A = np.random.randint(1, 20, 10)
print(A)
max = A[0]
n = len(A)
for i in range(n):
    if A[i] > max:
        max = A[i]
print(max)

'''
    五、元素唯一性问题
    问题描述：验证给定数组中的n个元素是否全部唯一。
    算法描述：依次判断数组中每个元素与其他元素值是否相同，如果数组中有相同元素程序返回false，否则返回true。
'''
print("算法五：")
def UniqueElements():
    A = np.random.randint(1, 150, 5)
    print(A)
    n = len(A)
    for i in range(n-2):
        for j in range(i+1,n-1):
            if A[i] == A[j]:
                return False
    return True

print(UniqueElements())

'''
    六、矩阵乘积
    问题描述：求两个给定的n阶方阵A和B的乘积
'''
print("算法六：")
A = np.random.randint(1,4,(2,2))
B = np.random.randint(2,6,(2,2))
C = np.zeros((2,2))
n = len(A)
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i,j] = C[i,j] + A[i,k]*B[k,j]
print(A)
print(B)
print(C)

'''
    七、十进制换二进制个数
    问题描述：求一个十进制正整数在二进制表示中的二进制数字个数。
'''
print("算法七：")
n = int(input("输入一个正整数："))
count = 1
while n > 1:
    count+=1
    n = int(n/2)
print(count)

'''
    八、递归求阶乘
    问题描述：求任意非负整数n的阶乘
    算法描述：当n≥1，n！=n*(n-1)*…*1=n*(n-1)!，由定义知0！=1
'''
print("算法八：")
def F(n):
    if n == 0:
        return 1
    result = n * F(n - 1)
    return result
print(F(5))

'''
    九、递归计算斐波那契
    问题描述：求第n个斐波那契数
    算法描述：当n≥2，F(n)=F(n-1)+F(n-2)，由定义知F(0)=0, F(1)=1
'''
print("算法九：")
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return F(n-1) + F(n-2)
print(F(5))
