#!/usr/bin/env python3
# Mapping of Latin letters to multiple confusable Unicode homoglyphs

import argparse
import random


puny_map = {
    'a': ['à', 'á', 'â', 'ã', 'ä', 'å', 'ā', 'ă', 'ą', 'ȧ', 'ӓ', 'а'],  # Cyrillic а
    'b': ['ƀ', 'ƃ', 'ɓ', 'б', 'в'],
    'c': ['ç', 'ć', 'ĉ', 'ċ', 'č'],
    'd': ['ď', 'đ', 'ɖ', 'ɗ', 'ԁ', 'ԃ'],
    'e': ['è', 'é', 'ê', 'ë', 'ē', 'ĕ', 'ė', 'ę', 'ě', 'ӗ'],
    'f': ['ƒ', 'ғ'],
    'g': ['ĝ', 'ğ', 'ġ', 'ģ', 'ǥ', 'ɠ'],
    'h': ['ĥ', 'ħ', 'н', 'һ'],
    'i': ['ì', 'í', 'î', 'ï', 'ĩ', 'ī', 'ĭ', 'į', 'ı', 'ӥ', 'і', 'ɨ'],
    'j': ['ĵ', 'ј'],
    'k': ['ķ', 'ĸ', 'к', 'қ', 'ҝ'],
    'l': ['ĺ', 'ļ', 'ľ', 'ŀ', 'ł', 'ӏ'],
    'm': ['м', 'ṃ', 'ɱ'],
    'n': ['ñ', 'ń', 'ņ', 'ň', 'ŋ', 'ɲ', 'п'],
    'o': ['ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'ō', 'ŏ', 'ő', 'ǿ', 'ȯ', 'ӧ', 'о'],
    'p': ['þ', 'р', 'ƥ', 'ρ'],
    'q': ['զ', 'ʠ'],
    'r': ['ŕ', 'ŗ', 'ř', 'ɾ'],
    's': ['ś', 'ŝ', 'ş', 'š', 'ѕ'],
    't': ['ţ', 'ť', 'ŧ', 'ʈ', 'т'],
    'u': ['ù', 'ú', 'û', 'ü', 'ũ', 'ū', 'ŭ', 'ů', 'ű', 'ų', 'ӯ', 'ư', 'µ'],
    'v': ['ѵ', 'ν'],
    'w': ['ŵ', 'ш', 'щ', 'ѡ'],
    'x': ['х', 'ҳ', 'ӽ', 'ӿ'],
    'y': ['ý', 'ÿ', 'ŷ', 'у', 'ў', 'ӯ'],
    'z': ['ź', 'ż', 'ž', 'ƶ', 'ȥ'],

    'A': ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Ā', 'Ă', 'Ą', 'Ȧ', 'Ӓ', 'А'],
    'B': ['ß', 'Ɓ', 'Б', 'В'],
    'C': ['Ç', 'Ć', 'Ĉ', 'Ċ', 'Č'],
    'D': ['Ď', 'Đ', 'Ɗ', 'Ԁ', 'Ԃ'],
    'E': ['È', 'É', 'Ê', 'Ë', 'Ē', 'Ĕ', 'Ė', 'Ę', 'Ě', 'Ӗ'],
    'F': ['Ғ'],
    'G': ['Ĝ', 'Ğ', 'Ġ', 'Ģ', 'Ǥ'],
    'H': ['Ĥ', 'Ħ', 'Н', 'Һ'],
    'I': ['Ì', 'Í', 'Î', 'Ï', 'Ĩ', 'Ī', 'Ĭ', 'Į', 'İ', 'Ӥ', 'І'],
    'J': ['Ĵ', 'Ј'],
    'K': ['Ķ', 'К', 'Қ', 'Ҝ'],
    'L': ['Ĺ', 'Ļ', 'Ľ', 'Ŀ', 'Ł', 'Ӆ'],
    'M': ['М', 'Ṃ'],
    'N': ['Ñ', 'Ń', 'Ņ', 'Ň', 'Ŋ', 'П'],
    'O': ['Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ō', 'Ŏ', 'Ő', 'Ǿ', 'Ȯ', 'Ӧ', 'О'],
    'P': ['Þ', 'Р', 'Ƥ', 'Ρ'],
    'Q': ['Ԛ'],
    'R': ['Ŕ', 'Ŗ', 'Ř'],
    'S': ['Ś', 'Ŝ', 'Ş', 'Š', 'Ѕ'],
    'T': ['Ţ', 'Ť', 'Ŧ', 'Т'],
    'U': ['Ù', 'Ú', 'Û', 'Ü', 'Ũ', 'Ū', 'Ŭ', 'Ů', 'Ű', 'Ų', 'Ү', 'Ư'],
    'V': ['Ѵ'],
    'W': ['Ŵ', 'Ш', 'Щ', 'Ѡ'],
    'X': ['Х', 'Ҳ', 'Ӽ', 'Ӿ'],
    'Y': ['Ý', 'Ÿ', 'Ŷ', 'У', 'Ў', 'Ӯ'],
    'Z': ['Ź', 'Ż', 'Ž', 'Ƶ', 'Ȥ']
}

def to_puny(text):
	return ''.join(random.choice(puny_map.get(ch, [ch])) for ch in text)

def print_map():
	for char in puny_map:
		print(char, end = " : ")
		for puny_s in puny_map.get(char,[char]):
			print(puny_s ,end = " ")
		print()

def main():
	parser = argparse.ArgumentParser(description="Convert text to puny/homoglyph lookalikes using Unicode confusables.")
	parser.add_argument('-text', type=str, help="Text to convert into puny/homoglyphs")
	parser.add_argument('--print', action='store_true', help="Print homoglyphs for each alphabetic character")

	args = parser.parse_args()

	if args.print :
		print_map()
	elif args.text :
		print("Original :\n\t" + args.text)
		print("Converted :\n\t" + to_puny(args.text))
	else :
		parser.print_help()


if __name__ == "__main__" :
	main()
