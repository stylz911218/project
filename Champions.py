from object import champion

# 核心符文:強攻,瞬疾步法,征服者, 電刑,靈魂收割,叢刃, 艾黎,彗星,相位, 不滅,餘震,神聖守護, 冰川,啟封法書,先攻
key_runes = ["PTA", "FF", "Con", 
             "Elec", "DH", "HoB", 
             "SA", "AC", "PR", 
             "GotU", "AS", "Guard", 
             "GA", "US", "FS" ]

top_summoners_weight = {"flash": 80,"tp": 80,"ignite": 25,"ghost": 2, "barrier": 1}

jg_summoners_weight = {"flash": 100,"smite": 100,"ignite": 50,"ghost": 1, "exhaust": 20}

mid_summoners_weight = {"flash": 80,"tp": 50,"ignite": 20,"ghost": 5, "barrier": 1, "cleanse": 1}

bot_summoners_weight = {"flash": 80,"tp": 5,"ignite": 0,"ghost": 1, "barrier": 50, "cleanse": 15}

sup_summoners_weight = {"flash": 80, "exhaust": 20, "ignite": 20, "heal": 10}

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
top_Kled = champion("Kled", ["Con"], "top", ["flash", "tp", "ignite"])
top_Jax = champion("Jax", ["Con", "GotU"], "top", ["flash", "tp", "ignite"])
top_Yorick = champion("Yorick", ["Con", "AC"], "top", ["flash", "tp", "ghost", "ignite"])
top_Zac = champion("Zac", ["Con", "GotU", "AS"], "top", ["flash", "tp", "ignite"])
top_Urgot = champion("Urgot", ["Con", "PTA"], "top", ["flash", "tp", "ignite"])
top_Malphite = champion("Malphite", ["AC", "GotU"], "top", ["flash", "tp", "ignite"])
top_Gwen = champion("Gwen", ["Con"], "top", ["flash", "ignite", "ghost", "tp"])
top_Illaoi = champion("Illaoi", ["Con", "GotU"], "top", ["flash", "tp", "exhaust", "ignite"])
top_Jayce = champion("Jayce", ["Con", "PR", "SA"], "top", ["flash", "tp", "ignite"])
top_Yone = champion("Yone", ["Con", "FF", "GotU"], "top", ["flash", "tp", "ignite"])
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

top_weight = [12.86, 6.43, 5.71, 2.01, 5.85, 6.28, 5.61, 0.95, 4.21, 1.57, 4.95, 1.15, 3.69, 1.74, 4.18, 1.54, 8.73, 3.02, 1.92, 1.5,
              3.89, 3.25, 2.34, 6.63, 0.92, 9.18, 1.56, 2.7, 2.02, 3.14, 3.87, 2.8, 4.81, 2.77, 2.31, 2.03, 3.08, 1.36, 1.67, 0.82, 
              1.97, 8.98, 4.75, 2.6, 1.31, 0.79, 2.21, 0.97, 1.8, 0.93, 1.56, 1.28, 1.04, 0.83]

# print(top_champions.__len__(), top_weight.__len__())

