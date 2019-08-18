func countCharacters(words []string, chars string) int {
	count := make(map[string]int)
	for _, c := range chars {
		count[string(c)]++
	}

	ans := 0
	for _, word := range words {
		// copy count
		newCount := make(map[string]int)
		for k, v := range count {
			newCount[k] = v
		}
		// check
		done := true
		for _, c := range word {
			s := string(c)
			if newCount[s] == 0 {
				done = false
				break
			}
			newCount[s]--
		}
		if done {
			ans += len(word)
		}
	}
	return ans
}
