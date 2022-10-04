def solve_riddle(riddle: str, word_length: int, start_letter: str, reverse=True):
	if not reverse:
		for num, ch in enumerate(riddle):
			if ch is start_letter:
				return riddle[num:num+word_length]
	else:
		riddle = riddle[::-1]
		for num, ch in enumerate(riddle):
			if ch is start_letter:
				return riddle[num:num+word_length]
	return ''






print(solve_riddle('aaaaaaaaaaaa', 5, 'p'))