# 打野角色
jungle_Leesin = champion("Leesin", ["Con", "Elec", "DH"], "jungle", ["flash", "smite"])
jungle_Lillia = champion("Lillia", ["Con"], "jungle", ["flash", "smite"])
jungle_Reksai = champion("Reksai", ["Con"], "jungle", ["flash", "smite"])
jungle_Noc = champion("Noc", ["Con", "PTA"], "jungle", ["flash", "smite"])
jungle_Warwick = champion("Warwick", ["PTA"], "jungle", ["flash", "smite", "ghost"])
jungle_Shaco = champion("Shaco", ["DH", "HoB"], "jungle", ["flash", "smite", "ignite"])
jungle_Khazix = champion("Khazix", ["FS", "DH", "Elec"], "jungle", ["flash", "smite", "ghost"])
jungle_Belveth = champion("Belveth", ["Con", "PTA"], "jungle", ["flash", "smite", "ghost"])
jungle_Xinzhao = champion("Xinzhao", ["Con", "HoB"], "jungle", ["flash", "smite"])
jungle_Amumu = champion("Amumu", ["Con", "AS"], "jungle", ["flash", "smite"])
jungle_Elise = champion("Elise", ["DH", "PTA"], "jungle", ["flash", "smite", "ignite"])
jungle_Yi = champion("YI", ["PTA", "HoB"], "jungle", ["flash", "smite", "ghost"])
jungle_Skarner = champion("Skarner", ["GotU", "AS"], "jungle", ["flash", "smite", "ghost"])
jungle_Ekko = champion("Ekko", ["DH"], "jungle", ["flash", "smite", "ignite"])
jungle_Karthus = champion("Karthus", ["DH"], "jungle", ["flash", "smite", "exhaust"])
jungle_Taliyah = champion("Taliyah", ["DH"], "jungle", ["flash", "smite", "ghost"])
jungle_Viego = champion("Viego", ["Con"], "jungle", ["flash", "smite"])
jungle_Evelyn = champion("Evelyn", ["Elec"], "jungle", ["flash", "smite", "ghost"])
jungle_Volibear = champion("Volibear", ["PTA"], "jungle", ["flash", "smite", "ghost"])
jungle_Nidalee = champion("Nidalee", ["Con", "DH"], "jungle", ["flash", "smite"])
jungle_Gwen = champion("Gwen", ["Con"], "jungle", ["flash", "smite", "ghost"])
jungle_Jarvan = champion("Jarvan", ["Con"], "jungle", ["flash", "smite", "ghost"])
jungle_Talon = champion("Talon", ["FS", "Elec"], "jungle", ["flash", "smite", "ignite"])
jungle_Kayn = champion("Kayn", ["Con", "DH"], "jungle", ["flash", "smite", "smite", "exhaust"])
jungle_Briar = champion("Briar", ["PTA", "HoB"], "jungle", ["flash", "smite", "ignite"])
jungle_Vi = champion("Vi", ["Con"], "jungle", ["flash", "smite", "ghost"])
jungle_Graves = champion("Graves", ["FF"], "jungle", ["flash", "smite", "ghost"])
jungle_Ivern = champion("Ivern", ["SA"], "jungle", ["flash", "smite", "ghost"])
jungle_Zac = champion("Zac", ["Con", "AS"], "jungle", ["flash", "smite", "ignite"])
jungle_Fiddlestick = champion("Fiddlestick", ["FS", "Elec", "DH"], "jungle", ["flash", "smite", "ghost"])
jungle_Nunu = champion("Nunu", ["PR"], "jungle", ["flash", "smite", "ghost"])
jungle_Udyr = champion("Udyr", ["Con", "PTA"], "jungle", ["flash", "smite", "ghost"])
jungle_Hekarim = champion("Hekarim", ["Con", "PR"], "jungle", ["flash", "smite", "ghost"])
jungle_Wukong = champion("Wukong", ["Con"], "jungle", ["flash", "smite", "ghost"])
jungle_Poppy = champion("Poppy", ["DH", "PR", "AS"], "jungle", ["flash", "smite", "ghost"])
jungle_Kindred = champion("Kindred", ["Con", "PTA"], "jungle", ["flash", "smite", "ghost"])
jungle_Zyra = champion("Zyra", ["AC", "Elec"], "jungle", ["flash", "smite", "ghost"])
jungle_Rammus = champion("Rammus", ["AS"], "jungle", ["flash", "smite", "ghost"])
jungle_Shyvana = champion("Graves", ["FF", "DH"], "jungle", ["flash", "smite", "ghost"])
jungle_Diana = champion("Diana", ["Con"], "jungle", ["flash", "smite", "ghost"])
jungle_Sjuanni = champion("Sjuanni", ["AS"], "jungle", ["flash", "smite", "ghost"])
jungle_Gragas = champion("Gragas", ["DH"], "jungle", ["flash", "smite"])
jungle_Brand = champion("Brand", ["DH", "Elec"], "jungle", ["flash", "smite", "ghost"])
jungle_Zed = champion("Zed", ["FS", "DH", "Elec"], "jungle", ["flash", "smite", "ghost"])
jungle_Sylas = champion("Sylas", ["DH", "Elec"], "jungle", ["flash", "smite"])
jungle_Rengar = champion("Rengar", ["Con", "Elec", "DH"], "jungle", ["flash", "smite", "ghost"])
jungle_Maokai = champion("Maokai", ["PR", "AS"], "jungle", ["flash", "smite", "ghost"])
jungle_Qiyanna = champion("Qiyanna", ["FS", "Elec"], "jungle", ["flash", "smite", "ignite"])


