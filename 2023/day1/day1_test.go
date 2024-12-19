package main

import (
	"reflect"
	"testing"
)

func TestFindFirstDigit(t *testing.T) {
	testcases := []struct {
		in                 string
		wantDigit, wantIdx int
	}{
		{"two1nine", 1, 3},
		{"4nineeightseven2", 4, 0},
		{"six", -1, -1},
		{"4", 4, 0},
		{"nonumbers", -1, -1},
	}

	for _, tc := range testcases {
		digit, idx := FindFirstDigit(tc.in)

		if digit != tc.wantDigit || idx != tc.wantIdx {
			t.Fatalf(`FindFirstDigit(%s) = %d, %d want %d, %d`, tc.in, digit, idx, tc.wantDigit, tc.wantIdx)
		}
	}
}

func TestFindLastDigit_WithOneDigit(t *testing.T) {
	testcases := []struct {
		line               string
		wantDigit, wantIdx int
	}{
		{"two1nine", 1, 3},
		{"4nineeightseven2", 2, 15},
		{"six", -1, -1},
		{"4", 4, 0},
		{"nonumbers", -1, -1},
	}

	for _, tc := range testcases {
		digit, idx := FindLastDigit(tc.line)

		if digit != tc.wantDigit || idx != tc.wantIdx {
			t.Fatalf(`FindLastDigit(%s) = %d, %d want %d, %d`, tc.line, digit, idx, tc.wantDigit, tc.wantIdx)
		}
	}
}

func TestFirstWordNumber(t *testing.T) {
	testcases := []struct {
		line               string
		wantDigit, wantIdx int
	}{
		{"two1nine", 2, 0},
		{"4nineeightseven2", 9, 1},
		{"six", 6, 0},
		{"4", -1, -1},
		{"nonumbers", -1, -1},
	}

	for _, tc := range testcases {
		digit, idx := FindFirstWordNumber(tc.line)

		if digit != tc.wantDigit || idx != tc.wantIdx {
			t.Fatalf(`FindFirstWordNumber(%s) = %d, %d want %d, %d`, tc.line, digit, idx, tc.wantDigit, tc.wantIdx)
		}
	}
}

func TestFindLastWordNumberd(t *testing.T) {
	testcases := []struct {
		line               string
		wantDigit, wantIdx int
	}{
		{"two1nine", 9, 4},
		{"4nineeightseven2", 7, 10},
		{"six", 6, 0},
		{"4", -1, -1},
		{"nonumbers", -1, -1},
	}

	for _, tc := range testcases {
		digit, idx := FindLastWordNumber(tc.line)

		if digit != tc.wantDigit || idx != tc.wantIdx {
			t.Fatalf(`FindLastWordNumber(%s) = %d, %d want %d, %d`, tc.line, digit, idx, tc.wantDigit, tc.wantIdx)
		}
	}
}

func TestProcessLine(t *testing.T) {
	testcases := []struct {
		line string
		want map[int]int
	}{
		{"two1nine", map[int]int{0: 2, 3: 1, 4: 9}},
		{"4nineeightseven2", map[int]int{0: 4, 1: 9, 10: 7, 15: 2}},
		{"six", map[int]int{0: 6}},
		{"4", map[int]int{0: 4}},
		{"nonumbers", nil},
	}

	for _, tc := range testcases {
		actual, err := ProcessLine(tc.line)
		if err != nil {
			if tc.line == "nonumbers" {
				return
			} else {
				t.Fatalf("Unexpected Error encountered with inputs %+v", tc)
			}
		}
		if !reflect.DeepEqual(tc.want, actual) {
			t.Fatalf(`ProccessLine(%s) = %v want %+v`, tc.line, tc.want, actual)
		}
	}
}

func TestGetLineSum(t *testing.T) {
	testcases := []struct {
		line map[int]int
		want int
	}{
		{map[int]int{0: 2, 3: 1, 4: 9}, 29},
		{map[int]int{0: 4, 1: 9, 10: 7, 15: 2}, 42},
		{map[int]int{0: 6}, 66},
		{map[int]int{0: 4}, 44},
	}

	for _, tc := range testcases {
		actual := GetLineSum(tc.line)
		if !reflect.DeepEqual(tc.want, actual) {
			t.Fatalf(`GetLineSum(%v) = %d want %d`, tc.line, tc.want, actual)
		}
	}
}
