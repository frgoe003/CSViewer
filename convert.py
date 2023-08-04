import json
import pandas as pd 
from collections import defaultdict

newDic = defaultdict(lambda: defaultdict(dict))

path = 'out.csv'
df = pd.read_csv(path)

id_list = df['weapon'].unique()
grouped_ids = df.groupby('weapon')

for usid in id_list:
    rows = grouped_ids.get_group(usid)


    for index, row in df.iterrows():

        weapon = row['weapon']
        weaponType = row['weaponType']
        rarity = row['rarity']
        name = row['name']
        caseName = row['caseName']
        newDic[weapon][name] = [weapon, name, rarity, weaponType, caseName]

f = open("caseData.json", "w")
json.dump(newDic, f)
f.close()
