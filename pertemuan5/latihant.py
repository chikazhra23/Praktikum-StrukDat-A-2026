data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama, poin in data_aktivitas:
    if poin > 80:
        print(f"{nama} memdapat predikat Gold")
    elif 50 <= poin <=80:
        print(f"{nama} memdapat predikat Silver")
    else:
        print(f"{nama} memdapat predikat Bronze")
