# RecoRelease-1

**This is our first supermarket recommendation app release, containing data collection, preparation, exploration and first modeling attempt.**

This release should be viewed in the following order (3 Steps):

**Step 1:**

The Data Collection/Creation, which can be viewed in the 'Data Collection/Creation folder'. It contains the 7 files that make up the whole data collection process. In order to create the final "supermarket_data.csv" file for the modeling, we followed the following process:
1. First download the "Superstore.csv" file.
2. Then download the "Create all data.py file". Open the file and run it. This will use the "Superstore.csv" file to create, "user_info.csv", "product_info.csv" and "interaction_data.csv".
3. Then, download "Create Supermarket_data.py". Open the file and run it. This will use the previously created 3 files to create our final data file "supermarket_data.csv".

**Step 2:**

The Data Cleaning/Preparation and some Explatory Data Analysis. This can be viewed in the 'Data Cleaning/Preparation + EDA' folder, containing a single ipynb notebook.

**Step 3:**

The Modeling. This can be viewed in the 'Modeling' folder, and inside the single ipynb notebook which shows our first algorithm attempt using collaborative filtering to recommend supermarket products.
