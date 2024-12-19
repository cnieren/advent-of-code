package day#

import (
	"fmt"
)

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

		if result, err := ProcessLine(line); err != nil {
			log.Fatal(err)
		}

		// TODO: Do things with processed file
		//
	}

	fmt.Println(sum)

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