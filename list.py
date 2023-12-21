import struct
f = open("model","rb")
fbytes = f.read()
f.close()

offset = 0

for i in range(5380):
    header_offset = (i)*14
    header = fbytes[header_offset+offset : offset+header_offset+14]
    name = fbytes[offset+header_offset+14:offset+header_offset+14+header[4]].decode()
    offset = offset + header[4]
    adress = struct.unpack("<i",header[0:4])[0]
    size = struct.unpack("<i",header[6:10])[0]
    unk = struct.unpack("<i",header[10:14])[0]
    print(" ".join([hex(x).replace("0x","").rjust(2) for x in header ])+"\n"+"Name:",name+"\n"+"Adress:",str(adress)+"\n"+"Size:",str(size)+"\n"+"unk:",str(unk))