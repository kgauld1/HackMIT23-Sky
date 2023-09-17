import pickle
from datetime import datetime

with open('jsdata.pkl', 'rb') as f:
	jsdata = pickle.load(f)

print('opened')

for x in jsdata:
	x['time'] = datetime.timestamp(datetime.strptime(x['time'],'%Y-%m-%dT%H:%M:%S.000Z'))

print('formatted')

with open('rftdat.pkl', 'wb') as rf:
	pickle.dump(jsdata, rf)

print('saved')
