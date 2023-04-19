import pandas as pd
import numpy as np
import datetime
import os
from sklearn.preprocessing import LabelEncoder
import pytest

df = pd.read_csv('supermarket_data.csv')
filtered_df = df[pd.to_datetime(df["Expiration Date"]).dt.date <= (pd.Timestamp.now() + pd.Timedelta(days = 60)).date()]
agg_interactions_super100 = filtered_df.groupby('Product Name').agg(mean_interaction=('Interaction Type', 'mean'),
                                                                    number_of_interactions=('Interaction Type', 'count')).reset_index()

agg_interactions_super100 = agg_interactions_super100[agg_interactions_super100['number_of_interactions'] > 50]
df_S10 = pd.merge(filtered_df, agg_interactions_super100[['Product Name']], on='Product Name', how = 'inner')


def test_pearson_correlation():
    matrix = pd.DataFrame(np.random.rand(100, 10))
    similarity = matrix.corr(method = 'pearson')
    assert similarity.shape == (10, 10)


def test_cosine_similarity():
    matrix = pd.DataFrame(np.random.rand(100, 10))
    similarity = matrix.corr(method = 'cosine')
    assert similarity.shape == (10, 10)


def test_label_encoder():
    le = LabelEncoder()
    data = ['View', 'Purchase', 'Add to Cart', 'Wishlist']
    le.fit(data)
    encoded_data = le.transform(data)
    assert list(encoded_data) == [1, 4, 3, 2]


def test_file_download():
    assert os.path.exists('supermarket_data.csv') == True


def test_dataframe_size():
    users = pd.read_csv('user_info.csv')
    products = pd.read_csv('product_info.csv')
    interactions = pd.read_csv('interaction_data.csv')
    assert users.shape == (1000, 5)
    assert products.shape == (167, 3)
    assert interactions.shape == (100000, 4)


def test_dataframe_datatypes():
    users = pd.read_csv('user_info.csv')
    products = pd.read_csv('product_info.csv')
    interactions = pd.read_csv('interaction_data.csv')
    assert users.dtypes.tolist() == ['User ID', 'Age', 'Gender', 'Occupation', 'Location']
    assert products.dtypes.tolist() == ['Product ID', 'Product Name', 'Expiration Date']
    assert interactions.dtypes.tolist() == ['User ID', 'Product ID', 'Interaction Type', 'Interaction Timestamp']



def test_interaction_timestamp_range():
    interactions = pd.read_csv('interaction_data.csv')
    timestamp_min = datetime.datetime.strptime(interactions['Interaction Timestamp'].min(), '%Y-%m-%d %H:%M:%S')
    timestamp_max = datetime.datetime.strptime(interactions['Interaction Timestamp'].max(), '%Y-%m-%d %H:%M:%S')
    assert timestamp_min.year >= 2023
    assert timestamp_max.year <= 2025


if __name__ == '__main__':
    pytest.main()