from loader import Loader
from card import Card
import cv2
import os

loader = Loader("eurogotowe.csv")
dane = loader.load()
cards = [Card(dane.iloc[i, :].values) for i in range(dane.shape[0])]

for card in cards:
    img = card.create_img()

    cv2.imshow("{}".format(card.nazwa_pola), img)
    cv2.waitKey(0)
    if not os.path.exists('obrazki'):
        os.makedirs('obrazki')
    cv2.imwrite("{}/obrazki/{}-{}.jpg".format(os.path.dirname(__file__),card.numer, card.nazwa_pola), img)
