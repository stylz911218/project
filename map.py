import random
from math import cos, sin, pi

class MapZone:
    def __init__(self, name, boundaries):
        self.name = name
        self.boundaries = boundaries  # boundaries 是一個字典，包含座標範圍

    def contains_point(self, x, y):
        # 檢查點 (x, y) 是否在該區域內
        if self.boundaries['type'] == 'rectangle':
            return (self.boundaries['x_min'] <= x <= self.boundaries['x_max'] and
                    self.boundaries['y_min'] <= y <= self.boundaries['y_max'])
        elif self.boundaries['type'] == 'line':
            return self.boundaries['equation'](x, y)
        elif self.boundaries['type'] == 'circle':
            center_x, center_y, radius = self.boundaries['center']
            return (x - center_x)**2 + (y - center_y)**2 <= radius**2

# 定義各區域
blue_top_lane = MapZone("Blue Top Lane", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 0,
    'y_min': 0,
    'y_max': 14850
})

red_top_lane = MapZone("Red Top Lane", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 14850,
    'y_min': 14850,
    'y_max': 14850
})

# 定義mid lane的分割點
mid_cutoff = 7425  # 這是中間點，大約是地圖正中央

# 藍方中路區域，x == y 且 x <= mid_cutoff
blue_mid_lane = MapZone("Blue Mid Lane", {
    'type': 'line',
    'equation': lambda x: x,  # 因為 x == y，所以 y 直接等於 x
    'x_min': 0,
    'x_max': mid_cutoff  # 最大值為分割點
})

# 紅方中路區域，x == y 且 x >= mid_cutoff
red_mid_lane = MapZone("Red Mid Lane", {
    'type': 'line',
    'equation': lambda x: x,  # 因為 x == y，所以 y 直接等於 x
    'x_min': mid_cutoff,
    'x_max': 14850  # 最大值為地圖最大值
})

blue_bot_lane = MapZone("Blue Bot Lane", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 14850,
    'y_min': 0,
    'y_max': 0
})

red_bot_lane = MapZone("Red Bot Lane", {
    'type': 'rectangle',
    'x_min': 14850,
    'x_max': 14850,
    'y_min': 0,
    'y_max': 14850
})

upper_river = MapZone("Upper River", {
    'type': 'line',
    'equation': lambda x: 14850 - x,  # 根據 x 計算 y 值
    'x_min': 0,
    'x_max': mid_cutoff
})

lower_river = MapZone("Lower River", {
    'type': 'line',
    'equation': lambda x: 14850 - x,  # 根據 x 計算 y 值
    'x_min': mid_cutoff,
    'x_max': 14850
})

baron_pit = MapZone("Baron Pit", {
    'type': 'circle',
    'center': (4500, 9500),
    'radius': 1000
})

dragon_pit = MapZone("Dragon Pit", {
    'type': 'circle',
    'center': (9500, 4500),
    'radius': 1000
})

# 定義野區
upper_blue_jungle = MapZone("Upper Blue Jungle", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 7400,
    'y_min': 7400,
    'y_max': 14850
})

lower_blue_jungle = MapZone("Lower Blue Jungle", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 7400,
    'y_min': 0,
    'y_max': 7400
})

upper_red_jungle = MapZone("Upper Red Jungle", {
    'type': 'rectangle',
    'x_min': 7400,
    'x_max': 14850,
    'y_min': 7400,
    'y_max': 14850
})

lower_red_jungle = MapZone("Lower Red Jungle", {
    'type': 'rectangle',
    'x_min': 7400,
    'x_max': 14850,
    'y_min': 0,
    'y_max': 7400
})

zones = [blue_top_lane, red_top_lane , blue_mid_lane, red_mid_lane, blue_bot_lane, red_bot_lane ,upper_river, lower_river, baron_pit, dragon_pit, 
             upper_blue_jungle, lower_blue_jungle, upper_red_jungle, lower_red_jungle]

# 檢查某個點是否在某個區域內
def check_point_in_zones(x, y):
    for zone in zones:
        if zone.contains_point(x, y):
            print(f"Point ({x}, {y}) is in {zone.name}")

