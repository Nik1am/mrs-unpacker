import gzip

#with gzip.open('1.txt.gz', 'rb') as f:
#    file_content = f.read()
#    print(file_content)

with open('model.txt.gz', 'rb') as f:
    file_content = f.read()
    print(gzip.decompress(file_content))