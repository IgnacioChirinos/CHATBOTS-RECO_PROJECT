USER_INFO_FILE = 'user_info.csv'
PRODUCT_INFO_FILE = 'product_info.csv'
INTERACTION_DATA_FILE = 'interaction_data.csv'
SUPERMARKET_DATA_FILE = 'supermarket_data.csv'

EXPECTED_USERS_SHAPE = (1000, 5)
EXPECTED_PRODUCTS_SHAPE = (167, 3)
EXPECTED_INTERACTIONS_SHAPE = (100000, 4)


USER_COL_NAMES = ['User ID', 'Age', 'Gender', 'Occupation', 'Location']
PRODUCT_COL_NAMES = ['Product ID', 'Product Name', 'Expiration Date']
INTERACTION_COL_NAMES = ['User ID', 'Product ID', 'Interaction Type', 'Interaction Timestamp']

MINIMUM_TIMESTAMP_YEAR = 2023
MAXIMUM_TIMESTAMP_YEAR = 2025