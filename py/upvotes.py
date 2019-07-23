import reduce


def count_upvote():
    df = reduce.load_data()
    upvotes = df["upvotes"].value_counts(sort=True, ascending=False)
    counter = 0
    for name, row in upvotes.items():
        counter += 1
        if counter <= 10:
            print("{0}:{1}".format(name, row))


def max_upvote():
    df = reduce.load_data()
    df.sort_values("upvotes", inplace=True, ascending=False)
    print(df.head(10))
    return df


if __name__ == "__main__":
    # count_upvote()
    max_upvote()
