from loader import Loader
from card import Card

loader = Loader("eurogotowe.csv")
dane = loader.load()
cards = [Card(dane.iloc[i, :].values) for i in range(dane.shape[0])]

for card in cards:
    print(card)