jungle_champions = [jungle_Leesin, jungle_Lillia, jungle_Reksai, jungle_Noc, top_Warwick, jungle_Shaco, jungle_Khazix, jungle_Belveth,
                    jungle_Xinzhao, jungle_Elise, jungle_Amumu, jungle_Yi, jungle_Skarner, jungle_Ekko, jungle_Karthus, jungle_Taliyah,
                    jungle_Viego, jungle_Evelyn, jungle_Volibear, jungle_Nidalee, jungle_Gwen, jungle_Jarvan, jungle_Talon, jungle_Kayn,
                    jungle_Briar, jungle_Vi, jungle_Graves, jungle_Ivern, jungle_Zac, jungle_Fiddlestick, jungle_Nunu, jungle_Udyr, jungle_Wukong,
                    jungle_Hekarim, jungle_Poppy, jungle_Kindred, jungle_Zyra, jungle_Rammus, jungle_Shyvana, jungle_Diana, jungle_Sjuanni, jungle_Gragas,
                    jungle_Brand, jungle_Zed, jungle_Sylas, jungle_Rengar, jungle_Maokai, jungle_Qiyanna]

jungle_weight = [30.13, 9.26, 2, 5.79, 2.56, 4.32, 9.68, 2.12, 5.91, 3.72, 4.25, 3.13, 2.32, 3.43, 3.34, 2.73, 17.19, 1.7,
                 1.34, 10.83, 1.16, 7.57, 1.69, 2.76, 2.73, 7.45, 6.5, 0.77, 3.33, 2.11, 1.68, 1.66, 1.99, 3.25, 1.49, 2.49, 0.69, 1.38,
                 1.43, 2.98, 3.68, 2.51, 1.27, 0.9, 3.77, 0.62, 0.97, 0.79]

# print(jungle_champions.__len__(), jungle_weight.__len__())

