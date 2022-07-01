

from regex import P
from entities.coin import Coin

import time
import random

class World:

    def __init__(self, character):
        self.coins = [] # to stock later in the chunk (maybe)
        self.character = character

        for i in range(10):
            c = Coin(random.randint(1,5)*80, random.randint(3,5)*80)
            self.coins.append(c)
            c.synchronize(self.coins[0].animation.last_time, self.coins[0].animation.pointer)


    

    def update(self, deltaTime):
        temp_coins = list(self.coins)
        coin : Coin
        for coin in temp_coins:
            coin.update(deltaTime)
            if coin.collider.isCollisionWithRect(self.character.collider):
                self.coins.remove(coin)
                # add money to the player
            elif coin.collider.x < 0:
                self.coins.remove(coin)


    def draw(self, surface):
        for coin in self.coins:
            coin.draw(surface)