package main

import (
	"fmt"
)

func foo() string {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered:", r)
		}
	}()
	fmt.Println("Start")
	panic("Something went wrong")
}

func main() {
	result := foo()
	fmt.Println("Result:", result)
}
