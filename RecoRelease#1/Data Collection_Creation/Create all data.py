import pandas as pd
import random

pl=pd.read_csv("/Users/carlopastor/Desktop/Superstore.csv")

pl = pl.drop_duplicates(subset=['Product Name'], keep='first')
new_pl=pl[["Product Name","Category"]]
user_id = []
age = []
gender = []
occupation = []
location = []

for i in range(100):
    user_id.append(i)
    age.append(random.randint(18, 65))
    gender.append(random.choice(['Male', 'Female', 'Other']))
    occupation.append(random.choice(['Student', 'Engineer', 'Teacher', 'Doctor', 'Businessman']))
    location.append(random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']))

df = pd.DataFrame({'User ID': user_id, 'Age': age, 'Gender': gender, 'Occupation': occupation, 'Location': location})
df.to_csv('/Users/carlopastor/Desktop/user_info.csv', index=False)


import pandas as pd
import random
import string

product_id = []
product_name = pl["Product Name"]

category = pl["Category"]
expiration_date = []

for i in range(1850):
    product_id.append(i)
    expiration_date.append(random.choice(pd.date_range('2023-01-01', '2025-12-31').strftime('%Y-%m-%d')))

df = pd.DataFrame({'Product ID': product_id, 'Product Name': product_name, 'Category': category, 'Expiration Date': expiration_date})

df.to_csv('/Users/carlopastor/Desktop/product_info.csv', index=False)


import pandas as pd
import random
from datetime import datetime

user_id = []
product_id = []
interaction_type = []
interaction_timestamp = []

for i in range(100000):
    user_id.append(random.randint(0, 99))
    product_id.append(random.randint(0, 999))
    interaction_type.append(random.choice(['View', 'Purchase', 'Add to Cart', 'Wishlist']))
    interaction_timestamp.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

df = pd.DataFrame({'User ID': user_id, 'Product ID': product_id, 'Interaction Type': interaction_type, 'Interaction Timestamp': interaction_timestamp})
df.to_csv('/Users/carlopastor/Desktop/interaction_data.csv', index=False)