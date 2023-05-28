package main

import (
	"fmt"
)

// 【修改】： 数组作为函数入参时是值传递
func modify(array [5]int) {
	array[0] = 10
	fmt.Println("调用修改函数修改之后的arr:", array)
}

func main() {
	// 【修改】传入数组，注意数组与slice的区别
	array := [5]int{1, 2, 3, 4, 5}

	modify(array)
	fmt.Println("主函数函数中修改之后的arr:", array)

}
