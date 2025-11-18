from stats import count_words, count_char_to_str, sort_dict
import sys

def main():
	try:
		sys.argv[1]
	except IndexError:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		dic = count_char_to_str(sys.argv[1])

		print("============ BOOKBOT ============")
		print(f'Analyzing book found at {sys.argv[1]}...')
		print("----------- Word Count ----------")
		print(count_words(sys.argv[1]))
		print("--------- Character Count -------")
		print(sort_dict(dic))
		print("============= END ===============")

main()

