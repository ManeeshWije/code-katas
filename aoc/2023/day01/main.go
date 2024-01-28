package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func part1() {
	content, err := os.ReadFile("input")

	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")
	total := 0

	for i := 0; i < len(lines); i++ {
		var first, last rune

		for j := 0; j < len(lines[i]); j++ {
			if unicode.IsDigit(rune(lines[i][j])) {
				first = rune(lines[i][j])
				break
			}
		}

		for k := len(lines[i]) - 1; k >= 0; k-- {
			if unicode.IsDigit(rune(lines[i][k])) {
				last = rune(lines[i][k])
				break
			}
		}

		num1, _ := strconv.Atoi(string(first))
		num2, _ := strconv.Atoi(string(last))

		num := num1*10 + num2
		total += num
	}
	fmt.Printf("part1: %d\n", total)
}

func part2() {
	d_num := map[string]string{"zero": "z0o", "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

	content, err := os.ReadFile("input")

	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")
	total := 0

	for _, line := range lines {
		modified_line := line

		for key, val := range d_num {
			modified_line = strings.ReplaceAll(modified_line, key, val)
		}

		var first, last rune

		for j := 0; j < len(modified_line); j++ {
			if unicode.IsDigit(rune(modified_line[j])) {
				first = rune(modified_line[j])
				break
			}
		}

		for k := len(modified_line) - 1; k >= 0; k-- {
			if unicode.IsDigit(rune(modified_line[k])) {
				last = rune(modified_line[k])
				break
			}
		}

		num1, _ := strconv.Atoi(string(first))
		num2, _ := strconv.Atoi(string(last))

		num := num1*10 + num2
		total += num
	}
	fmt.Printf("part2: %d\n", total)
}

func main() {
	part1()
	part2()
}
