import os
import pandas as pd

parent_directory = "\\".join(os.path.abspath(__file__).split("\\")[:-2])
excel_path = os.path.join(parent_directory,"Excel Files","test.xlsx")

def get_counter(subreddit):
    try:
        df = pd.read_excel(excel_path,index_col="SubReddit Name")
        
    except:
        print("couldnt open excel file.")
        
    
    #if the subreddit has already been used before, then consider videos after that counter
    if (subreddit in list(df.index)):
        return df.loc[subreddit,"Counter"]
    
    #else start from the first post
    else:
        return 0


def write_counter(subreddit, counter):
    try:
        df = pd.read_excel(excel_path)
        
    except:
        print("ERROR : couldnt open excel file.")
        return
    if subreddit in df['SubReddit Name'].values:
        # if the subreddit exists, update the counter
        df.loc[df['SubReddit Name'] == subreddit, 'Counter'] = counter
    else:
        # if the subreddit doesn't exist, append a new row
        df_temp = pd.DataFrame({"SubReddit Name" : [subreddit],"Counter" : [counter]})
        df = pd.concat([df,df_temp])
    

    # write back to the excel file
    df.to_excel(excel_path,index = False)
    
# example usage
# print(get_counter("Unexpected"))
# write_counter("MemeVideos",38)
# 54
# write_counter("FunnyDogVideos",3)
# 14
