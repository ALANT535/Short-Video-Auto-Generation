import os
import pandas as pd

def get_counter(subreddit):
    parent_directory = "\\".join(os.path.abspath(__file__).split("\\")[:-2])
    excel_path = os.path.join(parent_directory,"Excel Files","counters.xlsx")
    df = pd.read_excel(excel_path)
    
    #if the subreddit has already been used before, then consider videos after that counter
    if (subreddit in df["SubReddit Name"]):
        return df.iloc[subreddit]["counter"]
    #else start from the first post
    else:
        return 0

# counter = get_counter("Unexpected")
# print(counter)