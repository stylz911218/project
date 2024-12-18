from object import home, turret, camp, inhibitor, largecamp
from map import zones, MapZone, generate_random_point_in_zone
from map import top_get_zones_and_weights_for_time, jg_get_zones_and_weights_for_time, mid_get_zones_and_weights_for_time, bot_get_zones_and_weights_for_time, sup_get_zones_and_weights_for_time
from Champions import top_champions, ad_champions, mid_champions, jungle_champions, support_champions, jungle_Khazix
from Champions import top_weight, jungle_weight, mid_weight, ad_weight, support_weight
from Champions import top_summoners_weight, jg_summoners_weight, mid_summoners_weight, bot_summoners_weight, sup_summoners_weight
import random

# action space: 0 =  scuttler, 1 = drake, 2 = grubs, 3 = herald, 4 = baron, 5 = elder, 6 = clean own jungle, 7 = invade enemy jungle
action_space = ["take scuttler", "take drake", "take grubs", "take herald", "take baron", "take elder", "clean own jungle", "invade enemy jungle"]

# globals
draketype = ["ocean", "mountain", "cloud", "chemtech", "hextech", "infernal"]

summoners_spell = ["heal", "ghost", "barrier", "exhaust", "clarity", "flash", "tp", "smite", "cleanse", "ignite"]

# position: mid = 0, top = -2, bot lane = 2, own jungle = 1, enemy jungle = 1.5, drake and baron pool = 1.2
# locations = [0, -2, 2, -1, 1, -1.5, 1.5, 1.2, -1.2]


# 當前時間 (先嘗試隨機生成，後續可以進行更改)
def generate_random_game_time():
    total_seconds = random.randint(0, 3600)  
    minutes, seconds = divmod(total_seconds, 60)  
    return f'{minutes:02d}:{seconds:02d}', total_seconds

# 指定時間
def generate_specific_game_time():
    early_times = [5, 6, 10]  # 早期階段的固定分鐘數
    mid_times = list(range(14, 21))  # 14-20 分鐘之間的整數
    late_times = list(range(20, 61, 3))  # 20 分鐘後每 3 分鐘到最多 60 分鐘

    # 將所有可能的時間合併成一個列表
    all_possible_times = early_times + mid_times + late_times

    minutes = random.choice(all_possible_times)

    total_seconds = minutes * 60

    return f'{minutes:02d}:{0:02d}', total_seconds

# 角色資料

# 生成召喚師技能
def select_summoner_skills(champion, weight):
    # 先確保必須的技能在選擇列表中
    selected_skills = []
    if champion.position == "jungle":
        selected_skills.append("smite")  # 打野必須帶重擊

    if champion.name == "Hekarim":
        selected_skills.append("ghost")

    if champion.position == "bot" or champion.position == "mid":
        selected_skills.append("flash") 

    if champion.position == "support" and not (champion.name == "Yuumi" or champion.name == "Shaco"):
        selected_skills.append("flash") 

    # 獲取可以選擇的技能
    available_skills = [skill for skill in champion.correctsummoners if skill not in selected_skills]

    # 隨機選擇一個或多個技能
    while len(selected_skills) < 2:  # 確保至少選兩個技能
        skill = random.choices(list(weight.keys()), weights=list(weight.values()), k=1)[0]
        if skill in available_skills and skill not in selected_skills:
            selected_skills.append(skill)

    return selected_skills

# 生成友軍
def generate_ally_champions():
    ally_top = random.choices(top_champions, weights=top_weight, k=1)[0]
    ally_mid = random.choices(mid_champions, weights=mid_weight, k=1)[0]
    ally_bot = random.choices(ad_champions, weights=ad_weight, k=1)[0]
    ally_sup = random.choices(support_champions, weights=support_weight, k=1)[0]

    ally_top.team_now(1)
    ally_mid.team_now(1)
    ally_bot.team_now(1)
    ally_sup.team_now(1)

    return ally_top, ally_mid, ally_bot, ally_sup

# 生成玩家
def generate_player_champion():
    player = jungle_Khazix
    return player

