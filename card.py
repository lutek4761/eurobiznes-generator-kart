import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


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

        fontpath = "./AbhayaLibre-Medium.ttf"
        font = ImageFont.truetype(fontpath, 30)
        font2 = ImageFont.truetype(fontpath, 24)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((20, 50), "{}".format(self.numer), font=font, fill=color)
        draw.text((220, 50), "AKT", font=font, fill=self.text_kolor)
        draw.text((170, 80), "WŁASNOŚCI", font=font, fill=self.text_kolor)
        draw.text((int(250 - font.getsize("{}".format(self.nazwa_panstwa).upper())[0]/2), 110), "{}".format(self.nazwa_panstwa).upper(), font=font, fill=self.text_kolor)
        draw.text((int(250 - font.getsize("{}".format(self.nazwa_pola).upper())[0]/2), 140), "{}".format(self.nazwa_pola).upper(), font=font, fill=self.text_kolor)

        draw.text((25, 225), "Cena zakupu", font=font2, fill=color)
        draw.text((25, 250), "Opłata za postój", font=font2, fill=color)
        draw.text((25, 275), "- teren niezabudowany", font=font2, fill=color)
        draw.text((25, 300), "- teren z 1 domem", font=font2, fill=color)
        draw.text((25, 325), "- teren z 2 domami", font=font2, fill=color)
        draw.text((25, 350), "- teren z 3 domami", font=font2, fill=color)
        draw.text((25, 375), "- teren z 4 domami", font=font2, fill=color)
        draw.text((25, 400),  "- teren z 1 hotelem", font=font2, fill=color)

        draw.text((450 - font2.getsize("$ {}".format(self.cena))[0], 225), "$ {}".format(self.cena), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.placa_niezabudowany))[0], 275), "{}".format(self.placa_niezabudowany), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.placa1dom))[0], 300), "{}".format(self.placa1dom), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.placa2dom))[0], 325), "{}".format(self.placa2dom), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.placa3dom))[0], 350), "{}".format(self.placa3dom), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.placa4dom))[0], 375), "{}".format(self.placa4dom), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.placa5dom))[0], 400), "{}".format(self.placa5dom), font=font2, fill=color)

        draw.text((25, 440), "Jeżeli  gracz  posiada  wszystkie  tereny", font=font2, fill=color)
        draw.text((25, 465), "budowlane   w   tym   państwie  i  są one", font=font2, fill=color)
        draw.text((25, 490), "niezabudowane to opłata jest podwójna", font=font2, fill=color)

        draw.text((25, 525), "1 dom kosztuje", font=font2, fill=color)
        draw.text((25, 550), "1 hotel kosztuje 4 domy +", font=font2, fill=color)
        draw.text((25, 575), "Zastaw hipoteczny", font=font2, fill=color)

        draw.text((450 - font2.getsize("{}".format(self.koszt_domku))[0], 525), "{}".format(self.koszt_domku), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(self.koszt_domku))[0], 550), "{}".format(self.koszt_domku), font=font2, fill=color)
        draw.text((450 - font2.getsize("{}".format(int(self.cena / 2)))[0], 575), "{}".format(int(self.cena / 2)), font=font2, fill=color)
        img = np.array(img_pil)

        cv2.line(img, (0, 435), (500, 435), color)
        cv2.line(img, (0, 525), (500, 525), color)
        print(font.getsize("Zastaw hipoteczny"))

        return img