# 中路角色
mid_Sylas = champion("Sylas", ["Con", "Elec"], "mid", ["flash", "tp", "ignite"])
mid_Leblanc = champion("Leblanc", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Yone = champion("Yone", ["Con", "FF", "GotU"], "mid", ["flash", "tp", "ignite"])
mid_Hwei = champion("Hwei", ["AC"], "mid", ["flash", "tp", "barrier"])
mid_Ahri = champion("Ahri", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Yassuo = champion("Yassuo", ["Con", "FF", "GotU"], "mid", ["flash", "tp", "ignite"])
mid_Vex = champion("Vex", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Zed = champion("Zed", ["Con", "Elec"], "mid", ["flash", "tp", "ignite"])
mid_Lissandra = champion("Lissandra", ["Elec", "AC"], "mid", ["flash", "tp", "ignite"])
mid_Galio = champion("Galio", ["Elec", "AS"], "mid", ["flash", "tp", "ignite"])
mid_Anivia = champion("Anivia", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Tf = champion("Tf", ["Elec"], "mid", ["flash", "tp", "ignite"]) 
mid_Talon = champion("Talon", ["Con", "Elec", "PR"], "mid", ["flash", "tp", "ignite"])
mid_Akali = champion("Akali", ["Con", "Elec", "FF"], "mid", ["flash", "tp", "ignite"])
mid_Cassiopeia = champion("Cassiopeia", ["Con"], "mid", ["flash", "tp", "barrier"])
mid_Xerath = champion("Xerath", ["AC"], "mid", ["flash", "tp", "barrier"])
mid_Orianna = champion("Orianna", ["PR", "SA"], "mid", ["flash", "tp", "barrier", "cleanse"])
mid_ASol = champion("ASol", ["AC"], "mid", ["flash", "tp", "exhaust"])
mid_Renecton = champion("Renecton", ["Con", "PTA"], "mid", ["flash", "tp", "ignite"])
mid_Syndra = champion("Syndra", ["FS", "Elec"], "mid", ["flash", "tp", "ghost", "barrier"])
mid_Naafiri = champion("Naafiri", ["FS", "Elec"], "mid", ["flash", "tp", "ignite"])
mid_Katerina = champion("Katerina", ["Con", "Elec"], "mid", ["flash", "tp", "ignite"])
mid_Nunu = champion("Nunu", ["Elec"], "mid", ["flash", "cleanse", "ignite"])
mid_Ryze = champion("Ryze", ["PR"], "mid", ["flash", "tp", "ignite"])
mid_Zoe = champion("Zoe", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Fizz = champion("Fizz", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Diana = champion("Diana", ["Con", "Elec", "PR"], "mid", ["flash", "tp", "ignite"])
mid_Jayce = champion("Jayce", ["PR", "Con"], "mid", ["flash", "tp", "ignite"])
mid_Victor = champion("Victor", ["PR", "SA", "FS"], "mid", ["flash", "tp", "ghost"])
mid_Aurora = champion("Aurora", ["Elec"], "mid", ["flash", "tp", "ignite"])
mid_Garen = champion("Garen", ["Con"], "mid", ["flash", "tp", "ignite"])
mid_Annie = champion("Annie", ["Elec", "FS"], "mid", ["flash", "tp", "ignite"])
mid_Malzahar = champion("Malzahar", ["AC", "SA"], "mid", ["flash", "tp", "ignite"])
mid_Neeko = champion("Neeko", ["Elec", "AC"], "mid", ["flash", "tp", "ignite"])
mid_Qiyanna = champion("Qiyanna", ["FS", "Elec", "Con"], "mid", ["flash", "tp", "ignite"])
mid_Veigar = champion("Veigar", ["AC", "FS"], "mid", ["flash", "tp", "barrier"])
mid_Vladimir = champion("Vladimir", ["SA", "PR", "GotU", "Elec"], "mid", ["flash", "ghost", "ignite"])
mid_Akshan = champion("Akshan", ["PTA"], "mid", ["flash", "tp", "ignite"])
mid_Nasus = champion("Nasus", ["SA", "FF"], "mid", ["flash", "tp", "ghost"])
mid_Patheon = champion("Patheon", ["Con", "PTA"], "mid", ["flash", "tp", "ignite"])
mid_Taliyah = champion("Taliyah", ["PR", "FS"], "mid", ["flash", "tp", "ignite"])
mid_Gragas = champion("Gragas", ["PR", "AC"], "mid", ["flash", "tp", "ignite"])
mid_Irelia = champion("Irelia", ["Con", "PTA"], "mid", ["flash", "tp", "ignite"])
mid_Kennen = champion("Kennen", ["Elec", "SA"], "mid", ["flash", "tp", "ignite"])
mid_Ekko = champion("Ekko", ["Elec", "HoB"], "mid", ["flash", "tp", "ignite"])
mid_Swain = champion("Swain", ["Con"], "mid", ["flash", "tp", "ghost"])
mid_Malphite = champion("Malphite", ["AC", "GotU"], "mid", ["flash", "tp", "ignite"])
mid_Lux = champion("Lux", ["AC"], "mid", ["flash", "tp", "barrier"])
mid_Azir = champion("Azir", ["Con", "FF", "GotU"], "mid", ["flash", "tp", "ignite"])
mid_Quinn = champion("Quinn", ["PTA", "Elec"], "mid", ["flash", "tp", "ignite"])
mid_Kassadin = champion("Kassadin", ["FF", "Elec"], "mid", ["flash", "tp", "ignite"])
mid_Smolder = champion("Smolder", ["FF", "GotU"], "mid", ["flash", "tp", "barrier"])
mid_Rumble = champion("Rumble", ["AC"], "mid", ["flash", "tp", "ignite"])
mid_Tristana = champion("Tristana", ["FF", "PTA"], "mid", ["flash", "tp", "ignite"])
mid_Ziggs = champion("Ziggs", ["AC"], "mid", ["flash", "tp", "ignite"])
mid_Lucian = champion("Lucian", ["PTA", "FS"], "mid", ["flash", "tp", "barrier"])
mid_Corgi = champion("Corgi", ["FF", "Con"], "mid", ["flash", "tp", "ignite"])
mid_Zeri = champion("Zeri", ["FF"], "mid", ["flash", "tp", "barrier"])

mid_champions = [mid_Sylas, mid_Leblanc, mid_Yone, mid_Hwei, mid_Ahri, mid_Yassuo, mid_Vex, mid_Zed, mid_Lissandra, mid_Galio,
                 mid_Anivia, mid_Tf, mid_Talon, mid_Akali, mid_Cassiopeia, mid_Xerath, mid_Orianna, mid_ASol, mid_Renecton,
                 mid_Syndra, mid_Naafiri, mid_Katerina, mid_Nunu, mid_Ryze, mid_Zoe, mid_Fizz, mid_Diana, mid_Jayce, mid_Victor,
                 mid_Aurora, mid_Garen, mid_Annie, mid_Malzahar, mid_Neeko, mid_Qiyanna, mid_Vladimir, mid_Veigar, mid_Nasus, 
                 mid_Patheon, mid_Akshan, mid_Gragas, mid_Irelia, mid_Taliyah, mid_Kennen, mid_Ekko, mid_Swain, top_Malphite,
                 mid_Lux, mid_Azir, mid_Quinn, mid_Kassadin, mid_Smolder, mid_Rumble, mid_Tristana, mid_Ziggs, mid_Lucian, mid_Corgi, mid_Zeri]

mid_weight = [11.92, 9.45, 17.06, 7.8, 8.85, 8.31, 4.53, 8.97, 5.67, 3.71, 2.34, 3.83, 3.17, 6.78, 1.66, 3.77, 5.52, 2.19, 1.11, 4.18, 1.45, 3.82,
              1.09, 2.41, 2.54, 2.06, 2.23, 1.6, 2.42, 2.38, 1.28, 0.99, 1.89, 0.82, 1.89, 2.65, 1.51, 1.82, 1.03, 1.38, 0.64,
              2.83, 1.28, 0.78, 1.22, 0.56, 0.89, 1.51, 2.03, 0.52, 1.32, 4.35, 0.61, 2.7, 0.86, 0, 1.61, 0.52]

# print(mid_champions.__len__(), mid_weight.__len__())

# 下路角色
ad_Jhin = champion("Jhin", ["FF"], "bot", ["flash", "barrier", "cleanse"])
ad_Kaisa = champion("Kaisa", ["FF", "PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Jinx = champion("Jinx", ["PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Ashe = champion("Ashe", ["FF", "PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Ziggs = champion("Ziggs", ["AC"], "bot", ["flash", "tp", "barrier"])
ad_Swain = champion("Swain", ["Con"], "bot", ["flash", "exhaust", "ghost"])
ad_Ez = champion("Ez", ["Con", "PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Lucian = champion("Lucian", ["PTA", "FS"], "bot", ["flash", "cleanse", "barrier"])
ad_Kogmaw = champion("Kogmaw", ["PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Mf = champion("Mf", ["PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Twitch = champion("Twitch", ["PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Samira = champion("Samira", ["Con"], "bot", ["flash", "barrier", "cleanse"])
ad_Draven = champion("Draven", ["PTA", "HoB"], "bot", ["flash", "barrier", "cleanse"])
ad_Kaitlyn = champion("Kaitlyn", ["FF", "PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Seraphine = champion("Seraphine", ["SA"], "bot", ["flash", "barrier", "tp"])
ad_Sivir = champion("Sivir", ["FF", "FS"], "bot", ["flash", "barrier", "tp"])
ad_Kalista = champion("Kalista", ["PTA", "HoB"], "bot", ["flash", "barrier", "cleanse"])
ad_Varus = champion("Varus", ["PTA", "AC"], "bot", ["flash", "barrier", "cleanse"])
ad_Xayah = champion("Xayah", ["PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Zeri = champion("Zeri", ["FF"], "bot", ["flash", "barrier", "cleanse"])
ad_Aphelios = champion("Aphelios", ["FF", "PTA"], "bot", ["flash", "barrier", "cleanse"])
ad_Hwei = champion("Hwei", ["AC"], "bot", ["flash", "tp", "barrier"])
ad_Smolder = champion("Smolder", ["FF"], "bot", ["flash", "tp", "barrier"])
ad_Nilah = champion("Nilah", ["Con"], "bot", ["flash", "barrier", "cleanse"])
ad_Vayne = champion("Vayne", ["PTA", "FF", "GotU"], "bot", ["flash", "barrier", "cleanse"])
ad_Tristana = champion("Tristana", ["FF", "PTA"], "bot", ["flash", "barrier", "cleanse"])

ad_champions = [ad_Jhin, ad_Kaisa, ad_Jinx, ad_Ashe, ad_Ziggs, ad_Swain, ad_Ez, ad_Lucian, ad_Kogmaw, ad_Mf, ad_Twitch, ad_Samira,
                ad_Draven, ad_Kaitlyn, ad_Seraphine, ad_Sivir, ad_Kalista, ad_Varus, ad_Xayah, ad_Zeri, ad_Aphelios, ad_Hwei, ad_Smolder, ad_Vayne, ad_Tristana]

ad_weight = [38.6, 26.91, 19.52, 12.05, 9.7, 0.67, 19.76, 8.63, 1.45, 7.43, 1.44, 4.02, 2.75, 9.76, 0.56, 2.77, 1.56, 6.37, 2.58, 4.59, 3.82, 1.32, 5.87, 1.52, 0.69]

# print(ad_champions.__len__(), ad_weight.__len__())

# 輔助角色
support_Poppy = champion("Poppy", ["HoB", "AS"], "support", ["flash", "exhaust", "ignite"])
support_Sena = champion("Sena", ["GotU", "SA"], "support", ["flash", "heal", "exhaust"])
support_Pyke = champion("Pyke", ["HoB"], "support", ["flash", "exhaust", "ignite"])
support_Xerath = champion("Xerath", ["AC", "FS"], "support", ["flash", "heal", "exhaust"])
support_Lulu = champion("Lulu", ["SA"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Leona = champion("Leona", ["AS"], "support", ["flash", "exhaust", "ignite"])
support_Leblanc = champion("Leblanc", ["Elec", "FS"], "support", ["flash", "exhaust", "ignite"])
support_Shaco = champion("Shaco", ["AC", "HoB"], "support", ["flash", "exhaust", "ignite"])
support_Bard = champion("Bard", ["Elec", "Guard"], "support", ["flash", "exhaust", "ignite", "heal"])
support_Taric = champion("Taric", ["GA"], "support", ["flash", "exhaust", "ignite"])
support_Blitz = champion("Blitz", ["GA"], "support", ["flash", "exhaust", "ignite"])
support_Nautilus = champion("Nautilus", ["GA", "AS"], "support", ["flash", "exhaust", "ignite"])
support_Thresh = champion("Thresh", ["GA", "AS"], "support", ["flash", "exhaust", "ignite"])
support_Seraphine = champion("Seraphine", ["SA"], "support", ["flash", "exhaust", "ignite", "heal"])
support_Barum = champion("Barum", ["Guard"], "support", ["flash", "exhaust", "ignite"])
support_Rell = champion("Rell", ["GA", "AS"], "support", ["flash", "exhaust", "ignite"])
support_Alistar = champion("Alistar", ["PR", "AS"], "support", ["flash", "exhaust", "ignite"])
support_Zilean = champion("Zilean", ["AC", "SA"], "support", ["flash", "heal", "exhaust"])
support_Shen = champion("Shen", ["AS"], "support", ["flash", "exhaust", "ignite"])
support_Neeko = champion("Neeko", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Karma = champion("Karma", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Rakan = champion("Rakan", ["Guard"], "support", ["flash", "exhaust", "ignite"])
support_Lux = champion("Lux", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Maokai = champion("Maokai", ["AS"], "support", ["flash", "exhaust", "ignite"])
support_Hwei = champion("Hwei", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Soraka = champion("Soraka", ["SA"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Sona = champion("Sona", ["SA"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Nami = champion("Nami", ["SA"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Camille = champion("Camille", ["HoB"], "support", ["flash", "exhaust", "ignite"])
support_Velkoz = champion("Velkoz", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Millio = champion("Millio", ["SA"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Yuumi = champion("Yuumi", ["SA"], "support", ["heal", "exhaust", "ignite"])
support_Zac = champion("Zac", ["AS"], "support", ["flash", "exhaust", "ignite"])
support_Morgana = champion("Morgana", ["AC"], "support", ["flash", "exhaust", "ignite"])
support_Galio = champion("Galio", ["AS"], "support", ["flash", "exhaust", "ignite"])
support_Brand = champion("Brand", ["AC", "DH"], "support", ["flash", "exhaust", "ignite"])
support_Zoe = champion("Zoe", ["Elec"], "support", ["flash", "exhaust", "ignite"])
support_Pantheon = champion("Patheon", ["PTA"], "support", ["flash", "exhaust", "ignite"])
support_Tahmkench = champion("Tahmkench", ["GotU", "Guard"], "support", ["flash", "exhaust", "ignite"])
support_Swain = champion("Swain", ["Con", "Elec"], "support", ["flash", "exhaust", "ignite"])
support_Janna = champion("Janna", ["AC", "SA"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Amumu = champion("Amumu", ["AS"], "support", ["flash", "exhaust", "ignite"])
support_Zyra = champion("Zyra", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Heimer = champion("Heimer", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Fiddlestick = champion("Fiddlestick", ["AC"], "support", ["flash", "heal", "exhaust", "ignite"])
support_Renata = champion("Renata", ["Guard"], "support", ["flash", "exhaust", "ignite", "heal"])
support_Veigar = champion("Veigar", ["AC", "FS"], "support", ["flash", "exhaust", "ignite", "heal"])


support_champions = [support_Poppy, support_Sena, support_Pyke, support_Xerath, support_Lulu, support_Leblanc, support_Shaco, support_Bard,
                     support_Taric, support_Blitz, support_Nautilus, support_Thresh, support_Seraphine, support_Barum, support_Rell, support_Alistar, 
                     support_Zilean, support_Shen, support_Neeko, support_Karma, support_Rakan, support_Lux, support_Maokai, support_Hwei, 
                     support_Soraka, support_Sona, support_Nami, support_Camille, support_Velkoz, support_Millio, support_Yuumi, support_Zac, 
                     support_Morgana, support_Galio, support_Brand, support_Zoe, support_Pantheon, support_Swain, support_Janna, support_Amumu, 
                     support_Zyra, support_Heimer, support_Fiddlestick, support_Renata, support_Veigar]

support_weight = [7.99, 10.98, 7.63, 9.31, 12.78, 1.3, 2.21, 4.69, 0.85, 10.75, 11.84, 12.37, 4.94, 5.34, 6.15, 6.43, 2.25, 0.77, 1.81, 8.22, 5, 5.88,
                  2.19, 1.56, 2.86, 1.03, 2.93, 1.45, 1.52, 2.31, 5.74, 1.07, 3.29, 0.55, 1.17, 0.62, 1.69, 1.34, 1.27, 1.09, 2.44, 0.56, 0.68, 0.66, 0.59]

# print(support_champions.__len__(), support_weight.__len__())