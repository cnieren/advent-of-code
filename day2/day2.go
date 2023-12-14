package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Game struct {
	number, red, green, blue int
}

func SplitLine(line string) []string {
	return strings.Split(line, ":")
}

func ProcessLine(line string) (Game, error) {
	return Game{1, 1, 1, 1}, nil
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

	for scanner.Scan() {
		line := scanner.Text()

		result, err := ProcessLine(line)

		if err != nil {
			log.Fatal(err)
		}

		// TODO: Do things with processed file
		fmt.Println(result)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

func main() {
	fileName := "sample1.txt"

	if len(os.Args) >= 2 {
		fileName = os.Args[1]
	}

	ProcessFile(fileName)
}
