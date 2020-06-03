# Fast-Exponential

## Problem Description

Input: N, and N pairs of a, b
Output: N rows of c

Define $M = 1e9 + 7$.

$c_i = {a_i}^{b_i} \% M$.

## Problem Size

- 30%: N<=10, b<=10
- 70%: N<=10,000, b<=10,000
- 100%: N<=1,000,000, b<=1,000,000, a<=10,000,000

## Reference

- https://oi-wiki.org/math/quick-pow/