def profit(hisseSenetleriFiyatlari):
    
    enYuksekKar = 0 
    gecerliBuyukDeger = 0
    for fiyat in reversed(hisseSenetleriFiyatlari):
        gecerliBuyukDeger = max(gecerliBuyukDeger, fiyat)
        muhtemelKar = gecerliBuyukDeger - fiyat
        enYuksekKar = max(muhtemelKar, enYuksekKar)

    return enYuksekKar
print(profit([8, 20, 30, 5, 7, 9]))

[9, 7, 5, 30, 20, 8]

