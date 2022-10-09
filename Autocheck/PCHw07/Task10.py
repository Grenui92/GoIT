def make_request(keys, values):
	return dict(zip(keys, values)) if len(keys) == len(values) else {}




print(make_request(['name', 'age', 'email'], ['Nick', '23', 'nick@test.com']))