# 生成敵軍
def generate_enemy_champions(ally_top, player, ally_mid, ally_bot, ally_sup):
    enemy_top = random.choices(top_champions, weights=top_weight, k=1)[0]
    while enemy_top.name == ally_top.name or enemy_top.name == player.name or enemy_top.name == ally_mid.name or enemy_top.name == ally_bot.name or enemy_top.name == ally_sup.name:
        enemy_top = random.choices(top_champions, weights=top_weight, k=1)[0]

    enemy_jg = random.choices(jungle_champions, weights=jungle_weight, k=1)[0]
    while enemy_jg.name == ally_top.name or enemy_jg.name == player.name or enemy_jg.name == ally_mid.name or enemy_jg.name == ally_bot.name or enemy_jg.name == ally_sup.name:
        enemy_jg = random.choices(jungle_champions, weights=jungle_weight, k=1)[0]
    
    enemy_mid = random.choices(mid_champions, weights=mid_weight, k=1)[0]
    while enemy_mid.name == ally_top.name or enemy_mid.name == player.name or enemy_mid.name == ally_mid.name or enemy_mid.name == ally_bot.name or enemy_mid.name == ally_sup.name:
        enemy_mid = random.choices(mid_champions, weights=mid_weight, k=1)[0]

    enemy_bot = random.choices(ad_champions, weights=ad_weight, k=1)[0]
    while enemy_bot.name == ally_top.name or enemy_bot.name == player.name or enemy_bot.name == ally_mid.name or enemy_bot.name == ally_bot.name or enemy_bot.name == ally_sup.name:
        enemy_bot = random.choices(ad_champions, weights=ad_weight, k=1)[0]

    enemy_sup = random.choices(support_champions, weights=support_weight, k=1)[0]
    while enemy_sup.name == ally_top.name or enemy_sup.name == player.name or enemy_sup.name == ally_mid.name or enemy_sup.name == ally_bot.name or enemy_sup.name == ally_sup.name:
        enemy_sup = random.choices(support_champions, weights=support_weight, k=1)[0]

    enemy_top.team_now(-1)
    enemy_jg.team_now(-1)
    enemy_mid.team_now(-1)
    enemy_bot.team_now(-1)
    enemy_sup.team_now(-1)

    return enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup

# 生成角色評分
def generate_ally_sum_and_runes(top, mid, bot, sup):
    
    # 符文
    top_keystone = random.choice(top.correctkeystone)
    top.keystone_now(top_keystone)
    mid_keystone = random.choice(mid.correctkeystone)
    mid.keystone_now(mid_keystone)
    bot_keystone = random.choice(bot.correctkeystone)
    bot.keystone_now(bot_keystone)
    sup_keystone = random.choice(sup.correctkeystone)
    sup.keystone_now(sup_keystone)

    # print(f"Ally: Top: {top_keystone}, Mid: {mid_keystone}, Bot: {bot_keystone}, Sup: {sup_keystone}")

    # 召喚師技能
    top_selected_skills = select_summoner_skills(top, top_summoners_weight)
    top.summoners_now(top_selected_skills)

    mid_selected_skills = select_summoner_skills(mid, mid_summoners_weight)
    mid.summoners_now(mid_selected_skills)

    bot_selected_skills = select_summoner_skills(bot, bot_summoners_weight)
    bot.summoners_now(bot_selected_skills)

    sup_selected_skills = select_summoner_skills(sup, sup_summoners_weight)
    sup.summoners_now(sup_selected_skills)

    # print(f"Ally :Top: {top.summoners}, Mid: {mid.summoners}, Bot: {bot.summoners}, Sup: {sup.summoners} \n")



def generate_player_sum_and_runes(player):
    
    player_keystone = random.choice(player.correctkeystone)
    player.keystone_now(player_keystone)
    # print(f"Player keystone: {player_keystone}")

    player_selected_skills = select_summoner_skills(player, jg_summoners_weight)
    player.summoners_now(player_selected_skills)

    # print(f"Player sum: {player.summoners}\n")


def generate_enemy_sum_and_runes(top, jg, mid, bot, sup):
    # 符文
    top_keystone = random.choice(top.correctkeystone)
    top.keystone_now(top_keystone)
    jg_keystone = random.choice(jg.correctkeystone)
    jg.keystone_now(jg_keystone)
    mid_keystone = random.choice(mid.correctkeystone)
    mid.keystone_now(mid_keystone)
    bot_keystone = random.choice(bot.correctkeystone)
    bot.keystone_now(bot_keystone)
    sup_keystone = random.choice(sup.correctkeystone)
    sup.keystone_now(sup_keystone)

    # print(f"Enemy: Top: {top_keystone}, Jg: {jg_keystone} ,Mid: {mid_keystone}, Bot: {bot_keystone}, Sup: {sup_keystone}")

    # 召喚師技能
    top_selected_skills = select_summoner_skills(top, top_summoners_weight)
    top.summoners_now(top_selected_skills)

    jg_selected_skills = select_summoner_skills(jg, jg_summoners_weight)
    jg.summoners_now(jg_selected_skills)

    mid_selected_skills = select_summoner_skills(mid, mid_summoners_weight)
    mid.summoners_now(mid_selected_skills)

    bot_selected_skills = select_summoner_skills(bot, bot_summoners_weight)
    bot.summoners_now(bot_selected_skills)

    sup_selected_skills = select_summoner_skills(sup, sup_summoners_weight)
    sup.summoners_now(sup_selected_skills)

    # print(f"Enemy: Top: {top.summoners}, Jg: {jg.summoners} ,Mid: {mid.summoners}, Bot: {bot.summoners}, Sup: {sup.summoners} \n")

