package main

import (
	"fmt"
	"strings"
	"testing"
)

func TestSplitLine(t *testing.T) {
	line := "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
	actual := SplitLine(line)

	for _, v := range actual {
		fmt.Println(strings.Trim(v, " "))
	}
}
