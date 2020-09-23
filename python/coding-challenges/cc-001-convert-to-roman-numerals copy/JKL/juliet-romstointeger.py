
def int_to_rome():
    while True:
        try:
            a = input("lütfen 0 ile 4000 arası bir sayı giriniz: \nçıkış için exit yazmanız yeterli.")
            if a.lower() == "exit":
                break
            n = int(a)
            if not 0 < n <4000:
                return "lütfen belirtilen aralıkta bir sayı giriniz"
            b = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
            c = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
            d= []
            for i in range(len(b)):
                count = int((n/b[i]))
                d.append(count*c[i])
                n -= count * b[i]
            return "".join(d)
        except ValueError:
            return "lütfen tam sayı bir değer giriniz: "

int_to_rome()