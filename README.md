# RecoRelease-2

**This is our second supermarket recommendation app release, containing data collection, preparation, exploration and first modeling attempt.**

This release should be viewed in the following order (3 Steps):

**Step 1:**

The Data Collection/Creation, which can be viewed in the 'Projectlib/datasets'. It contains the 2 files that make up the whole data collection process. In order to create the final "supermarket_data.csv" file for the modeling, we followed the following process:
1. First download the csv file from https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset?resource=download.
2. Then with the "DataCreation.ipynb" execute to create the "supermarket_data.csv" that is the data is going to be use for the recomendation system

**Step 2:**

The Modeling. This can be viewed in the 'Projectlib/Models' folder, and inside 2 ipynb notebook. The first shows our first algorithm attempt using collaborative filtering to recommend supermarket products and the second uses a SAR model aplaid based on recommeders approach.

**Step 3:**

The implementaion of a Flask API. this can be viewed in the 'Projectlib/Flask' folder. Where also the implementation of a simple front-end is create in the template folder, thst is use by the ipynb file called FLaskAPI to create the local API.

**Step 4:**

The app implementation to deploy in azure is created and with that we add more files, necessary for the deployment using Git Actions.
