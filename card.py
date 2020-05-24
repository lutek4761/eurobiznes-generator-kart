class Card:
    def __init__(self, dane):
        self.numer = dane[0]
        self.nazwa_panstwa = dane[1]
        self.nazwa_pola = dane[2]
        self.cena = dane[3]
        self.koszt_domku = dane[4]
        self.placa1dom = dane[5]
        self.placa2dom = dane[6]
        self.placa3dom = dane[7]
        self.placa4dom = dane[8]
        self.placa5dom = dane[9]

    def __str__(self):
        return "{}, {}, Koszt:{}, Placa:{}, {}, {}, {}, {}".format(self.nazwa_panstwa, self.nazwa_pola, self.cena,
                                                              self.placa1dom, self.placa2dom, self.placa3dom,
                                                              self.placa4dom, self.placa5dom)
