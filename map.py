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
blue_top_lane = MapZone("top", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 0,
    'y_min': 0,
    'y_max': 14850
})

red_top_lane = MapZone("top", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 14850,
    'y_min': 14850,
    'y_max': 14850
})

mid_lane = MapZone("mid", {
    'type': 'line',
    'equation': lambda x, y: x == y
})

blue_bot_lane = MapZone("bot", {
    'type': 'rectangle',
    'x_min': 0,
    'x_max': 14850,
    'y_min': 0,
    'y_max': 0
})

red_bot_lane = MapZone("bot", {
    'type': 'rectangle',
    'x_min': 14850,
    'x_max': 14850,
    'y_min': 0,
    'y_max': 14850
})

river = MapZone("River", {
    'type': 'line',
    'equation': lambda x, y: x + y == 14850
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

zones = [blue_top_lane, red_top_lane , mid_lane, blue_bot_lane, red_bot_lane ,river, baron_pit, dragon_pit, 
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
        center_x, center_y, radius = zone.boundaries['center']
        angle = random.uniform(0, 2 * 3.14159)  # 隨機角度
        r = radius * random.uniform(0, 1)  # 隨機半徑
        x = center_x + r * cos(angle)
        y = center_y + r * sin(angle)
        return x, y
    elif zone.boundaries['type'] == 'line':
        # 針對線型區域的隨機點生成，這裡假設y是x的函數
        if 'equation' in zone.boundaries:
            # 隨機選取一個x值，計算相應的y值
            x = random.uniform(zone.boundaries['x_min'], zone.boundaries['x_max'])
            y = zone.boundaries['equation'](x)
            return x, y
    return None

# 隨機選擇一個區域並生成隨機點
# random_zone = random.choice(zones)
# random_point = generate_random_point_in_zone(random_zone)