def generate_random_point_in_zone(zone):
    if zone.boundaries['type'] == 'rectangle':
        x = random.uniform(zone.boundaries['x_min'], zone.boundaries['x_max'])
        y = random.uniform(zone.boundaries['y_min'], zone.boundaries['y_max'])
        return x, y
    elif zone.boundaries['type'] == 'circle':
        center_x, center_y = zone.boundaries['center']
        radius = zone.boundaries['radius']
        angle = random.uniform(0, 2 * pi)  # 隨機角度
        r = radius * random.uniform(0, 1)  # 隨機半徑
        x = center_x + r * cos(angle)
        y = center_y + r * sin(angle)
        return x, y
    elif zone.boundaries['type'] == 'line':
        # 針對線型區域的隨機點生成，這裡假設x是隨機，y根據equation計算
        x = random.uniform(zone.boundaries['x_min'], zone.boundaries['x_max'])
        y = zone.boundaries['equation'](x)  # 根據x計算y
        return x, y
    return None
# 隨機選擇一個區域並生成隨機點
# random_zone = random.choice(zones)
# random_point = generate_random_point_in_zone(random_zone)

# 根據不同的時間段，定義可能出現的區域並分配權重
# 上路
def top_get_zones_and_weights_for_time(time, side, jungle_zone, drake_count, enemy_drake_count, baron_alive, baron_killed_by, elder_alive, elder_killed_by, player_or_not):
    if side == 1: # 藍
        if time <= 6:
            current_zones = [blue_top_lane]
            weights = [1]
        elif 6 < time <= 10:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [blue_top_lane, baron_pit]
                weights = [0.65, 0.35]
            else:
                current_zones = [blue_top_lane]
                weights = [1]
        elif 10 < time < 14:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [blue_top_lane, baron_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [blue_top_lane]
                weights = [1]
        elif 14 <= time < 20:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [blue_top_lane, baron_pit]
                weights = [0.6, 0.4]
            else:
                current_zones = [blue_top_lane]
                weights = [1]
        elif 20 <= time:
            # if mid_zone == blue_bot_lane:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.5, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [blue_top_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [blue_top_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [blue_top_lane, dragon_pit]
                weights = [0.55, 0.45]
            else:
                current_zones = [blue_top_lane]
                weights = [0.75]
            # else:
            #     if jungle_zone == baron_pit:
            #         current_zones = [blue_bot_lane, baron_pit]
            #         weights = [0.6, 0.4]
            #     elif jungle_zone == dragon_pit and drake_count < 3:
            #         current_zones = [blue_bot_lane, dragon_pit]
            #         weights = [0.7, 0.3]
            #     elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
            #         current_zones = [blue_bot_lane, dragon_pit]
            #         weights = [0.55, 0.45]
            #     else:
            #         current_zones = [blue_bot_lane]
            #         weights = [0.75]
    
    else: # 紅
        if time <= 6:
            current_zones = [red_top_lane]
            weights = [1]
        elif 6 < time <= 10:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [red_top_lane, baron_pit]
                weights = [0.65, 0.35]
            else:
                current_zones = [red_top_lane]
                weights = [1]
        elif 10 < time < 14:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [red_top_lane, baron_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_top_lane]
                weights = [1]
        elif 14 <= time < 20:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [red_top_lane, baron_pit]
                weights = [0.6, 0.4]
            else:
                current_zones = [red_top_lane]
                weights = [1]
        elif 20 <= time:
            # if mid_zone == blue_bot_lane:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [red_top_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [red_top_lane, dragon_pit]
                weights = [0.55, 0.45]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [red_top_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_top_lane]
                weights = [0.75]
            # else:
            # if jungle_zone == baron_pit:
            #     current_zones = [red_bot_lane, baron_pit]
            #     weights = [0.6, 0.4]
            # elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
            #     current_zones = [red_bot_lane, dragon_pit]
            #     weights = [0.55, 0.45]
            # elif jungle_zone == dragon_pit and drake_count < 3:
            #     current_zones = [red_bot_lane, dragon_pit]
            #     weights = [0.7, 0.3]
            # else:
            #     current_zones = [red_bot_lane]
            #     weights = [0.75]
    return current_zones, weights

# 中路
def mid_get_zones_and_weights_for_time(time, side, jungle_zone, drake_count, enemy_drake_count, baron_alive, baron_killed_by, elder_alive, elder_killed_by, player_or_not):
    if side == 1: # 藍
        if time <= 6:
            current_zones = [blue_mid_lane]
            weights = [1]
        elif 6 < time <= 10:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [blue_mid_lane, baron_pit]
                weights = [0.65, 0.35]
            else:
                current_zones = [blue_mid_lane]
                weights = [1]
        elif 10 < time < 14:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [blue_mid_lane, baron_pit]
                weights = [0.65, 0.35]
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_mid_lane, dragon_pit]
                weights = [0.65, 0.35]
            else:
                current_zones = [blue_mid_lane]
                weights = [1]
        elif 14 <= time < 20:
            if jungle_zone == baron_pit: # 先鋒
                current_zones = [blue_bot_lane, baron_pit, blue_mid_lane]
                weights = [0.45, 0.45, 0.1]
            else:
                current_zones = [blue_bot_lane]
                weights = [1]
        elif 20 <= time:
            # if top_zone == blue_bot_lane:
            #     if jungle_zone == baron_pit:
            #         current_zones = [blue_top_lane, baron_pit]
            #         weights = [0.6, 0.4]
            #     elif jungle_zone == dragon_pit and drake_count < 3:
            #         current_zones = [blue_top_lane, dragon_pit]
            #         weights = [0.7, 0.3]
            #     elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
            #         current_zones = [blue_top_lane, dragon_pit]
            #         weights = [0.55, 0.45]
            #     else:
            #         current_zones = [blue_top_lane]
            #         weights = [0.75]
            # else:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.5, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [blue_bot_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [blue_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [blue_bot_lane, dragon_pit]
                weights = [0.55, 0.45]
            else:
                current_zones = [blue_bot_lane]
                weights = [0.75]
    
    else: # 紅
        if time <= 6:
            current_zones = [red_mid_lane]
            weights = [1]
        elif 6 < time <= 10:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [red_mid_lane, baron_pit]
                weights = [0.65, 0.35]
            else:
                current_zones = [red_mid_lane]
                weights = [1]
        elif 10 < time < 14:
            if jungle_zone == baron_pit: # 巢蟲
                current_zones = [red_mid_lane, baron_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_mid_lane]
                weights = [1]
        elif 14 <= time < 20:
            if jungle_zone == baron_pit: # 先鋒
                current_zones = [red_bot_lane, baron_pit, red_mid_lane]
                weights = [0.45, 0.45, 0.1]
            else:
                current_zones = [red_bot_lane]
                weights = [1]
        elif 20 <= time:
            # if top_zone == blue_bot_lane:
            #     if jungle_zone == baron_pit:
            #         current_zones = [red_top_lane, baron_pit]
            #         weights = [0.6, 0.4]
            #     elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
            #         current_zones = [red_top_lane, dragon_pit]
            #         weights = [0.55, 0.45]
            #     elif jungle_zone == dragon_pit and drake_count < 3:
            #         current_zones = [red_top_lane, dragon_pit]
            #         weights = [0.7, 0.3]
            #     else:
            #         current_zones = [red_top_lane]
            #         weights = [0.75]
            # else:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [red_bot_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [red_bot_lane, dragon_pit]
                weights = [0.55, 0.45]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [red_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_bot_lane]
                weights = [0.75]
    return current_zones, weights