def generate_ally_position(current_game_time, side, neutral_camp, ally_drake_count, enemy_drake_count, grub_slain_by, baron_slain_by, elder_slain_by, ally_top, player, ally_mid, ally_bot, ally_sup):
    
    # player
    player_possible_zone, player_weight = jg_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, grub_slain_by=grub_slain_by, drake_alive=neutral_camp[1].alive, 
                                      grubs_alive=neutral_camp[2].alive, herald_alive=neutral_camp[3].alive, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=1)
    
    player_chosen_zone = random.choices(player_possible_zone, player_weight)[0]
    player_position = generate_random_point_in_zone(player_chosen_zone)
    # print(f"At time {current_game_time} minutes, player in zone {player_chosen_zone.name}, the position is {player_position}")

    # top
    top_possible_zone, top_weight = top_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=player_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=1)
    top_chosen_zone = random.choices(top_possible_zone, top_weight)[0]
    top_position = generate_random_point_in_zone(top_chosen_zone)
    # print(f"At time {current_game_time} minutes, ally top in zone {top_chosen_zone.name}, the position is {top_position}")

    # mid
    mid_possible_zone, mid_weight = mid_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=player_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=1)
    mid_chosen_zone = random.choices(mid_possible_zone, mid_weight)[0]
    mid_position = generate_random_point_in_zone(mid_chosen_zone)
    # print(f"At time {current_game_time} minutes, ally mid in zone {mid_chosen_zone.name}, the position is {mid_position}")

    # bot
    bot_possible_zone, bot_weight = bot_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=player_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=1)
    bot_chosen_zone = random.choices(bot_possible_zone, bot_weight)[0]
    bot_position = generate_random_point_in_zone(bot_chosen_zone)
    # print(f"At time {current_game_time} minutes, ally bot in zone {bot_chosen_zone.name}, the position is {bot_position}")

    # sup
    sup_possible_zone, sup_weight = bot_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=player_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=1)
    sup_chosen_zone = random.choices(sup_possible_zone, sup_weight)[0]
    sup_position = generate_random_point_in_zone(sup_chosen_zone)
    # print(f"At time {current_game_time} minutes, ally sup in zone {sup_chosen_zone.name}, the position is {sup_position}")

    ally_top.current_place(top_chosen_zone.name, top_position)
    player.current_place(player_chosen_zone.name, player_position)
    ally_mid.current_place(mid_chosen_zone.name, mid_position)
    ally_bot.current_place(bot_chosen_zone.name, bot_position)
    ally_sup.current_place(sup_chosen_zone.name, sup_position)

