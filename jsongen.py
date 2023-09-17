text_fn = 'dawnEventDataStream.txt'
with open(text_fn, 'r') as f:
	agg = f.read()
n_agg = '[\n'+agg.replace('\n', ',\n')[:-2]+'\n]'
# print(n_agg[-1000:])

with open('dawndata.json', 'w') as f:
	f.write(n_agg)
