import marshal

with open("Updated.marshalled", "rb") as f:
    code = marshal.loads(f.read())

exec(code)