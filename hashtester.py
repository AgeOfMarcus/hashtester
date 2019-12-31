import uuid, json

def gen(leng):
	res = ''.join(str(uuid.uuid4()).split("-"))
	while len(res) < leng:
		res += ''.join(str(uuid.uuid4()).split("-"))
	return res[:leng]

def load(fn):
	return json.loads(open(fn,"r").read())

def test(func, leng=8, prog={
	'total':0,
	'hashes':{},
	'bad':0,
	}):
	while True:
		try:
			dat = gen(leng)
			hsh = func(dat.encode())
			if hsh in prog['hashes']:
				prog['hashes'][hsh].append(dat)
				prog['bad'] += 1
			else:
				prog['hashes'][hsh] = [dat]
			prog['total'] += 1

			print("total: %i, bad: %i, current: %s/%s" % (
				prog['total'],
				prog['bad'],
				dat,hsh), end="\r")
		except KeyboardInterrupt:
			if not input("Save progress? Y/n: ").lower()[0] == "n":
				fn = input("Filename: ")
				with open(fn, "w") as f:
					f.write(json.dumps(prog))
			exit(0)