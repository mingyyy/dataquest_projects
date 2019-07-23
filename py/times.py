import read
import dateutil


def get_hour(dt):
    dt = dateutil.parser.parse(dt)
    hour = dt.hour
    return hour


def get_day(dt):
    dt = dateutil.parser.parse(dt)
    day = dt.day
    return day


def count_hour():
    df = read.load_data()
    sub_hour = df["submission_time"].apply(lambda x: get_hour(x))
    hour_freq = sub_hour.value_counts()
    counter = 0
    for name, row in hour_freq.items():
        print("{0}:{1}".format(name, row))


def count_day():
    df = read.load_data()
    sub_day = df["submission_time"].apply(lambda x: get_day(x))
    day_freq = sub_day.value_counts()
    counter = 0
    for name, row in day_freq.items():
        print("{0}:{1}".format(name, row))


if __name__ == "__main__":
    # count_hour()
    count_day()