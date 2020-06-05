package main

import "fmt"

var M int

func exp(a, b int) (c int)  {
	c = 1
	one := int(1)
	for b>0 {
		if b&one==one {
			c = (c * a) % M
		}
		a = (a * a) % M
		b = b >> 1
	}
	return 
}

func main() {
	var n, a, b, i int
	M = int(1000000007)

	fmt.Scanf("%d", &n)
	for i=0; i<n; i++ {
		fmt.Scanln(&a, &b)
		fmt.Println(exp(a, b))
	}
}