import json

with open("GetLiveEvents.json", "r") as raw_file:
    print(raw_file)
    raw_json = json.load(raw_file)
print(raw_json)
json_data_COD = raw_json[0]
print(json_data_COD)

j3 = 0
sports_NodeId_COD = []
sports_Active_COD = []
sports_Locked_COD = []
# for j1 in json_data_COD:
print(json_data_COD['Events'][0])
for j2 in json_data_COD['Events'][0]:
    print(json_data_COD['Events'][0][j2])
    sports_NodeId_COD.append(json_data_COD['Events'][0]['NodeId'])
    sports_Active_COD.append(json_data_COD['Events'][0]['IsActive'])
    sports_Locked_COD.append(json_data_COD['Events'][0]['Locked'])


print("FILE 22222222")
print(sports_Locked_COD)
