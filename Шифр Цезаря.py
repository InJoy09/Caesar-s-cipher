
print('-' * 15)


def detect_lang(phrase):
	lst = phrase.split()
	count_ru = 0
	count_en = 0
	for el in lst:
		if not el[0].isalpha():
			continue
		q = ord(el[0].lower())
		if q in range(1072, 1104):
			count_ru += 1
		elif q in range(97, 123):
			count_en += 1

	if count_ru and not count_en:
		return 'ru'
	elif count_en and not count_ru:
		return 'en'
	else:
		return 'mixed'


def get_shift_step():
	shift = input('Шаг сдвига (положительный - зашифровать, отрицательный - расшифровать) >_ ')

	while True:
		try:
			shift = int(shift)
			return shift
		except ValueError:
			shift = input('Шаг сдвига должен быть числом >_ ')


def coding_char(ch, shift, begin, end):
	new_ord = ord(ch) + shift
	if new_ord > end:
		new_ord = new_ord - end + begin - 1
	return chr(new_ord)


def decoding_char(ch, shift, begin, end):
	new_ord = ord(ch) + shift
	if new_ord < begin:
		new_ord = end - (begin - new_ord) + 1
	return chr(new_ord)


def transform_phrase(phrase, shift, begin, end):
	transform = coding_char if shift > 0 else decoding_char
	res = ''

	for ch in phrase:
		is_upper = False
		if ch.isalpha():
			if ch.isupper():
				ch = ch.lower()
				is_upper = True
			new_char = transform(ch, shift, begin, end)
			if is_upper:
				new_char = new_char.upper()
			res += new_char
		else:
			res += ch

	print(res)


def main():
	print('Программа шифрует и дешифрует фразу по принципу шифра Цезаря,')
	print('поддерживается русский и английский алфавит(определяется автоматически),')
	print('цифры и знаки препинания игнорируются')

	phrase = input('\nВведите текст: >_ ')
	shift = get_shift_step()

	lang = detect_lang(phrase)
	if lang == 'ru':
		shift %= 32
		transform_phrase(phrase, shift, 1072, 1103)
	elif lang == 'en':
		shift %= 26
		transform_phrase(phrase, shift, 97, 122)
	elif lang == 'mixed':
		print('Этот диалект я не знаю!')
		print('Фраза должна быть либо на русском, либо на английском языке')


main()
