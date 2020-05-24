import cv2
import numpy as np


class Card:
    def __init__(self, dane):
        self.numer = dane[0]
        self.nazwa_panstwa = dane[1]
        self.nazwa_pola = dane[2]
        self.cena = dane[3]
        self.koszt_domku = dane[4]
        self.placa_niezabudowany = dane[5]
        self.placa1dom = dane[6]
        self.placa2dom = dane[7]
        self.placa3dom = dane[8]
        self.placa4dom = dane[9]
        self.placa5dom = dane[10]
        self.kolor = self.parse_color(dane[12])
        self.text_kolor = self.parse_color(dane[13])

    def parse_color(self, color):
        return int(color[5:7], 16), int(color[3:5], 16), int(color[1:3], 16)

    def __str__(self):
        return "{}, {}, Koszt:{}, Placa:{}, {}, {}, {}, {}".format(self.nazwa_panstwa, self.nazwa_pola, self.cena,
                                                                   self.placa1dom, self.placa2dom, self.placa3dom,
                                                                   self.placa4dom, self.placa5dom)

    def create_img(self):
        color = (244, 55, 55)
        img = np.zeros((625, 500, 3), np.uint8)
        img.fill(255)
        cv2.ellipse(img, (250, 120), (140, 80), 0, 0, 360, self.kolor, thickness=-1)
        cv2.putText(img, "{}".format(self.numer), (20, 50), 0, 0.8, color, thickness=2)
        cv2.putText(img, "AKT", (225, 80), 0, 0.8, self.text_kolor, thickness=2)
        cv2.putText(img, "WLASNOSCI", (180, 110), 0, 0.8, self.text_kolor, thickness=2)

        text_width = int(cv2.getTextSize("{}".format(self.nazwa_panstwa).upper(), 0, 0.8, 0)[0][0] / 2)
        cv2.putText(img, "{}".format(self.nazwa_panstwa).upper(), (250 - text_width, 140), 0, 0.8, self.text_kolor,
                    thickness=2)

        text_width = int(cv2.getTextSize("{}".format(self.nazwa_pola).upper(), 0, 0.8, 0)[0][0] / 2)
        cv2.putText(img, "{}".format(self.nazwa_pola).upper(), (250 - text_width, 170), 0, 0.8, self.text_kolor,
                    thickness=2)

        thickness = 1
        cv2.putText(img, "Cena zakupu", (25, 250), 0, 0.7, color, thickness)
        cv2.putText(img, "Oplata za postoj", (25, 275), 0, 0.7, color, thickness)
        cv2.putText(img, "- teren niezabudowany", (25, 300), 0, 0.7, color, thickness)
        cv2.putText(img, "- teren z 1 domem", (25, 325), 0, 0.7, color, thickness)
        cv2.putText(img, "- teren z 2 domami", (25, 350), 0, 0.7, color, thickness)
        cv2.putText(img, "- teren z 3 domami", (25, 375), 0, 0.7, color, thickness)
        cv2.putText(img, "- teren z 4 domami", (25, 400), 0, 0.7, color, thickness)
        cv2.putText(img, "- teren z 1 hotelem", (25, 425), 0, 0.7, color, thickness)

        cv2.putText(img, "$ {}".format(self.cena), (375, 250), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.placa_niezabudowany), (375, 300), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.placa1dom), (375, 325), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.placa2dom), (375, 350), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.placa3dom), (375, 375), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.placa4dom), (375, 400), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.placa5dom), (375, 425), 0, 0.7, color, thickness)

        cv2.line(img, (0, 435), (500, 435), color, thickness)
        cv2.putText(img, "Jezeli gracz posiada  wszystkie  tereny", (25, 460), 0, 0.7, color, thickness)
        cv2.putText(img, "budowlane  w  tym  panstwie i sa one", (25, 485), 0, 0.7, color, thickness)
        cv2.putText(img, "niezabudowane to oplata jest podwojna", (25, 510), 0, 0.7, color, thickness)
        cv2.line(img, (0, 525), (500, 525), color, thickness)

        cv2.putText(img, "1 dom kosztuje", (25, 550), 0, 0.7, color, thickness)
        cv2.putText(img, "1 hotel kosztuje 4 domy +", (25, 575), 0, 0.7, color, thickness)
        cv2.putText(img, "Zastaw hipoteczny", (25, 600), 0, 0.7, color, thickness)

        cv2.putText(img, "{}".format(self.koszt_domku), (375, 550), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(self.koszt_domku), (375, 575), 0, 0.7, color, thickness)
        cv2.putText(img, "{}".format(int(self.cena / 2)), (375, 600), 0, 0.7, color, thickness)

        return img
