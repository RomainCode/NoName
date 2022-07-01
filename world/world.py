

from regex import P
from entities.coin import Coin
from world.chunckManager import ChunckManager
from ui.mainScore import MainScore
import config

import time
import random

class World:

    COIN_BATCH_SIZE = (2, 5) # minium and maximum
    COIN_SPAWN_PROPORTIONS = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
    COIN_AMOUNT = 3
    COIN_BATCH_SEPARATING_TIME = 6 # min and max

    def __init__(self, character):
        self.coins = [] # to stock later in the chunk (maybe)
        self.character = character
        self.chunck_manager = ChunckManager()
        self.last_coin_batch = 0
        self.main_score = MainScore()

    def update(self, deltaTime):
        # handle the chunks
        self.chunck_manager.update(deltaTime)

        # handle the coins
        temp_coins = list(self.coins)
        coin : Coin
        for coin in temp_coins:
            coin.update(deltaTime)
            if coin.collider.isCollisionWithRect(self.character.collider):
                self.coins.remove(coin)
                self.main_score.triggerGold()
                # add money to the player
            elif coin.collider.x < 0:
                self.coins.remove(coin)

        if len(self.coins) < World.COIN_AMOUNT and self.last_coin_batch + World.COIN_BATCH_SEPARATING_TIME < time.time():
            self.last_coin_batch = time.time()
            self.addCoinBatch()

        self.main_score.update(deltaTime)
 

    def draw(self, surface):
        for coin in self.coins:
            coin.draw(surface)
        
        self.chunck_manager.draw(surface)

        self.main_score.draw(surface)

    def addCoin(self, x, y):
        coin = Coin(x, y)
        self.coins.append(coin)
        coin.synchronize(self.coins[0].animation.last_time, self.coins[0].animation.pointer)


    def addCoinBatch(self):
        batch_size = random.choice(World.COIN_SPAWN_PROPORTIONS)
        world_x = config.WIDTH
        world_y = random.randint(1, 3)*45 + 200

        relat_pos_list = []
        while len(relat_pos_list) != batch_size:
            position = [random.randint(0, 4), random.randint(0, 4)]
            if not position in relat_pos_list:
                print(position, relat_pos_list)
                relat_pos_list.append(position)
        
        for i in range(batch_size):
            self.addCoin(relat_pos_list[i][0]*45+world_x, relat_pos_list[i][1]*45+world_y)