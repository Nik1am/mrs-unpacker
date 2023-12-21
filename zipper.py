import gzip
f = open("model","rb")
content = f.read()
f.close()
with gzip.open('model.txt.gz', 'wb') as f:
    f.write(content)