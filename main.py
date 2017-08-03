import os
import pandas as pd

ARTICLES_PATH = '/media/hdd/training_data/transfer-learning-sed/'


def load_data(path):
    csvs = os.listdir(path)
    csvs.remove('sample_submission.csv')
    csvs.remove('test.csv')
    articles_paths = [os.path.join(path, csv) for csv in csvs]
    X_titles = []
    X_contents = []
    y = []
    for article_path in articles_paths:
        new_articles = pd.read_csv(article_path)
        X_titles.extend(list(new_articles['title'].copy()))
        X_contents.extend(list(new_articles['content'].copy()))
        y.extend(list(new_articles['tags'].copy()))

    return X_titles, X_contents, y


X1, X2, y = load_data(ARTICLES_PATH)
print(X2[:3])
