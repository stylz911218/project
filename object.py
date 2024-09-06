import numpy as np

# 主堡
class home:
    def __init__(self, hitable, hp) -> None:
        self.hitable = hitable
        self.hp = hp

# 防禦塔
class turret:
    def __init__(self, hitable, hp, damage) -> None:
        self.hitable = hitable
        self.hp = hp
        self.damage = damage

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
        self.hp = None
        self.mana = None
        self.position = position
        self.correctsummoners = correctsummoners

        self.summoners = []

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

    # TODO
    # 狀態評分
    def state_value(self, hp_now, mana_now, playstyle, keyitem, keystone, current_location, summoners1_, summoners2_,):
        hp = hp_now / self.hp
        mana = mana_now / self.mana
        if playstyle == 0: # ad, use aa
            value = hp * 80 + mana * 20
        elif playstyle == 1: # ad, use skills
            value = hp * 60 + mana * 40
        elif playstyle == 2: # ap
            value = hp * 40 + mana * 60

        for it in self.item:
            if it == keyitem:
                value += 40

        # TODO  
        # if keystone == self.correctkeystone:
        #     value += 20
        
        if 0 < abs(current_location - self.position) <= 1:
            value += self.team * 30
        elif 1 < abs(current_location - self.position) <= 2.7:
            value += self.team * 15
        elif 2.7 < abs(current_location - self.position) and ((self.summoners1 == 6 and summoners1_) or (self.summoners2 == 6 and summoners2_)):
            value += self.team * 20


        return value

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
