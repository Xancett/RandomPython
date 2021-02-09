# n is the number of triangles
n = 60
# p is the perimeter
p = 0
for i in range(n + 1):
	p += i + i + i
print(p)

# Also can be solved by:
# p = p / 3
# p = n * (n + 1) / 2
# 3660 = n(n+1)
# Using (n-60)(n+61) we get n=60