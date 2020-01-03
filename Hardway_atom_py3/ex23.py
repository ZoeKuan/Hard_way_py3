import sys
script, encoding, error = sys.argv #ex13.py


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) #if F return main
#if: check T or F

def print_line(line, encoding, errors):
    next_lang = line.strip() #del "\n" every lines
    raw_bytes = next_lang.encode(encoding, errors = errors) #set .encode(method, error)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


language = open("languages.txt", encoding = "utf-8")

main(language, encoding, error)
