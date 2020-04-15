# 算法分析与设计实验
# 崔荣成 2020.3.18
# 蛮力法常用算法整理

print("字符串匹配算法")

def BruteForceStringMatch(t,p):
   n = len(t)
   m = len(p)
   for i in range(n-m):
      j = 0
      while j < m and p[j]==t[i+j]:
         j = j+1
         if j == m:
            return i
         else:
            return -1
T = "cuirongcheng"
P = "r"
print(BruteForceStringMatch(T,P))
