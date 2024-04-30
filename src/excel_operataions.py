import os
import pandas as pd

parent_directory = "\\".join(os.path.abspath(__file__).split("\\")[:-2])
excel_path = os.path.join(parent_directory,"Excel Files","counters.xlsx")

def get_counter(subreddit):
    try:
        df = pd.read_excel(excel_path)
    except:
        print("couldnt open excel file.")
    
    #if the subreddit has already been used before, then consider videos after that counter
    if (subreddit in df["SubReddit Name"]):
        return df.iloc[subreddit]["counter"]
    #else start from the first post
    else:
        return 0

def write_counter(subreddit, counter):
    try:
        df = pd.read_excel(excel_path)
        print(df.columns)
    except:
        print("couldnt open excel file.")
    if subreddit in df['SubReddit Name'].values:
        # if the subreddit exists, update the counter
        df.loc[df['SubReddit Name'] == subreddit, 'Counter'] = counter
    else:
        # if the subreddit doesn't exist, append a new row
        df = df._append({'SubReddit Name': subreddit, 'Counter': counter}, ignore_index=True)
    
    # df.rename(columns={'row': 'Sl.No'}, inplace=True)

    # write back to the dataframe with SL.No starting from 1
    df.to_excel(excel_path, index=True, startrow=1)
    
# example usage
# counter = get_counter("Unexpected")
# print(counter)

write_counter("Unexpected",47)