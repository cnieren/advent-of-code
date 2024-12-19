package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
)

func FindFirstDigit(line string) (digit, index int) {
	for idx, val := range line {
		if unicode.IsNumber(val) {
			num, _ := strconv.Atoi(string(val))
			return num, idx
		}
	}

	return -1, -1
}

func FindLastDigit(line string) (digit, index int) {
	runeLine := []rune(line)

	for i := len(runeLine) - 1; i >= 0; i-- {
		if unicode.IsNumber(runeLine[i]) {
			num, _ := strconv.Atoi(string(runeLine[i]))
			return num, i
		}
	}

	return -1, -1
}

func FindFirstWordNumber(line string) (digit, index int) {
	numberWords := []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	var numberIdxMap = make(map[int]int)

	for i, word := range numberWords {
		idx := strings.Index(line, word)
		if idx != -1 {
			numberIdxMap[idx] = i
		}
	}

	if len(numberIdxMap) <= 0 {
		return -1, -1
	}

	keys := make([]int, 0, len(numberIdxMap))
	for k := range numberIdxMap {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	return numberIdxMap[keys[0]], keys[0]
}

func FindLastWordNumber(line string) (digit, index int) {
	numberWords := []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	var numberIdxMap = make(map[int]int)

	for i, word := range numberWords {
		idx := strings.LastIndex(line, word)
		if idx != -1 {
			numberIdxMap[idx] = i
		}
	}

	if len(numberIdxMap) <= 0 {
		return -1, -1
	}

	keys := make([]int, 0, len(numberIdxMap))
	for k := range numberIdxMap {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	return numberIdxMap[keys[len(keys)-1]], keys[len(keys)-1]
}

func ProcessLine(line string) (map[int]int, error) {
	var result = make(map[int]int)

	digit, idx := FindFirstDigit(line)
	if digit != -1 && idx != -1 {
		result[idx] = digit
	}

	digit, idx = FindFirstWordNumber(line)
	if digit != -1 && idx != -1 {
		result[idx] = digit
	}

	digit, idx = FindLastDigit(line)
	if digit != -1 && idx != -1 {
		result[idx] = digit
	}

	digit, idx = FindLastWordNumber(line)
	if digit != -1 && idx != -1 {
		result[idx] = digit
	}

	if len(result) > 0 {
		return result, nil
	}

	return nil, errors.New("No values found")
}

func GetLineSum(input map[int]int) int {
	keys := make([]int, 0, len(input))
	for k := range input {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	return 10*input[keys[0]] + input[keys[len(keys)-1]]
}

func ProcessFile(fileName string) {
	// open file
	f, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}

	// Close the file at the end of the program
	defer f.Close()

	scanner := bufio.NewScanner(f)

	sum := 0

	for scanner.Scan() {
		line := scanner.Text()

		if result, err := ProcessLine(line); err == nil {
			sum += GetLineSum(result)
		}
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

func main() {
	fileName := "sample2.txt"

	if len(os.Args) >= 2 {
		fileName = os.Args[1]
	}

	ProcessFile(fileName)
}
