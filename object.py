import numpy as np
import random

# 主堡
class home:
    def __init__(self, hitable, hp) -> None:
        self.hitable = hitable
        self.hp = hp

# 防禦塔
class turret:
    def __init__(self, hitable, hp) -> None:
        self.hitable = hitable
        self.hp = hp

# 兵營
class inhibitor:
    def __init__(self, hitable, hp) -> None:
        self.hitable = hitable
        self.hp = hp

# 英雄
class champion:
    def __init__(self, name, correctkeystone, position, correctsummoners) -> None:
        self.item = []
        self.name = name
        self.correctkeystone = correctkeystone
        self.hp = -1
        self.mana = -1
        self.position = position
        self.correctsummoners = correctsummoners

        self.summoners = []

        self.value = 0

        # 風格
        self.style = None

    # 當前藍 血總量
    def hp_mana_now(self, current_hp, current_mana):
        self.hp = current_hp
        self.mana = current_mana
    
    # 裝備輸入
    def item_now(self, current_item):
        self.item = current_item

    # 召喚師技能輸入
    def summoners_now(self, current_summoners):
        self.summoners = current_summoners

    # 隊伍
    def team_now(self, ally):
        self.team = ally

    # 當前福文
    def keystone_now(self, currentkeystone):
        self.keystone = currentkeystone

    # 紅 or 藍, 紅 = -1, 藍 = 1
    def red_or_blue(self, side):
        self.side = side

    # 現在位置
    def current_place(self, zone, location):
        self.zone = zone
        self.location = location

    # 狀態評分
    def state_value(self, hp_now, mana_now ,summoners1_, summoners2_):

        # 針對目前狀態
        if self.mana == -1 and self.hp == -1: # random
            if self.name == "Renecton" or self.name == "Gnar":
                hp = random.uniform(0, 100)
                mana = random.uniform(0, 100) # 在這裡是怒氣值==
                self.value = hp * 0.5 + mana * 0.5
            if self.name == "Aatrox" or self.name == "Rumble" or self.name == "Garen" or self.name == "Sett" or self.name == "Tryndamere" or self.name == "Kled" or self.name == "Zac" or self.name == "Yone" or self.name == "Mordekaiser" or self.name == "Raven" or self.name == "Vladimir" or self.name == "Reksai" or self.name == "Belveth" or self.name == "Yassuo" or self.name == "Viego" or self.name == "Katerina" or self.name == "Briar" or self.name == "Rengar":
                hp = random.uniform(0, 100) # 這些逼沒有魔力==
                self.value = hp * 1
            else:
                hp = random.uniform(0, 100)
                mana = random.uniform(0, 100)
                self.value = hp * 0.55 + mana * 0.45
        else: # with record
            hp = hp_now / self.hp
            mana = mana_now / self.mana
            if self.name == "Renecton" or self.name == "Gnar":
                hp = hp_now / self.hp
                mana = mana_now / 100 # 在這裡是怒氣值==
                self.value = hp * 0.5 + mana * 0.5
            if self.name == "Aatrox" or self.name == "Rumble" or self.name == "Garen" or self.name == "Sett" or self.name == "Tryndamere" or self.name == "Kled" or self.name == "Zac" or self.name == "Yone" or self.name == "Mordekaiser" or self.name == "Raven" or self.name == "Vladimir" or self.name == "Reksai" or self.name == "Belveth" or self.name == "Yassuo" or self.name == "Viego" or self.name == "Katerina" or self.name == "Briar" or self.name == "Rengar":
                hp = hp_now / self.hp
                self.value = hp * 1
            else:
                hp = hp_now / self.hp
                mana = mana_now / self.mana
                self.value = hp * 0.55 + mana * 0.45


        # 召喚師技能
        if set(self.summoners).issubset(set(self.correctsummoners)):
            self.value += 10

        # 核心符文
        if set(self.keystone).issubset(set(self.correctkeystone)):
            self.value += 10
    
    # 位置評分
    def location_value(self, player_location, player):
        if player:
            return

        # 基本距離計算
        distance = ((self.location[0] - player_location[0])**2 + (self.location[1] - player_location[1])**2)**0.5
        max_distance = 14850 * 2 ** 0.5  # 假設地圖的對角線最大距離
        distance_score = (max_distance - distance) / max_distance  # 距離越近，分數越高

        self.value += (distance_score) * 100

    def final_value(self, player, player_location, hp_now, mana_now ,summoners1_, summoners2_):
        self.location_value(player=player, player_location=player_location)
        
        self.state_value(hp_now, mana_now ,summoners1_, summoners2_)

        self.alive = random.randint(0,1)

        if not self.alive:
            self.value -= 1000 
        
        
        self.value = self.value * self.team



# 小型野怪
class camp:
    def __init__(self, alive, respawn_countdown, value, enemycamp) -> None:
        self.alive = alive
        self.value = value
        if self.alive == 0:
            self.respawn_countdown = respawn_countdown
        elif self.alive == -2:
            self.respawn_countdown = -2
        else:
            self.respawn_countdown = 0
        self.enemycamp = enemycamp

# 大型野怪
class largecamp:
    def __init__(self, alive, buff, respawn_countdown, value) -> None:
        self.alive = alive
        self.buff = buff
        self.value = value
        if not self.alive:
            self.respawn_countdown = respawn_countdown
        else:
            self.respawn_countdown = -1
