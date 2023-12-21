import struct
import gzip
import os

archivename = "model"

f = open(f"{archivename}.gz","rb")
fbytes = f.read()
f.close()

header = fbytes[0:8]
data = fbytes[8::]
datas = data.split(b"\x1F\x8B")

files = []
indexdata = b""
for j in range(128):
    try:
        k = gzip.decompress(b"\x1F\x8B"+datas[1][0:len(datas[0])-j])
        print(len(k))
        indexdata = k
    except:
        pass

fi = open(archivename,"rb")
fibytes = fi.read()
fi.close()

offset = 0
offset = 0
index = ["./output/0","./output/index.txt"]
for i in range(5380):
    header_offset = (i)*14
    header = fibytes[header_offset+offset : offset+header_offset+14]
    path = fibytes[offset+header_offset+14:offset+header_offset+14+header[4]].decode()
    offset = offset + header[4]
    fullpath = os.path.join("./output",path)
    index.append(fullpath)
    directory,filename = os.path.split(fullpath)
    if not os.path.exists(directory):
        os.makedirs(directory)
print(index)

for ind,i in enumerate(datas):
    for j in range(64):
        try:
            k = gzip.decompress(b"\x1F\x8B"+i[0:len(i)-j])
            print(ind,len(k),j,path,k[0:4])
            path = index[ind]
            
            f = open(path,"wb")
            f.write(k)
            f.close()
        except:
            pass