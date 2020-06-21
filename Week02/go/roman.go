package main


func romanToInt(s string) int {
	specialMap := map[string]int{"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900} //特殊罗马数字
	romanMap := map[string]int{"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}   //正常罗马数字
	result := 0
	for len(s) != 0 {
		if len(s) > 1 {
			chars := s[0:2]
			if v, ok := specialMap[chars]; ok {
				result += v
				s = s[2:]
			} else {
				result += romanMap[string(s[0])]
				s = s[1:]
			}
		} else {
			result += romanMap[string(s[0])]
			s = s[1:]
		}
	}
	return result
}
