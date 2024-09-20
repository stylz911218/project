from object import home, turret, camp, champion, inhibitor, largecamp
from Champions import top_champions, ad_champions, mid_champions, jungle_champions, support_champions, jungle_Lillia, jungle_Leesin, jungle_Khazix
import random

# action space: 0 =  scuttler, 1 = drake, 2 = grubs, 3 = herald, 4 = baron, 5 = elder, 6 = clean own jungle, 7 = invade enemy jungle
action_space = ["take scuttler", "take drake", "take grubs", "take herald", "take baron", "take elder", "clean own jungle", "invade enemy jungle"]

# globals
draketype = ["ocean", "mountain", "cloud", "chemtech", "hextech", "infernal"]

summoners_spell = ["heal", "ghost", "barrier", "exhaust", "clarity", "flash", "tp", "smite", "cleanse", "ignite"]

# position: mid = 0, top = -2, bot lane = 2, own jungle = 1, enemy jungle = 1.5, drake and baron pool = 1.2
locations = {
    "mid_lane": 0,
    "top_lane": -2,
    "bottom_lane": 2,
    "ally_top_jungle": -1,
    "ally_bot_jungle": 1,
    "enemy_top_jungle": -1.5,
    "enemy_bot_jungle": 1.5,
    "drake_pit": 1.2,
    "baron_pit": -1.2
}

# 當前時間 (先嘗試隨機生成，後續可以進行更改)
def generate_random_game_time():
    total_seconds = random.randint(0, 3600)  
    minutes, seconds = divmod(total_seconds, 60)  
    return f'{minutes:02d}:{seconds:02d}', total_seconds

# 獲取最後一條小龍被擊殺的時間
def get_last_drake_time(current_game_seconds, drakecount, drakes):
    if drakecount < 4 or current_game_seconds < 1200:
        return None, None  # 未達成擊殺四條小龍
    # 確保最後一條小龍的擊殺時間合理
    last_drake = drakes[-1]
    last_drake_time = last_drake["time"]
    last_drake_seconds = int(last_drake_time[0:2]) * 60 + int(last_drake_time[3:5])
    minutes, seconds = divmod(last_drake_seconds, 60)
    return f'{minutes:02d}:{seconds:02d}', last_drake_seconds

# 生成小龍信息
def generate_drake_info(drakecount, current_game_seconds):
    if drakecount == 0:
        return []

    drakes = []
    last_drake_time = 0
    ally_drake_count = 0
    enemy_drake_count = 0

    for i in range(drakecount):
        if i == 0:
            drake_type = random.randint(0, 5)
        elif i == 1:
            while True:
                drake_type = random.randint(0, 5)
                if drake_type != drakes[0]["type"]:
                    break
        elif i == 2:
            while True:
                drake_type = random.randint(0, 5)
                if drake_type != drakes[0]["type"] and drake_type != drakes[1]["type"]:
                    break
        else:
            drake_type = drakes[2]["type"]

        # 確保小龍的擊殺時間合理
        min_drake_time = last_drake_time + 330  # 每條小龍至少5分鐘間隔
        remaining_drakes = drakecount - i
        max_drake_time = current_game_seconds - (remaining_drakes - 1) * 320  # 確保剩餘小龍有足夠時間生成

        if min_drake_time > max_drake_time:
            drake_time = current_game_seconds - (remaining_drakes - 1) * 300
        else:
            drake_time = random.randint(min_drake_time, max_drake_time)

        minutes, seconds = divmod(drake_time, 60)
        slain_by = random.choice(["ally", "enemy"])
        
        # 更新累計擊殺數
        if slain_by == "ally":
            ally_drake_count += 1
        else:
            enemy_drake_count += 1
        
        # 如果尚未達到四條小龍的擊殺數量，則繼續生成
        if ally_drake_count < 4 and enemy_drake_count < 4:
            drakes.append({"time": f'{minutes:02d}:{seconds:02d}', "type": drake_type, "slain_by": slain_by})
            last_drake_time = drake_time
        elif ally_drake_count == 4 or enemy_drake_count == 4:
            # 如果已經有一方達成四條小龍的擊殺，確保最後一條小龍由達成四條的隊伍擊殺
            if ally_drake_count == 4:
                # 確保最後一條小龍是由友軍擊殺
                drakes.append({"time": f'{minutes:02d}:{seconds:02d}', "type": drake_type, "slain_by": "ally"})
            elif enemy_drake_count == 4:
                # 確保最後一條小龍是由敵軍擊殺
                drakes.append({"time": f'{minutes:02d}:{seconds:02d}', "type": drake_type, "slain_by": "enemy"})
            break  # 停止生成後續小龍

    return drakes

