from object import champion
from env import summoners_spell

# 核心符文:強攻,瞬疾步法,征服者, 電刑,靈魂收割,叢刃, 艾黎,彗星,相位, 不滅,餘震,神聖守護, 冰川,啟封法書,先攻
key_runes = ["PTA", "FF", "Con", 
             "Elec", "DH", "HoB", 
             "SA", "AC", "PR", 
             "GotU", "AS", "Guard", 
             "GA", "US", "FS", ]

# 上路角色
top_Aatrox = champion("Aatrox", ["Con", "AC"], "top", ["flash", "tp", "ignite", "barrier"])
top_Nasus = champion("Nasus", ["FF", "SA"], "top", ["flash", "tp", "ghost"])
top_Darius = champion("Darius", ["Con"], "top", ["flash", "ignite", "ghost", "barrier"])
top_Poppy = champion("Poppy", ["GotU"], "top", ["flash", "tp", "ignite"])
top_Camille = champion("Camille", ["GotU"], "top", ["flash", "tp", "ignite"])
top_Renecton = champion("Renecton", ["Con", "PTA"], "top", ["flash", "tp", "ignite"])
top_Garen = champion("Garen", ["Con"], "top", ["flash", "tp", "ignite"])
top_Cassiopeia = champion("cassiopeia", ["Con", "SA"], "top", ["flash", "tp", "ignite"])
top_Sett = champion("Sett", ["Con", "PTA"], "top", ["flash", "tp", "ignite"])
top_Warwick = champion("Warwick", ["Con", "PTA"], "top", ["flash", "tp", "barrier", "ignite"])
top_Fiora = champion("Fiora", ["Con", "GotU"], "top", ["flash", "tp", "ghost", "ignite"])
top_Aurora = champion("Aurora", ["FF", "Elec"], "top", ["flash", "tp", "ignite"])
top_Volibear = champion("Volibear", ["GotU", "PTA"], "top", ["flash", "tp", "ignite"])
top_Tryndamere = champion("Tryndamere", ["GotU", "FF"], "top", ["flash", "ignite", "ghost"])
top_Mordekaiser = champion("Mordekaiser", ["Con"], "top", ["flash", "tp", "ghost", "ignite"])
top_Kled = champion("Kled", ["Con"], "top", ["flash", "tp", "ignite"]) # here
top_Jax = champion("Jax", ["Con", "GotU"], "top", ["flash", "tp", "ignite"])
top_Yorick = champion("Yorick", ["Con", "AC"], "top", ["flash", "tp", "ghost", "ignite"])
top_Zac = champion("Zac", ["Con", "GotU", "AS"], "top", ["flash", "tp", "ignite"])
top_Urgot = champion("Urgot", ["Con", "PTA"], "top", ["flash", "tp", "ignite"])
top_Malphite = champion("Malphite", ["AC"], "top", ["flash", "tp", "ignite"])
top_Gwen = champion("Gwen", ["Con"], "top", ["flash", "ignite", "ghost", "tp"])
top_Illaoi = champion("Illaoi", ["Con", "GotU"], "top", ["flash", "tp", "exhaust", "ignite"])
top_Jayce = champion("Jayce", ["Con", "PR", "SA"], "top", ["flash", "tp", "ignite"])
top_Yone = champion("Yone", ["Con", "FF"], "top", ["flash", "tp", "ignite"])
top_Udyr = champion("Udyr", ["GotU"], "top", ["flash", "tp", "ghost"])
top_Ryze = champion("Ryze", ["PR"], "top", ["flash", "tp", "ghost"])
top_Kennen = champion("Kennen", ["Elec", "SA"], "top", ["flash", "tp", "ignite"])
top_Shen = champion("Shen", ["GotU", "AS"], "top", ["flash", "tp", "ignite"])
top_Raven = champion("Raven", ["Con"], "top", ["flash", "tp", "ignite"])
top_Gangplank = champion("Gangplank", ["GotU", "FS", "FF"], "top", ["flash", "tp", "ignite"])
top_Drmondo = champion("Drmondo", ["GotU", "AS"], "top", ["flash", "tp", "ghost"])
top_Gnar = champion("Gnar", ["GotU", "FF"], "top", ["flash", "tp", "ghost"])
top_Ornn = champion("Ornn", ["GotU", "AS"], "top", ["flash", "tp", "ignite"])
top_Sion = champion("Sion", ["GotU", "AS"], "top", ["flash", "tp", "ghost"])
top_Rumble = champion("Rumble", ["AC"], "top", ["flash", "tp", "ignite"])
top_Irelia = champion("Irelia", ["Con"], "top", ["flash", "tp", "ignite"])
top_Sylas = champion("Sylas", ["Con", "Elec"], "top", ["flash", "tp", "ignite"])
top_Pantheon = champion("Patheon", ["Con", "PTA"], "top", ["flash", "tp", "ignite"])
top_Heimer = champion("Heimer", ["Con", "AC"], "top", ["flash", "tp", "ignite"])
top_Olaf = champion("Olaf", ["Con"], "top", ["flash", "tp", "ghost"])
top_Vladimir = champion("Vladimir", ["PR", "SA"], "top", ["flash", "tp", "ghost", "ignite"])
top_Ksante = champion("Ksante", ["GotU", "Con", "AS"], "top", ["flash", "tp", "ghost"])
top_Gragas = champion("Gragas", ["PR", "AC"], "top", ["flash", "tp", "ignite"])
top_Tahmkench = champion("Tahmkench", ["GotU", "AS"], "top", ["flash", "tp", "ghost"])
top_Quinn = champion("Quinn", ["Elec", "FF", "PTA"], "top", ["flash", "tp", "ignite"])
top_Wukong = champion("Wukong", ["Con", "GotU"], "top", ["flash", "tp", "ignite"])
top_Singed = champion("Singed", ["Con", "US"], "top", ["flash", "tp", "ghost", "ignite"])
top_Teemo = champion("Teemo", ["PTA", "GotU"], "top", ["flash", "tp", "ignite"])
top_Trundle = champion("Trundle", ["PTA", "GotU"], "top", ["flash", "tp", "ghost"])
top_Akali = champion("Akali", ["Con", "FF"], "top", ["flash", "tp", "ignite"])
top_Vayne = champion("Vayne", ["PTA", "FF"], "top", ["flash", "tp", "ghost"])
top_Kyle = champion("Kyle", ["FF"], "top", ["flash", "tp", "ghost"])
top_Chogath = champion("Chogath", ["GotU", "AC"], "top", ["flash", "tp", "ignite"])

top_champions = [top_Aatrox, top_Nasus, top_Darius, top_Poppy, top_Camille, top_Renecton, top_Garen, top_Cassiopeia, top_Sett, top_Warwick,
                 top_Fiora, top_Aurora, top_Volibear, top_Tryndamere, top_Mordekaiser, top_Kled, top_Jax, top_Yorick, top_Zac, top_Urgot,
                 top_Malphite, top_Gwen, top_Illaoi, top_Jayce, top_Udyr, top_Yone, top_Ryze, top_Kennen, top_Shen, top_Raven, top_Gangplank,
                 top_Drmondo, top_Gnar, top_Ornn, top_Sion, top_Rumble, top_Irelia, top_Sylas, top_Pantheon, top_Heimer, top_Olaf, top_Vladimir,
                 top_Ksante, top_Gragas, top_Tahmkench, top_Quinn, top_Wukong, top_Singed, top_Teemo, top_Trundle, top_Akali, top_Vayne,
                 top_Kyle, top_Chogath
                 ]
# 打野角色
jungle_champions = []

# 中路角色
mid_champions = []

# 下路角色
ad_champions = []

# 輔助角色
support_champions = []
