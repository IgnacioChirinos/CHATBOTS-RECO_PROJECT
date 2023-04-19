

import pandas as pd
data = pd.read_csv('data.csv')
def recommend_for_user(model, test_data, user_id, num_recs): 
    # Get the user's interactions from the test dataset
    user_interactions = test_data[test_data['User ID'] == user_id]
    
    # Generate top-k recommendations for the user
    top_k = model.recommend_k_items(user_interactions, top_k=num_recs, remove_seen=True)
    
    # Join with product names
    top_k_with_titles = top_k.join(data[['Product ID', 'Product Name']].drop_duplicates().set_index('Product ID'), 
                                    on='Product ID', 
                                    how='inner').sort_values(by='Prediction', ascending=False)
    
    # Return the top recommendations for the user
    return top_k_with_titles.head(num_recs)

