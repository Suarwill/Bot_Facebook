def codec(w, cifrar=True):
    x , i = "" , 0
    for c in w:
        y = ord(c)
        if cifrar : nV = (y+i)%256
        else: nV = (y-i)%256
        i += 1
        nV = max(0, min(nV, 0x10FFFF))
        nC = chr(nV)
        x += nC
    return x

texto = "bde16757"
nueva = codec(texto)
print(nueva)
print(codec(nueva,False))