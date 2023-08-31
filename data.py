import json
import numpy as np
#data = json.load(file)
with open('test_data_collection.txt',"r") as file:
    lines = file.readlines()
    for line in lines:
        d = json.loads(line)
        print(np.array(d['answer']['rp_y']))
        print(np.array(d['answer']['rp_y']).shape)
        break