# 計算龍數量
def analyze_drakes(drakes):
    ally_drake_count = 0
    enemy_drake_count = 0

    for drake in drakes:
        if drake["slain_by"] == "ally":
            ally_drake_count += 1
        elif drake["slain_by"] == "enemy":
            enemy_drake_count += 1

    # 判斷遠古巨龍是否已經生成
    ancient_dragon_generated = (ally_drake_count >= 4 or enemy_drake_count >= 4)
    
    return ancient_dragon_generated, ally_drake_count, enemy_drake_count

# 敵軍資料
# 角色
def generate_ally_champions():
    ally_top = random.choice(top_champions)
    ally_mid = random.choice(mid_champions)
    ally_bot = random.choice(ad_champions)
    ally_sup = random.choice(support_champions)
    return ally_top, ally_mid, ally_bot, ally_sup

def generate_player_champion():
    player = random.choice((jungle_Lillia, jungle_Leesin, jungle_Khazix))
    return player

def generate_enemy_champions(ally_top, player, ally_mid, ally_bot, ally_sup):
    enemy_top = random.choice(top_champions)
    while enemy_top.name == ally_top.name or enemy_top.name == player.name or enemy_top.name == ally_mid.name or enemy_top.name == ally_bot.name or enemy_top.name == ally_sup.name:
        enemy_top = random.choice(top_champions)

    enemy_jg = random.choice(jungle_champions)
    while enemy_jg.name == ally_top.name or enemy_jg.name == player.name or enemy_jg.name == ally_mid.name or enemy_jg.name == ally_bot.name or enemy_jg.name == ally_sup.name:
        enemy_jg = random.choice(jungle_champions)
    
    enemy_mid = random.choice(mid_champions)
    while enemy_mid.name == ally_top.name or enemy_mid.name == player.name or enemy_mid.name == ally_mid.name or enemy_mid.name == ally_bot.name or enemy_mid.name == ally_sup.name:
        enemy_mid = random.choice(mid_champions)

    enemy_bot = random.choice(ad_champions)
    while enemy_bot.name == ally_top.name or enemy_bot.name == player.name or enemy_bot.name == ally_mid.name or enemy_bot.name == ally_bot.name or enemy_bot.name == ally_sup.name:
        enemy_bot = random.choice(ad_champions)

    enemy_sup = random.choice(support_champions)
    while enemy_sup.name == ally_top.name or enemy_sup.name == player.name or enemy_sup.name == ally_mid.name or enemy_sup.name == ally_bot.name or enemy_sup.name == ally_sup.name:
        enemy_sup = random.choice(support_champions)

    return enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup

def enemy():
    pass

# 防禦塔
def enemyturret():
    pass

# 友軍資料
# 角色
def ally():
    pass

# 防禦塔
def allyturret():
    pass

# 玩家資料
def player():
    pass

