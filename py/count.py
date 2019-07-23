import reduce


def count_word():
    df = reduce.load_data()
    counter = 0
    hl = ""
    for line in df["headline"]:
        if type(line) is type("str"):
            line = str(line.lower()) + ' '
            hl += line

    word_list = hl.split(" ")
    unsorted = freq(word_list)

    for w in sorted(unsorted, key=unsorted.get, reverse=True):
        counter += 1
        if counter <= 100:
            print(w, unsorted[w])


def freq(list):
    word_dict = {}
    for word in list:
        word = word.strip()
        # word = re.match('^[a-z]$',word)
        if word in word_dict:
            word_dict[word] += 1
        elif word.isalpha():
            word_dict[word] = 1
    return word_dict


if __name__ == "__main__":
    count_word()