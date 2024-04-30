# from excel_operataions import get_counter
import pandas as pd


excel_path = r"Excel Files\test.xlsx"
# df = pd.read_excel(excel_path)

# df = pd.DataFrame({"SubReddit Name":["Unexpected"],"Counter":[4]})

# df = pd.concat([df,df11])


# df11 = pd.read_excel(excel_path)

df12 = pd.DataFrame({"SubReddit Name" : ["Memes"],"Counter" : [45]})

# df11 = pd.concat([df11,df12])
df12.to_excel(excel_path,index = False)
print(df12.columns)