# 中立資源
def junglecamp(time, drakecount, drakes):
    
    # 小型野怪
    # done

    # krug 109
    allykrug_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 102:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 102 - timenow
        minutes, seconds = divmod(respawn, 60)
        allykrug = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=109, enemycamp=0)
    elif allykrug_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        allykrug = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=109, enemycamp=0)
    elif allykrug_alive == 1:
        allykrug = camp(alive=1, respawn_countdown=0, value=109, enemycamp=0)
    else:
        allykrug = camp(alive=-2, respawn_countdown=0, value=109, enemycamp=0)

    enemykrug_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 102 - timenow
        minutes, seconds = divmod(respawn, 60)
        enemykrug = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=109, enemycamp=1)
    elif enemykrug_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        enemykrug = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=109, enemycamp=1)
    elif enemykrug_alive == 1:
        enemykrug = camp(alive=1, respawn_countdown=0, value=109, enemycamp=1)
    else:
        enemykrug = camp(alive=-2, respawn_countdown=0, value=109, enemycamp=1)

    # raptor 75
    allyraptor_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 102:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        allyraptor = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=75, enemycamp=0)
    elif allyraptor_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        allyraptor = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=75, enemycamp=0)
    elif allyraptor_alive == 1:
        allyraptor = camp(alive=1, respawn_countdown=0, value=75, enemycamp=0)
    else:
        allyraptor = camp(alive=-2, respawn_countdown=0, value=75, enemycamp=0)
    
    enemyraptor_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        enemyraptor = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=75, enemycamp=1)
    elif enemyraptor_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        enemyraptor = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=75, enemycamp=1)
    elif enemyraptor_alive == 1:
        enemyraptor = camp(alive=1, respawn_countdown=0, value=75, enemycamp=1)
    else:
        enemyraptor = camp(alive=-2, respawn_countdown=0, value=75, enemycamp=1)

    # gromp 80
    allygromp_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 102:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 102 - timenow
        minutes, seconds = divmod(respawn, 60)
        allygromp = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=80, enemycamp=0)
    elif allygromp_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        allygromp = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=80, enemycamp=0)
    elif allygromp_alive == 1 :
        allygromp = camp(alive=1, respawn_countdown=0, value=80, enemycamp=0)
    else:
        allygromp = camp(alive=-2, respawn_countdown=0, value=80, enemycamp=0)
    
    enemygromp_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 102:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 102 - timenow
        minutes, seconds = divmod(respawn, 60)
        enemygromp = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=80, enemycamp=1)
    elif enemygromp_alive == 1:
        enemygromp = camp(alive=1, respawn_countdown=0, value=80, enemycamp=1)
    elif enemygromp_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        enemygromp = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=80, enemycamp=1)
    else:
        enemygromp = camp(alive=-2, respawn_countdown=0, value=80, enemycamp=1)

    # wolf 85
    allywolf_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        allywolf = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=85, enemycamp=0)
    elif allywolf_alive == 1:
        allywolf = camp(alive=1, respawn_countdown=0, value=85, enemycamp=0)
    elif allywolf_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        allywolf = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=85, enemycamp=0)
    else:
        allywolf = camp(alive=-2, respawn_countdown=0, value=85, enemycamp=0)
    
    enemywolf_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        enemywolf = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=85, enemycamp=1)
    elif enemywolf_alive == 1:
        enemywolf = camp(alive=1, respawn_countdown=0, value=85, enemycamp=1)
    elif enemywolf_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        enemywolf = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=85, enemycamp=1)
    else:
        enemywolf = camp(alive=-2, respawn_countdown=0, value=85, enemycamp=1)

    # blue
    allyblue_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        allyblue = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=0)
    if allyblue_alive == 1:
        allyblue = camp(alive=1, respawn_countdown=0, value=90, enemycamp=0)
    elif allyblue_alive == 0:
        respawn = random.randint(1, 300)
        minutes, seconds = divmod(respawn, 60)
        allyblue = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=0)
    else:
        allyblue = camp(alive=-2, respawn_countdown=0, value=90, enemycamp=0)
    
    enemyblue_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        enemyblue = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=1)
    elif enemyblue_alive == 1:
        enemyblue = camp(alive=1, respawn_countdown=0, value=90, enemycamp=1)
    elif enemyblue_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        enemyblue = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=1)
    else:
        enemyblue = camp(alive=-2, respawn_countdown=0, value=90, enemycamp=1)

    # red
    allyred_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        allyred = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=0)
    elif allyred_alive == 1:
        allyred = camp(alive=1, respawn_countdown=0, value=90, enemycamp=0)
    elif allyred_alive == 0:
        respawn = random.randint(1, 300)
        minutes, seconds = divmod(respawn, 60)
        allyred = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=0)
    else:
        allyred = camp(alive=-2, respawn_countdown=0, value=90, enemycamp=0)
    
    enemyred_alive = random.choice([0, 1, -2]) # -2 = killed by enemny, unknown

    if int(time[0:2]) *60 + int(time[3:5]) < 90:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 90 - timenow
        minutes, seconds = divmod(respawn, 60)
        enemyred = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=1)
    elif enemyred_alive == 1:
        enemyred = camp(alive=1, respawn_countdown=0, value=90, enemycamp=1)
    elif enemyred_alive == 0:
        respawn = random.randint(1, 135)
        minutes, seconds = divmod(respawn, 60)
        enemyred = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=90, enemycamp=1)
    else:
        enemyred = camp(alive=-2, respawn_countdown=0, value=90, enemycamp=1)

    # scuttler
    scuttler_alive = random.choice([0, 1, -2])
    player = random.randint(3,18)
    val = 55 + 2.75 * player

    if int(time[0:2]) *60 + int(time[3:5]) < 210:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 210 - timenow
        minutes, seconds = divmod(respawn, 60)
        scuttler = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=val, enemycamp=1)
    elif scuttler_alive == 1:
        scuttler = camp(alive=1, respawn_countdown=0, value=val, enemycamp=1)
    elif enemyred_alive == 0:
        respawn = random.randint(1, 150)
        minutes, seconds = divmod(respawn, 60)
        scuttler = camp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', value=val, enemycamp=1)
    else:
        scuttler = camp(alive=-2, respawn_countdown=0, value=val, enemycamp=1)
    # 大型野怪

    # drake 0
    # done
    elder_available, ally_drake_count, enemy_drake_count = analyze_drakes(drakes=drakes)
    drake_type = random.randint(0,5)
    if int(time[0:2]) < 5:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 300 - timenow
        minutes, seconds = divmod(respawn, 60)
        drake = largecamp(alive=0, respawn_countdown= f'{minutes:02d}:{seconds:02d}', buff=drake_type, value=25)
    elif int(time[0:2]) == 5 or drakecount == 0:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 300 - timenow
        minutes, seconds = divmod(respawn, 60)
        drake = largecamp(alive=1, respawn_countdown= f'{minutes:02d}:{seconds:02d}', buff=drake_type, value=25)
    else:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        last_drake_slain = drakes[-1]["time"]
        last_drake_slain_time = int(last_drake_slain[0:2]) * 60 + int(last_drake_slain[3:5])
        respawn = last_drake_slain_time + 300 - timenow
        if respawn > 0:
            alive = 0
        else:
            alive = 1
        
        if elder_available: # won't respawn
            drake = largecamp(alive=-1, respawn_countdown=0, buff=-1, value=0)
        elif alive == 1:
            if drakecount <= 2:
                for i in range(drakecount):
                    if i == 0:
                        drake_type = random.randint(0, 5)
                    elif i == 1:
                        while True:
                            drake_type = random.randint(0, 5)
                            if drake_type != drakes[0]["type"]:
                                break
                    elif i == 2:
                        while True:
                            drake_type = random.randint(0, 5)
                            if drake_type != drakes[0]["type"] and drake_type != drakes[1]["type"]:
                                break
                drake = largecamp(alive=alive, respawn_countdown=0, buff=drake_type, value=25)
            else:
                last_drake_type = drakes[-1]["type"]
                drake = largecamp(alive=alive, respawn_countdown=0, buff=last_drake_type, value=25)
        elif alive == 0:
            minutes, seconds = divmod(respawn, 60)
            if drakecount <= 2:
                for i in range(drakecount):
                    if i == 0:
                        drake_type = random.randint(0, 5)
                    elif i == 1:
                        while True:
                            drake_type = random.randint(0, 5)
                            if drake_type != drakes[0]["type"]:
                                break
                    elif i == 2:
                        while True:
                            drake_type = random.randint(0, 5)
                            if drake_type != drakes[0]["type"] and drake_type != drakes[1]["type"]:
                                break
                drake = largecamp(alive=alive, respawn_countdown= f'{minutes:02d}:{seconds:02d}', buff=drake_type, value=25)
            else:
                last_drake_type = drakes[-1]["type"]
                drake = largecamp(alive=alive, respawn_countdown= f'{minutes:02d}:{seconds:02d}', buff=last_drake_type, value=25)

    print(f'Drake info: alive = {drake.alive}, respawn = {drake.respawn_countdown}, type = {drake.buff}, value = {drake.value}')

    # grubs 1 
    # done
    if int(time[0:2]) < 6:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 360 - timenow
        minutes, seconds = divmod(respawn, 60)
        grub = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="grub", value=90)
    elif int(time[0:2]) * 60 + int(time[3:5]) > 825:
        grub = largecamp(alive=-1, respawn_countdown=0 , buff="Won't respawn", value=90)
    else:
        alive = random.choice([0, 1])
        if alive == 1:
            grub = largecamp(alive=1, respawn_countdown=0, buff="grub", value=90)
        else:
            timenow = int(time[0:2]) * 60 + int(time[3:5])
            timediff = 0
            # killed time
            killed_time = random.randint(375, timenow)
            minutes, seconds = divmod(killed_time, 60)
            print(f'First grubs were killed at {minutes:02d}:{seconds:02d}')
            if killed_time > 585: # won't respawn
                grub = largecamp(alive=-1, respawn_countdown=0, buff="Won't respawn", value=90)
            else:
                respawn = killed_time + 240
                timediff = respawn - timenow
                minutes, seconds = divmod(timediff, 60)
                grub = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="grub", value=90)
    
    print(f'Grub info: alive = {grub.alive}, respawn = {grub.respawn_countdown}, type = {grub.buff}, value = {grub.value}')

    
    # herald
    # done
    if int(time[0:2]) < 14:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 840 - timenow
        minutes, seconds = divmod(respawn, 60)
        herald = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="herald", value=600)
    elif int(time[0:2]) == 14:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 840 - timenow
        minutes, seconds = divmod(respawn, 60)
        herald = largecamp(alive=1, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="herald", value=600)
    elif int(time[0:2]) >= 20: # wont respawn
        herald = largecamp(alive=-1, respawn_countdown=0, buff="No herald", value=600)
    else:
        alive = random.choice([0, 1])
        if alive == 1:
            herald = largecamp(alive=1, respawn_countdown=0, buff="herald", value=600)
        else:
            herald = largecamp(alive=0, respawn_countdown=-1, buff="No herald", value=600) # killed

    print(f'Herald info: alive = {herald.alive}, respawn = {herald.respawn_countdown}, type = {herald.buff}, value = {herald.value}')    

    # baron
    # done
    if int(time[0:2]) < 20:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 1200 - timenow
        minutes, seconds = divmod(respawn, 60)
        baron = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="baron", value=1525)
    elif int(time[0:2]) == 20:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        respawn = 1200 - timenow
        minutes, seconds = divmod(respawn, 60)
        baron = largecamp(alive=1, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="baron", value=1525)
    else:
        alive = random.choice([0, 1])
        if alive == 1:
            baron = largecamp(alive=1, respawn_countdown=0, buff="baron", value=1525)
        else:
            timediff = 0
            while timediff < 1200:
                respawn = random.randint(1, 360)
                timenow = int(time[0:2]) * 60 + int(time[3:5])
                timediff = timenow - respawn
            minutes, seconds = divmod(respawn, 60)
            baron = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="No baron", value=1525) # killed

    print(f'Baron info: alive = {baron.alive}, respawn = {baron.respawn_countdown}, type = {baron.buff}, value = {baron.value}')

    # elder
    # done
    if not elder_available:
        elder = largecamp(alive=0, respawn_countdown=-1, buff="Won't respawn", value=1100)
    else:
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        last_drake_time, last_drake_seconds = get_last_drake_time(timenow, drakecount, drakes)
        print(f'last drake was slain at {last_drake_time}')
        elder_spawn_time = last_drake_seconds + 360  # 6 minutes after last drake
        if elder_spawn_time > timenow:
            time_until_elder = elder_spawn_time - timenow
            minutes, seconds = divmod(time_until_elder, 60)
            elder = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="Elder", value=1100)
        else:
            elder = largecamp(alive=1, respawn_countdown=0, buff="Elder", value=1100)

    print(f'Elder info: alive = {elder.alive}, respawn = {elder.respawn_countdown}, type = {elder.buff}, value = {elder.value}')

    allycamp = [allygromp, allyraptor, allyblue, allykrug, allyred, allywolf]
    enemycamp = [enemygromp, enemyraptor, enemyblue, enemykrug, enemyred, enemywolf]
    neutralcamp = [scuttler, drake, grub, herald, baron, elder]

    return allycamp, enemycamp, neutralcamp
    


