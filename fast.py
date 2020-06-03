M = int(1e9 + 7)

def exp_fast(a, b):
  r = 1
  c = a
  while b>0:
    if b%2==1:
      r = int((r*c) % M)
    b = int(b >> 1)
    c = int((c*c) % M)
  return r

n = int(input())
for _ in range(n):
  a, b = input().split()
  a = int(a)
  b = int(b)
  print(exp_fast(a, b))