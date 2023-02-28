n = 50
x = n//5 - n//10
y = n - n//5 - n//2 + n//10

ans = (2**x - 1) * 2**y

print(ans)