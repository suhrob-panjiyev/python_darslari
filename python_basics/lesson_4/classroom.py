unlilar_soni=0
undoshlar_soni=0
name="Suhrob".lower()
unlilar="aeuio"
for n in name:
    if n in unlilar:
        unlilar_soni=unlilar_soni+1
        print(f"{n}, unli harf")
    else:
        undoshlar_soni=undoshlar_soni+1
        print(f"{n}, undosh harf")
print(unlilar_soni, "ta unli bor")
print(undoshlar_soni, "ta undosh bor")