def generate_enemy_position(current_game_time, side, neutral_camp, enemy_drake_count, ally_drake_count, grub_slain_by, baron_slain_by, elder_slain_by,  enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup):
    
    # jungle
    jungle_possible_zone, player_weight = jg_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, grub_slain_by=grub_slain_by, drake_alive=neutral_camp[1].alive, 
                                      grubs_alive=neutral_camp[2].alive, herald_alive=neutral_camp[3].alive, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=0)
    
    jungle_chosen_zone = random.choices(jungle_possible_zone, player_weight)[0]
    jungle_position = generate_random_point_in_zone(jungle_chosen_zone)
    # print(f"At time {current_game_time} minutes, enemy jungle in zone {jungle_chosen_zone.name}, the position is {jungle_position}")

    # top
    top_possible_zone, top_weight = top_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=jungle_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=0)
    top_chosen_zone = random.choices(top_possible_zone, top_weight)[0]
    top_position = generate_random_point_in_zone(top_chosen_zone)
    # print(f"At time {current_game_time} minutes, enemy top in zone {top_chosen_zone.name}, the position is {top_position}")

    # mid
    mid_possible_zone, mid_weight = mid_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=jungle_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=0)
    mid_chosen_zone = random.choices(mid_possible_zone, mid_weight)[0]
    mid_position = generate_random_point_in_zone(mid_chosen_zone)
    # print(f"At time {current_game_time} minutes, enemy mid in zone {mid_chosen_zone.name}, the position is {mid_position}")

    # bot
    bot_possible_zone, bot_weight = bot_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=jungle_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=0)
    bot_chosen_zone = random.choices(bot_possible_zone, bot_weight)[0]
    bot_position = generate_random_point_in_zone(bot_chosen_zone)
    # print(f"At time {current_game_time} minutes, enemy bot in zone {bot_chosen_zone.name}, the position is {bot_position}")

    # sup
    sup_possible_zone, sup_weight = bot_get_zones_and_weights_for_time(time=int(current_game_time[0:2]), side=side, jungle_zone=jungle_chosen_zone, drake_count=ally_drake_count, enemy_drake_count=enemy_drake_count, baron_alive=neutral_camp[4].alive, baron_killed_by= baron_slain_by, elder_alive=neutral_camp[5].alive,
                                      elder_killed_by= elder_slain_by, player_or_not=0)
    sup_chosen_zone = random.choices(sup_possible_zone, sup_weight)[0]
    sup_position = generate_random_point_in_zone(sup_chosen_zone)
    # print(f"At time {current_game_time} minutes, enemy sup in zone {sup_chosen_zone.name}, the position is {sup_position}")

    enemy_top.current_place(top_chosen_zone.name, top_position)
    enemy_jg.current_place(jungle_chosen_zone.name, jungle_position)
    enemy_mid.current_place(mid_chosen_zone.name, mid_position)
    enemy_bot.current_place(bot_chosen_zone.name, bot_position)
    enemy_sup.current_place(sup_chosen_zone.name, sup_position)

# 防禦塔
def enemyturret():
    pass

# 防禦塔
def allyturret():
    pass

# 中立資源

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
        return [], 0, 0

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

    return drakes, ally_drake_count, enemy_drake_count

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

    # print(f'Drake info: alive = {drake.alive}, respawn = {drake.respawn_countdown}, type = {drake.buff}, value = {drake.value}')

    # grubs 1 
    # done
    grub_slain_by = "Nobody"
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
            killed_time = random.randint(360, timenow)
            minutes, seconds = divmod(killed_time, 60)
            slain_by = random.choice(["ally", "enemy"])
            grub_slain_by = slain_by
            # print(f'First grubs were killed at {minutes:02d}:{seconds:02d} and slain by {grub_slain_by}')
            if killed_time > 585: # won't respawn
                grub = largecamp(alive=-1, respawn_countdown=0, buff="Won't respawn", value=90)
            else:
                respawn = killed_time + 240
                timediff = respawn - timenow
                minutes, seconds = divmod(timediff, 60)
                grub = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="grub", value=90)
    
    # print(f'Grub info: alive = {grub.alive}, respawn = {grub.respawn_countdown}, type = {grub.buff}, value = {grub.value}')

    
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

    # print(f'Herald info: alive = {herald.alive}, respawn = {herald.respawn_countdown}, type = {herald.buff}, value = {herald.value}')    

    # baron
    # done
    baron_slain_by = "Nobody"

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
            baron_buff_end_time = respawn - 360 + 180
            if baron_buff_end_time < timenow:
                baron_slain_by = "Nobody"
            else:
                baron_slain_by = random.choice(["ally", "enemy"])

    # print(f'Baron info: alive = {baron.alive}, respawn = {baron.respawn_countdown}, type = {baron.buff}, value = {baron.value}')

    # elder
    # done

    elder_slain_by = "Nobody"
    if not elder_available:
        elder = largecamp(alive=0, respawn_countdown=-1, buff="Won't respawn", value=1100)
    else:
        respawn = 0
        timenow = int(time[0:2]) * 60 + int(time[3:5])
        last_drake_time, last_drake_seconds = get_last_drake_time(timenow, drakecount, drakes)
        # print(f'last drake was slain at {last_drake_time}')
        if timenow >= 2800 and last_drake_slain_time < timenow - 720: # 第二條遠古龍
            alive = random.choice([0, 1])
            if alive == 1:
                elder = largecamp(alive=1, respawn_countdown=0, buff="Elder", value=1100)
            else:
                timediff = 0
                while timediff < (timenow - 360):
                    respawn = random.randint(1, 360)
                    timenow = int(time[0:2]) * 60 + int(time[3:5])
                    timediff = timenow - respawn
                minutes, seconds = divmod(respawn, 60)
                elder = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="Elder", value=1100) # killed
        else: # 第一條遠古龍
            elder_spawn_time = last_drake_seconds + 360  # 6 minutes after last drake
            if elder_spawn_time > timenow:
                respawn = elder_spawn_time - timenow
                minutes, seconds = divmod(respawn, 60)
                elder = largecamp(alive=0, respawn_countdown=f'{minutes:02d}:{seconds:02d}', buff="Elder", value=1100)
            else:
                elder = largecamp(alive=1, respawn_countdown=0, buff="Elder", value=1100)

        if not elder.alive:
            elder_buff_end_time = respawn - 360 + 150
            if elder_buff_end_time < timenow:
                elder_slain_by = "Nobody"
            else:
                elder_slain_by = random.choice(["ally", "enemy"])
    
    # print(f'Elder info: alive = {elder.alive}, respawn = {elder.respawn_countdown}, type = {elder.buff}, value = {elder.value}')

    allycamp = [allygromp, allyraptor, allyblue, allykrug, allyred, allywolf]
    enemycamp = [enemygromp, enemyraptor, enemyblue, enemykrug, enemyred, enemywolf]
    neutralcamp = [scuttler, drake, grub, herald, baron, elder]

    return allycamp, enemycamp, neutralcamp, grub_slain_by, baron_slain_by, elder_slain_by
    


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


