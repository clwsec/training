package main

import (
	"fmt"
)

func bar() {
	i := 0
	defer fmt.Println(i)
	i++
	fmt.Println(i)
}

func main() {
	bar()
}
