# Fast-Exponential

## Problem Description

Input: N, and N pairs of a, b
Output: N rows of c

Define $M = 1e9 + 7$.

$c_i = {a_i}^{b_i} \% M$.

## Problem Size

- 30%: N<=10, b<=10
- 70%: N<=10,000, b<=10,000
- 100%: N<=500,000, b<=500,000, a<=10,000,000

## Sample

Input:

```
5
576960 0
1445976 1
6813812 1
4575144 2
2444059 2
```

Output:

```
1
1445976
6813812
942474219
424353670
```

## Reference

- https://oi-wiki.org/math/quick-pow/