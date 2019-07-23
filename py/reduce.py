import pandas as pd


def load_data():
    df = pd.read_csv("stories.csv",
                 names=['col0','submission_time','col2','col3','upvotes','url','col6','headline'])
    story = df.drop(['col0','col2','col3','col6'], axis=1)
    story=story.sample(n=40000)
    return story

if __name__=="__main__":
    load_data()