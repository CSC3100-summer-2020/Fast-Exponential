import random

M = int(1e9 + 7)

def exp(a, b):
  r = 1
  for _ in range(b):
    r *= a
    r = int(r % M)
  return r

def exp_fast(a, b):
  r = 1
  c = a
  while b>0:
    if b&1==1:
      r = int((r*c) % M)
    b = int(b >> 1)
    c = int((c*c) % M)
  return r


i = input("ID:")
n = int(input("Number:"))
mb = int(input("max b:"))

with open("{}.in".format(i), "w") as fin:
  fin.write("{}\n".format(n))
  with open("{}.out".format(i), "w") as fout:
    for _ in range(n):
      a = random.randint(0, 1e7)
      b = random.randint(0, mb)
      # print(a, b)
      # print(exp(a, b))
      # print(exp_fast(a, b))
      # assert exp(a, b) == exp_fast(a, b)
      fin.write("{} {}\n".format(a, b))
      fout.write("{}\n".format(exp_fast(a, b)))

print("Finish")