def environment():
    current_game_time, current_game_seconds = generate_specific_game_time()
    # print(f'Current game time: {current_game_time}')

    drakecount = 0
    temp = int(current_game_time[0:2]) // 5
    
    if temp > 7:
        drakecount = random.randint(0,7)
    else:
        drakecount = random.randint(0,temp)
    
    drakes, ally_drake_count, enemy_drake_count = generate_drake_info(drakecount, current_game_seconds)
    truedrakecount = 0
    for i in drakes:
        # print(i)
        truedrakecount += 1

    # print(f'Drake slained: {truedrakecount}')

    ally_camp, enemy_camp, neutral_camp, grub_slain_by, baron_slain_by, elder_slain_by = junglecamp(current_game_time, drakecount=truedrakecount, drakes=drakes)
    actions = available_actions(ally=ally_camp, enemy=enemy_camp, neutral=neutral_camp)

    # print("\n")

    # # print("Ally camp:")
    # for i in ally:
    #     # print(f'{i.__dict__}')


    # # print("Enemy camp:")
    # for i in enemy:
    #     # print(f'{i.__dict__}')

    # # print("\n")
    # print("Actions available: ")
    # for i in range(len(actions)):
        # print(action_space[actions[i]])

    # print("\n")

    ally_top, ally_mid, ally_bot, ally_sup = generate_ally_champions()
    player = generate_player_champion()
    enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup = generate_enemy_champions(ally_top, player, ally_mid, ally_bot, ally_sup)

    # print(f'Our Team: {ally_top.name}, {player.name}, {ally_mid.name}, {ally_bot.name}, {ally_sup.name}')
    # print(f'Enemy Team: {enemy_top.name}, {enemy_jg.name}, {enemy_mid.name}, {enemy_bot.name}, {enemy_sup.name}\n')

    generate_player_sum_and_runes(player)
    generate_ally_sum_and_runes(ally_top, ally_mid, ally_bot, ally_sup)
    generate_enemy_sum_and_runes(enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup)

    # print(f"Last Baron was slained by {baron_slain_by}\n")
    # print(f"Last Elder was slained by {elder_slain_by}\n")

    # for allys
    side = random.choice((-1,1))
    side2 = side * -1
    # print(f"Player at side {side}")

    generate_ally_position(current_game_time, side, neutral_camp, ally_drake_count, enemy_drake_count, grub_slain_by, baron_slain_by, elder_slain_by\
                           , ally_top, player, ally_mid, ally_bot, ally_sup)
    generate_enemy_position(current_game_time, side2, neutral_camp, enemy_drake_count, ally_drake_count, grub_slain_by, baron_slain_by, elder_slain_by\
                            ,  enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup) 
    
    ally_top.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    ally_mid.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    ally_bot.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    ally_sup.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)

    enemy_top.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    enemy_jg.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    enemy_mid.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    enemy_bot.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)
    enemy_sup.final_value(player=0, player_location=player.location, hp_now=-1, mana_now= -1, summoners1_ = -1, summoners2_ = -1)

    allies = [ally_top, ally_mid, ally_bot, ally_sup]
    enemies = [enemy_top, enemy_jg, enemy_mid, enemy_bot, enemy_sup]

    return actions, allies, enemies, ally_drake_count, enemy_drake_count, ally_camp, enemy_camp, neutral_camp, grub_slain_by, current_game_seconds

# if __name__ == "__main__":
    # main()