# 各路兵線狀況
def minionwave():
    pass

# 可行動作
def available_actions(ally, enemy, neutral):

    actions = []
    for camp in ally:
        if camp.alive == 1:
            actions.append(6)
            break
    
    for camp in enemy:
        if camp.alive == 1:
            actions.append(7)
            break
    
    for counter in range(6):
        if neutral[counter].alive == 1:
            actions.append(counter)

    return actions

# 設計可能情況

def main():
    current_game_time, current_game_seconds = generate_random_game_time()
    print(f'Current game time: {current_game_time}')

    drakecount = 0
    temp = int(current_game_time[0:2]) // 5
    
    if temp > 7:
        drakecount = random.randint(0,7)
    else:
        drakecount = random.randint(0,temp)
    
    drakes = generate_drake_info(drakecount, current_game_seconds)
    truedrakecount = 0
    for i in drakes:
        print(i)
        truedrakecount += 1

    print(f'Drake slained: {truedrakecount}')

    ally, enemy, neutral = junglecamp(current_game_time, drakecount=truedrakecount, drakes=drakes)
    actions = available_actions(ally=ally, enemy=enemy, neutral=neutral)

    print("\n")

    print("Ally camp:")
    for i in ally:
        print(f'{i.__dict__}')


    print("Enemy camp:")
    for i in enemy:
        print(f'{i.__dict__}')

    print("\n")
    print("Actions available: ")
    for i in range(len(actions)):
        print(action_space[actions[i]])

    print("\n")

    ally_top, ally_mid, ally_bot, ally_sup = generate_ally_champions()
    player = generate_player_champion()
    enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup = generate_enemy_champions(ally_top, player, ally_mid, ally_bot, ally_sup)

    print(f'{ally_top.name}, {player.name}, {ally_mid.name}, {ally_bot.name}, {ally_sup.name}')
    print(f'{enemy_top.name}, {enemy_jg.name}, {enemy_mid.name}, {enemy_bot.name}, {enemy_sup.name}')

if __name__ == "__main__":
    main()