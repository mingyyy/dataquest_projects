import read


def count_word():
    df = read.load_data()
    domains = df["url"].value_counts()
    counter = 0
    for name, row in domains.items():
        counter += 1
        if counter <= 10:
            print("{0}:{1}".format(name, row))


if __name__ == "__main__":
    count_word()