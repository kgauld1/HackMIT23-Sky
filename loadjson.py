import time
import json
import pickle

st = time.time()
file = open('dawndata.json', 'r')
jsdata = json.load(file)
file.close()

print("LOADED")
print(time.time() -st)

with open('jsdata.pkl', 'wb') as wfile:
	pickle.dump(jsdata, wfile)