# 下路
def bot_get_zones_and_weights_for_time(time, side, jungle_zone, drake_count, enemy_drake_count, baron_alive, baron_killed_by, elder_alive, elder_killed_by, player_or_not):
    if side == 1:
        if time < 5:
            current_zones = [blue_bot_lane]
            weights = [1]
        elif 5 <= time < 6:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [blue_bot_lane]
                weights = [1]
        elif 6 <= time < 10:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [blue_bot_lane]
                weights = [1]
        elif 10 <= time < 20:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_mid_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == baron_pit and time < 14:
                current_zones = [blue_mid_lane, baron_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == baron_pit:
                current_zones = [blue_mid_lane, baron_pit]
                weights = [0.6, 0.4]
            else:
                current_zones = [blue_mid_lane]
                weights = [1]
        elif 20 <= time:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.5, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [blue_mid_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [blue_mid_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [blue_mid_lane, dragon_pit]
                weights = [0.55, 0.45]
            else:
                current_zones = [blue_mid_lane]
                weights = [0.75]
    else:
        if time < 5:
            current_zones = [red_bot_lane]
            weights = [1]
        elif 5 <= time < 6:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [red_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_bot_lane]
                weights = [1]
        elif 6 <= time < 10:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [red_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_bot_lane]
                weights = [1]
        elif 10 <= time < 20:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [red_mid_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == baron_pit and time < 14:
                current_zones = [red_mid_lane, baron_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == baron_pit:
                current_zones = [red_mid_lane, baron_pit]
                weights = [0.6, 0.4]
            else:
                current_zones = [red_mid_lane]
                weights = [1]
        elif 20 <= time:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [red_mid_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [red_mid_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [red_mid_lane, dragon_pit]
                weights = [0.55, 0.45]
            else:
                current_zones = [red_mid_lane]
                weights = [0.75]
    return current_zones, weights

# 輔助
def sup_get_zones_and_weights_for_time(time, side, jungle_zone, drake_count, enemy_drake_count, baron_alive, baron_killed_by, elder_alive, elder_killed_by, player_or_not):
    if side == 1:
        if time < 5:
            current_zones = [blue_bot_lane]
            weights = [1]
        elif 5 <= time < 6:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [blue_bot_lane]
                weights = [1]
        elif 6 <= time < 10:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == baron_pit: # 巢蟲
                current_zones = [blue_bot_lane, baron_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [blue_bot_lane]
                weights = [1]
        elif 10 <= time < 20:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [blue_mid_lane, dragon_pit, lower_blue_jungle, lower_red_jungle]
                weights = [0.55, 0.3, 0.1, 0.05]
            elif jungle_zone == baron_pit and time < 14:
                current_zones = [blue_mid_lane, baron_pit, upper_blue_jungle, upper_red_jungle]
                weights = [0.55, 0.3, 0.1, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [blue_mid_lane, baron_pit, upper_blue_jungle, upper_red_jungle]
                weights = [0.3, 0.4, 0.2 , 0.1]
            else:
                current_zones = [blue_mid_lane, upper_river, lower_river, lower_blue_jungle, upper_blue_jungle, lower_red_jungle, upper_red_jungle]
                weights = [0.85, 0.05, 0.05, 0.02, 0.02, 0.005, 0.005]
        elif 20 <= time:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.5, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [blue_mid_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [blue_mid_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [blue_mid_lane, dragon_pit]
                weights = [0.55, 0.45]
            else:
                current_zones = [blue_mid_lane, upper_river, lower_river, lower_blue_jungle, upper_blue_jungle, lower_red_jungle, upper_red_jungle]
                weights = [0.3, 0.15, 0.15, 0.1, 0.1, 0.05, 0.05]
    else:
        if time < 5:
            current_zones = [red_bot_lane]
            weights = [1]
        elif 5 <= time < 6:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [red_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_bot_lane]
                weights = [1]
        elif 6 <= time < 10:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [red_bot_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == baron_pit: # 巢蟲
                current_zones = [red_bot_lane, baron_pit]
                weights = [0.7, 0.3]
            else:
                current_zones = [red_bot_lane]
                weights = [1]
        elif 10 <= time < 20:
            if jungle_zone == dragon_pit: # 小龍
                current_zones = [red_mid_lane, dragon_pit, lower_blue_jungle, lower_red_jungle]
                weights = [0.55, 0.3, 0.1, 0.05]
            elif jungle_zone == baron_pit and time < 14:
                current_zones = [red_mid_lane, baron_pit, upper_blue_jungle, upper_red_jungle]
                weights = [0.55, 0.3, 0.1, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [red_mid_lane, baron_pit, upper_blue_jungle, upper_red_jungle]
                weights = [0.3, 0.4, 0.2 , 0.1]
            else:
                current_zones = [red_mid_lane, upper_river, lower_river, lower_blue_jungle, upper_blue_jungle, lower_red_jungle, upper_red_jungle]
                weights = [0.85, 0.05, 0.05, 0.02, 0.02, 0.005, 0.005]
        elif 20 <= time:
            if (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif jungle_zone == baron_pit:
                current_zones = [red_mid_lane, baron_pit]
                weights = [0.6, 0.4]
            elif jungle_zone == dragon_pit and drake_count < 3:
                current_zones = [red_mid_lane, dragon_pit]
                weights = [0.7, 0.3]
            elif jungle_zone == dragon_pit and (drake_count == 3 or enemy_drake_count == 3):
                current_zones = [red_mid_lane, dragon_pit]
                weights = [0.55, 0.45]
            else:
                current_zones = [red_mid_lane, upper_river, lower_river, lower_blue_jungle, upper_blue_jungle, lower_red_jungle, upper_red_jungle]
                weights = [0.3, 0.15, 0.15, 0.1, 0.1, 0.05, 0.05]
    return current_zones, weights

# 打野
def jg_get_zones_and_weights_for_time(time, side, drake_count, enemy_drake_count, grub_slain_by, drake_alive, grubs_alive, herald_alive, baron_alive, baron_killed_by, elder_alive, elder_killed_by, player_or_not):
    if side == 1:
        if time < 5:
            current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
            weights = [0.4, 0.4, 0.015, 0.015, 0.01, 0.01, 0.05, 0.05, 0.05]
        elif 5 <= time < 6:
            if drake_alive:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.02, 0.02, 0.02, 0.02, 0.06, 0.02, 0.02, 0.02]
            else:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.015, 0.015, 0.01, 0.01, 0.05, 0.05, 0.05]
        elif 6 <= time < 14:
            if grubs_alive:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, baron_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.01, 0.01, 0.01, 0.01, 0.1, 0.02, 0.02, 0.02]
            elif drake_alive:
                if (grub_slain_by == "enemy" and player_or_not) or (grub_slain_by == "ally" and not player_or_not):
                    current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                    weights = [0.4, 0.4, 0.01, 0.01, 0.01, 0.01, 0.1, 0.02, 0.02, 0.02]
                else:
                    current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                    weights = [0.4, 0.4, 0.02, 0.02, 0.02, 0.02, 0.06, 0.02, 0.02, 0.02]
            else:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.015, 0.015, 0.01, 0.01, 0.05, 0.05, 0.05]
        elif 14 <= time < 20:
            if herald_alive:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, baron_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.2, 0.2, 0.015, 0.005, 0.01, 0.01, 0.53, 0.01, 0.01, 0.01]
            elif drake_alive:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.2, 0.2, 0.025, 0.015, 0.02, 0.02, 0.49, 0.01, 0.01, 0.01]
            else:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.01, 0.01, 0.015, 0.015, 0.01, 0.13, 0.01]
        elif 20 <= time:
            if elder_alive: # 遠古龍活著
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit]
                weights = [0.1, 0.1, 0.005, 0.015, 0.01, 0.01, 0.76]
                return current_zones, weights
            elif (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
                return current_zones, weights

            possible = 0
            if baron_alive and drake_alive:
                possible = random.choice((0,1))
            
            if time > 30:
                possible = 1 # 必須考慮巴龍優先

            if possible and time >= 25: # 巴龍活著
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, baron_pit]
                weights = [0.1, 0.1, 0.015, 0.005, 0.01, 0.01, 0.76]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [blue_bot_lane, blue_mid_lane, blue_top_lane ,lower_blue_jungle, upper_blue_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif not possible:
                if enemy_drake_count == 3 or drake_count == 3:
                    current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit]
                    weights = [0.1, 0.1, 0.005, 0.015, 0.01, 0.01, 0.76]
                else:
                    current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle, dragon_pit]
                    weights = [0.15, 0.15, 0.02, 0.05, 0.01, 0.01, 0.61]
            else:
                current_zones = [upper_blue_jungle, lower_blue_jungle, upper_river, lower_river, upper_red_jungle, lower_red_jungle]
                weights = [0.45, 0.45, 0.04, 0.04, 0.01, 0.01]
    else:
        if time < 5:
            current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
            weights = [0.4, 0.4, 0.015, 0.015, 0.01, 0.01, 0.05, 0.05, 0.05]
        elif 5 <= time < 6:
            if drake_alive:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.02, 0.02, 0.02, 0.02, 0.06, 0.02, 0.02, 0.02]
            else:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.015, 0.015, 0.01, 0.01, 0.05, 0.05, 0.05]
        elif 6 <= time < 14:
            if grubs_alive:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, baron_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.01, 0.01, 0.01, 0.01, 0.1, 0.02, 0.02, 0.02]
            elif drake_alive:
                if (grub_slain_by == "enemy" and player_or_not) or (grub_slain_by == "ally" and not player_or_not):
                    current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                    weights = [0.4, 0.4, 0.01, 0.01, 0.01, 0.01, 0.1, 0.02, 0.02, 0.02]
                else:
                    current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                    weights = [0.4, 0.4, 0.02, 0.02, 0.02, 0.02, 0.06, 0.02, 0.02, 0.02]
            else:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.015, 0.015, 0.01, 0.01, 0.05, 0.05, 0.05]
        elif 14 <= time < 20:
            if herald_alive:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, baron_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.2, 0.2, 0.015, 0.005, 0.01, 0.01, 0.53, 0.01, 0.01, 0.01]
            elif drake_alive:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.2, 0.2, 0.025, 0.015, 0.02, 0.02, 0.49, 0.01, 0.01, 0.01]
            else:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, blue_mid_lane, blue_bot_lane, blue_top_lane]
                weights = [0.4, 0.4, 0.01, 0.01, 0.015, 0.015, 0.01, 0.13, 0.01]
        elif 20 <= time:
            if elder_alive: # 遠古龍活著
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit]
                weights = [0.1, 0.1, 0.005, 0.015, 0.01, 0.01, 0.76]
                return current_zones, weights
            elif (not elder_alive and elder_killed_by == "enemy" and player_or_not) or (not elder_alive and elder_killed_by == "ally" and not player_or_not): # 遠古龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
                return current_zones, weights
            
            possible = 0
            if baron_alive and drake_alive:
                possible = random.choice((0,1))
            
            if time > 30:
                possible = 1 # 必須考慮巴龍優先

            if possible: # 巴龍活著
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, baron_pit]
                weights = [0.1, 0.1, 0.015, 0.005, 0.01, 0.01, 0.76]
            elif (not baron_alive and baron_killed_by == "enemy" and player_or_not) or (not baron_alive and baron_killed_by == "ally" and not player_or_not): # 巴龍被對面吃掉
                weights = [red_bot_lane, red_mid_lane, red_top_lane ,upper_red_jungle, lower_red_jungle]
                weights = [0.3, 0.3, 0.3, 0.05, 0.05]
            elif not possible:
                if enemy_drake_count == 3 or drake_count == 3:
                    current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit]
                    weights = [0.1, 0.1, 0.005, 0.015, 0.01, 0.01, 0.76]
                else:
                    current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle, dragon_pit]
                    weights = [0.15, 0.15, 0.02, 0.05, 0.01, 0.01, 0.61]
            else:
                current_zones = [upper_red_jungle, lower_red_jungle, upper_river, lower_river, upper_blue_jungle, lower_blue_jungle]
                weights = [0.45, 0.45, 0.04, 0.04, 0.01, 0.01]
    return current_zones, weights