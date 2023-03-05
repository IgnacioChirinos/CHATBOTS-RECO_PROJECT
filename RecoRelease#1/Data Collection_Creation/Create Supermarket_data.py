import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder

# Load the data
users = pd.read_csv('/Users/carlopastor/Desktop/user_info.csv')
products = pd.read_csv('/Users/carlopastor/Desktop/product_info.csv')
interactions = pd.read_csv('/Users/carlopastor/Desktop/interaction_data.csv')

products['Expiration Date'] = pd.to_datetime(products['Expiration Date'])

# Encode the categorical variables
le = LabelEncoder()
products['Category'] = le.fit_transform(products['Category'])
users['Gender'] = le.fit_transform(users['Gender'])
users['Occupation'] = le.fit_transform(users['Occupation'])
interactions['Interaction Type'] = le.fit_transform(interactions['Interaction Type'])

# Merge the dataframes
data = interactions.merge(users, on='User ID').merge(products, on="Product ID")

# Filter out expired products and drop missing values

data = data[data['Expiration Date'] > pd.Timestamp.today()]
data.dropna(inplace=True)

data.to_csv('/Users/carlopastor/Desktop/supermarket_data.csv', index=False)