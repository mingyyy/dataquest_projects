import pandas as pd

def load_data():
    story=pd.read_csv("hn_stories.csv",
                 names=['submission_time','upvotes','url','headline'])
    return story

if __name__=="__main__":
    load_data()