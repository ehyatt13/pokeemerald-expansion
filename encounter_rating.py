class Pokemon:
    def __init__(self, name, index, values, type_1, type_2, tags=None):
        self.name = name
        self.index = index
        self.values = values
        self.type_1 = type_1
        self.type_2 = type_2

        if tags is None:
            self.tags = []
        else:
            self.tags = tags

    def get_average(self):
        if not self.values:
            return 0
        return sum(self.values) / len(self.values)
    

'''
averages_list = []

averages_list.append(Pokemon("Venusaur", [4, 4]))

for mon in averages_list:
    print(mon.get_average())
'''

#"Name": Pokemon("Name", num, [ , ], "type1", "type2"),

pokemon_dict = {
    "Venusaur": Pokemon("Venusaur", 1, [4, 4], "grass", "poison", ["starter", "mega"]),
    "Charizard": Pokemon("Charizard", 2, [4, 4], "fire", "flying", ["starter", "mega"]),
    "Blastoise": Pokemon("Blastoise", 3, [4, 4], "water", "", ["starter", "mega"]),
    "Butterfree": Pokemon("Butterfree", 4, [3, 2], "bug", "flying"),
    "Beedrill": Pokemon("Beedrill", 5, [3, 3], "bug", "poison", ["mega"]),
    "Pidgeot": Pokemon("Pidgeot", 6, [3, 5], "normal", "flying", ["mega"]),
    "Raticate": Pokemon("Raticate", 7, [1, 1], "normal", ""),
    "Raticate-A": Pokemon("Raticate-A", 8, [2, 2], "dark", "normal", ["regional-form"]),
    "Fearow": Pokemon("Fearow", 9, {1, 2}, "normal", "flying"),
    "Arbok": Pokemon("Arbok", 10, {1, 1}, "poison", ""),
    "Raichu": Pokemon("Raichu", 11, {3, 3}, "electric", "", ["item-evo"]),
    "Raichu-A": Pokemon("Raichu-A", 12, {4, 5}, "electric", "psychic", ["regional-form", "normal-pre-evo", "item-evo"]),
    "Sandslash": Pokemon("Sandslash", 13, {3, 2}, "ground", ""),
    "Sandslash-A": Pokemon("Sandslash-A", 14, {4, 3}, "ice", "steel", ["regional-form", "item-evo"]),
    "Nidoqueen": Pokemon("Nidoqueen", 15, {3, 2}, "poison", "ground", ["item-evo"]),
    "Nidoking": Pokemon("Nidoking", 16, {3, 2}, "poison", "ground", ["item-evo"]),
    "Clefable": Pokemon("Clefable", 17, {3, 1}, "fairy", "", ["item-evo"]),
    "Ninetales": Pokemon("Ninetales", 18, {3, 4}, "fire", "", ["item-evo"]),
    "Ninetales-A": Pokemon("Ninetales-A", 19, {4, 5}, "ice", "fairy", ["regional-form", "item-evo"]),
    "Wigglytuff": Pokemon("Wigglytuff", 20, {2, 2}, "normal", "fairy", ["item-evo"]),
    "Vileplume": Pokemon("Vileplume", 21, {3, 2}, "grass", "poison", ["item-evo"]),
    "Parasect": Pokemon("Parasect", 22, {2, 1}, "bug", "grass"),
    "Venomoth": Pokemon("Venomoth", 23, {2, 1}, "bug", "poison"),
    "Dugtrio": Pokemon("Dugtrio", 24, {3, 3}, "ground", ""),
    "Dugtrio-A": Pokemon("Dugtrio-A", 25, {3, 3}, "ground", "steel", ["regional-form"]),
    "Persian": Pokemon("Persian", 26, {1, 2}, "normal", ""),
    "Persian-A": Pokemon("Persian-A", 27, {2, 2}, "dark", "", ["regional-form"]),
    "Golduck": Pokemon("Golduck", 28, {3, 1}, "water", ""),
    "Arcanine": Pokemon("Arcanine", 29, {3, 4}, "fire", "", ["item-evo"]),
    "Arcanine-H": Pokemon("Arcanine-H", 30, {4, 5}, "fire", "rock", ["regional-form", "item-evo"]),
    "Poliwrath": Pokemon("Poliwrath", 31, {3, 4}, "water", "fighting", ["item-evo"]),
    "Alakazam": Pokemon("Alakazam", 32, {4, 5}, "psychic", "", ["mega", "trade-evo"]),
    "Machamp": Pokemon("Machamp", 33, {3, 4}, "fighting", "", ["trade-evo"]),
    "Victreebel": Pokemon("Victreebel", 34, {3, 1}, "grass", "poison", ["item-evo"]),
    "Tentacruel": Pokemon("Tentacruel", 35, {3, 1}, "water", "poison"),
    "Golem": Pokemon("Golem", 36, {3, 4}, "rock", "ground", ["trade-evo"]),
    "Golem-A": Pokemon("Golem-A", 37, {3, 3}, "rock", "electric", ["regional-form"]),
    "Rapidash": Pokemon("Rapidash", 38, {3, 2}, "fire", ""),
    "Rapidash-G": Pokemon("Rapidash-G", 39, {3, 3}, "psychic", "fairy"),
    "Slowbro": Pokemon("Slowbro", 40, {3, 2}, "water", "psychic", ["mega"]),
    "Slowbro-G": Pokemon("Slowbro-G", 41, {3, 3}, "poison", "psychic", ["regional-form", "item-evo"]),
    "Farfetch'd": Pokemon("Farfetch'd", 42, {1, 3}, "normal", "flying"),
    "Dodrio": Pokemon("Dodrio", 43, {2, 3}, "normal", "flying"),
    "Dewgong": Pokemon("Dewgong", 44, {3, 3}, "water", "ice"),
    "Muk": Pokemon("Muk", 45, {2, 2}, "poison", ""),
    "Muk-A": Pokemon("Muk-A", 46, {2, 2}, "poison", "dark", ["regional-form"]),
    "Cloyster": Pokemon("Cloyster", 47, {3, 1}, "water", "ice", ["item-evo"]),
    "Gengar": Pokemon("Gengar", 48, {4, 5}, "ghost", "poison", ["mega", "trade-evo"]),
    "Hypno": Pokemon("Hypno", 49, {1, 1}, "psychic", ""),
    "Kingler": Pokemon("Kingler", 50, {2, 2}, "water", ""),
    "Electrode": Pokemon("Electrode", 51, {2, 2}, "electric", ""),
    "Electrode-H": Pokemon("Electrode-H", 52, {3, 4}, "electric", "grass", ["regional-form", "item-evo"]),
    "Exeggutor": Pokemon("Exeggutor", 53, {3, 2}, "grass", "psychic", ["item-evo"]),
    "Exeggutor-A": Pokemon("Exeggutor-A", 54, {3, 2}, "grass", "dragon", ["regional-form", "normal-pre-evo", "item-evo"]),
    "Marowak": Pokemon("Marowak", 55, {2, 3}, "ground", ""),
    "Marowak-A": Pokemon("Marowak-A", 56, {3, 4}, "fire", "ghost", ["regional-form"]),
    "Hitmonlee": Pokemon("Hitmonlee", 57, {3, 4}, "fighting", ""),
    "Hitmonchan": Pokemon("Hitmonchan", 58, {3, 4}, "fighting", ""),
    "Weezing": Pokemon("Weezing", 59, {2, 2}, "poison", ""),
    "Weezing-G": Pokemon("Weezing-G", 60, {3, 4}, "poison", "fairy", ["regional-form"]),
    "Kangaskhan": Pokemon("Kangaskhan", 61, {2, 3}, "normal", "", ["mega"]),
    "Seaking": Pokemon("Seaking", 62, {2, 2}, "water", ""),
    "Starmie": Pokemon("Starmie", 63, {3, 3}, "water", "psychic", ["item-evo"]),
    "Mr.Mime": Pokemon("Mr.Mime", 64, {2, 1}, "psychic", "fairy"),
    "Jynx": Pokemon("Jynx", 65, {2, 1}, "ice", "psychic"),
    "Pinsir": Pokemon("Pinsir", 66, {3, 3}, "bug", "", ["mega"]),
    "Tauros": Pokemon("Tauros", 67, {3, 3}, "normal", ""),
    "Tauros-P-CB": Pokemon("Tauros-P-CB", 68, {3, 3}, "fighting", "", ["regional-form"]),
    "Tauros-P-BB": Pokemon("Tauros-P-BB", 69, {3, 3}, "fighting", "fire", ["regional-form"]),
    "Tauros-P-AB": Pokemon("Tauros-P-AB", 70, {3, 3}, "fighting", "water", ["regional-form"]),
    "Gyarados": Pokemon("Gyarados", 71, {4, 5}, "water", "flying", ["mega"]),
    "Lapras": Pokemon("Lapras", 72, {4, 5}, "water", "ice"),
    "Ditto": Pokemon("Ditto", 73, {1, 1}, "normal", ""),
    "Vaporeon": Pokemon("Vaporeon", 74, {4, 4}, "water", "", ["item-evo"]),
    "Jolteon": Pokemon("Jolteon", 75, {4, 4}, "electric", "", ["item-evo"]),
    "Flareon": Pokemon("Flareon", 76, {4, 4}, "fire", "", ["item-evo"]),
    "Omastar": Pokemon("Omastar", 77, {3, 3}, "rock", "water", ["fossil"]),
    "Kabutops": Pokemon("Kabutops", 78, {4, 2}, "rock", "water", ["fossil"]),
    "Aerodactyl": Pokemon("Aerodactyl", 79, {3, 3}, "rock", "flying", ["fossil", "mega"]),
    "Snorlax": Pokemon("Snorlax", 80, {4, 4}, "normal", ""),
    "Articuno": Pokemon("Articuno", 81, {4, 4}, "ice", "flying", ["legendary"]),
    "Articuno-G": Pokemon("Articuno-G", 82, {4, 4}, "psychic", "flying", ["legendary", "regional-form"]),
    "Zapdos": Pokemon("Zapdos", 83, {4, 4}, "electric", "flying", ["legendary"]),
    "Zapdos-G": Pokemon("Zapdos-G", 84, {3, 4}, "fighting", "flying", ["legendary", "regional-form"]),
    "Moltres": Pokemon("Moltres", 85, {4, 4}, "fire", "flying", ["legendary"]),
    "Moltres-G": Pokemon("Moltres-G", 86, {4, 4}, "dark", "flying", ["legendary", "regional-form"]),
    "Dragonite": Pokemon("Dragonite", 87, {4, 5}, "dragon", "flying", ["pseudo"]),
    "Mewtwo": Pokemon("Mewtwo", 88, {4, 4}, "psychic", "", ["legendary", "mega"]),
    "Mew": Pokemon("Mew", 89, {4, 3}, "psychic", "", ["mythical"]),
    "Meganium": Pokemon("Meganium", 90, {4, 4}, "grass", "", ["starter"]),
    "Typhlosion": Pokemon("Typhlosion", 91, {4, 4}, "fire", "", ["starter"]),
    "Typhlosion-H": Pokemon("Typhlosion-H", 92, {4, 5}, "fire", "ghost", ["starter", "regional-form", "normal-pre-evo"]),
    "Feraligatr": Pokemon("Feraligatr", 93, {4, 5}, "water", "", ["starter"]),
    "Furret": Pokemon("Furret", 94, {1, 1}, "normal", ""),
    "Noctowl": Pokemon("Noctowl", 95, {2, 3}, "normal", "flying"),
    "Ledian": Pokemon("Ledian", 96, {2, 2}, "bug", "flying"),
    "Ariados": Pokemon("Ariados", 97, {2, 2}, "bug", "poison"),
    "Crobat": Pokemon("Crobat", 98, {3, 3}, "poison", "flying"),
    "Lanturn": Pokemon("Lanturn", 99, {3, 2}, "water", "electric"),
    "Xatu": Pokemon("Xatu", 100, {2, 2}, "psychic", "flying"),
    "Ampharos": Pokemon("Ampharos", 101, {5, 5}, "electric", "", ["mega"]),
    "Bellossom": Pokemon("Bellossom", 102, {3, 3}, "grass", "", ["item-evo"]),
    "Azumarill": Pokemon("Azumarill", 103, {3, 3}, "water", "fairy"),
    "Sudowoodo": Pokemon("Sudowoodo", 104, {3, 2}, "rock", ""),
    "Politoed": Pokemon("Politoed", 105, {3, 2}, "water", "", ["trade-evo", "item-evo"]),
    "Jumpluff": Pokemon("Jumpluff", 106, {2, 2}, "grass", "flying"),
    "Sunflora": Pokemon("Sunflora", 107, {2, 1}, "grass", "", ["item-evo"]),
    "Quagsire": Pokemon("Quagsire", 108, {3, 2}, "water", "ground"),
    "Espeon": Pokemon("Espeon", 109, {4, 4}, "psychic", ""),
    "Umbreon": Pokemon("Umbreon", 110, {4, 4}, "dark", ""),
    "Slowking": Pokemon("Slowking", 111, {3, 3}, "water", "psychic", ["trade-evo", "item-evo"]),
    "Slowking-G": Pokemon("Slowking-G", 112, {3, 3}, "poison", "psychic", ["regional-form", "item-evo"]),
    "Unown": Pokemon("Unown", 113, {1, 1}, "psychic", ""),
    "Wobuffett": Pokemon("Wobuffett", 114, {1, 1}, "psychic", ""),
    "Forretress": Pokemon("Forretress", 115, {2, 1}, "bug", "steel"),
    "Steelix": Pokemon("Steelix", 116, {2, 2}, "steel", "ground", ["mega", "trade-evo", "item-evo"]),
    "Granbull": Pokemon("Granbull", 117, {1, 2}, "fairy", ""),
    "Qwlfish": Pokemon("Qwlfish", 118, {1, 2}, "water", "poison"),
    "Scizor": Pokemon("Scizor", 119, {4, 4}, "bug", "steel", ["mega", "trade-evo", "item-evo"]),
    "Shuckle": Pokemon("Shuckle", 120, {3, 3}, "bug", "rock"),
    "Heracross": Pokemon("Heracross", 121, {4, 4}, "bug", "fighting", ["mega"]),
    "Magcargo": Pokemon("Magcargo", 122, {3, 2}, "fire", "rock"),
    "Corsola": Pokemon("Corsola", 123, {2, 1}, "water", "rock"),
    "Octillery": Pokemon("Octillery", 124, {2, 2}, "water", ""),
    "Delibird": Pokemon("Delibird", 125, {2, 2}, "ice", "flying"),
    "Mantine": Pokemon("Mantine", 126, {2, 2}, "water", "flying"),
    "Skarmory": Pokemon("Skarmory", 127, {3, 3}, "steel", "flying"),
    "Houndoom": Pokemon("Houndoom", 128, {3, 3}, "fire", "dark", ["mega"]),
    "Kingdra": Pokemon("Kingdra", 129, {5, 5}, "water", "dragon", ["trade-evo", "item-evo"]),
    "Donphan": Pokemon("Donphan", 130, {3, 4}, "ground", ""),
    "Smeargle": Pokemon("Smeargle", 131, {2, 2}, "normal", ""),
    "Hitmontop": Pokemon("Hitmontop", 132, {3, 4}, "fighting", ""),
    "Miltank": Pokemon("Miltank", 133, {2, 3}, "normal", ""),
    "Blissey": Pokemon("Blissey", 134, {3, 3}, "normal", ""),
    "Raikou": Pokemon("Raikou", 135, {4, 4}, "electric", "", ["legendary"]),
    "Entei": Pokemon("Entei", 136, {4, 4}, "fire", "", ["legendary"]),
    "Suicune": Pokemon("Suicune", 137, {4, 4}, "water", "", ["legendary"]),
    "Tyranitar": Pokemon("Tyranitar", 138, {4, 5}, "rock", "dark", ["pseudo", "mega"]),
    "Lugia": Pokemon("Lugia", 139, {4, 4}, "psychic", "flying", ["box-art", "legendary"]),
    "Ho-oh": Pokemon("Ho-oh", 140, {4, 4}, "fire", "flying", ["box-art", "legendary"]),
    "Celebi": Pokemon("Celebi", 141, {4, 3}, "grass", "psychic", ["mythical"]),
    "Sceptile": Pokemon("Sceptile", 142, {5, 5}, "grass", "", ["starter", "mega"]),
    "Blaziken": Pokemon("Blaziken", 143, {5, 5}, "fire", "fighting", ["starter", "mega"]),
    "Swampert": Pokemon("Swampert", 144, {4, 5}, "water", "ground", ["starter", "mega"]),
    "Mightyena": Pokemon("Mightyena", 145, {2, 3}, "dark", ""),
    "Linoone": Pokemon("Linoone", 146, {1, 2}, "normal", ""),
    "Beautifly": Pokemon("Beautifly", 147, {2, 2}, "bug", "flying"),
    "Dustox": Pokemon("Dustox", 148, {2, 2}, "bug", "poison"),
    "Ludicolo": Pokemon("Ludicolo", 149, {3, 3}, "water", "grass", ["item-evo"]),
    "Shiftry": Pokemon("Shiftry", 150, {3, 3}, "grass", "dark", ["item-evo"]),
    "Swellow": Pokemon("Swellow", 151, {4, 4}, "normal", "flying"),
    "Pelipper": Pokemon("Pelipper", 152, {3, 3}, "water", "flying"),
    "Gardevoir": Pokemon("Gardevoir", 153, {5, 4}, "psychic", "fairy", ["mega"]),
    "Masquerain": Pokemon("Masquerain", 154, {2, 2}, "bug", "flying"),
    "Breloom": Pokemon("Breloom", 155, {4, 4}, "grass", "fighting"),
    "Slaking": Pokemon("Slaking", 156, {3, 3}, "normal", ""),
    "Ninjask": Pokemon("Ninjask", 157, {2, 2}, "bug", "flying"),
    "Shedinja": Pokemon("Shedinja", 158, {2, 2}, "bug", "ghost"),
    "Exploud": Pokemon("Exploud", 159, {2, 2}, "normal", ""),
    "Hariyama": Pokemon("Hariyama", 160, {3, 3}, "fighting", ""),
    "Delcatty": Pokemon("Delcatty", 161, {1, 1}, "normal", "", ["item-evo"]),
    "Sableye": Pokemon("Sableye", 162, {3, 2}, "dark", "ghost", ["mega"]),
    "Mawile": Pokemon("Mawile", 163, {2, 2}, "steel", "fairy", ["mega"]),
    "Aggron": Pokemon("Aggron", 164, {4, 3}, "steel", "rock", ["mega"]),
    "Medicham": Pokemon("Medicham", 165, {3, 3}, "fighting", "psychic", ["mega"]),
    "Manectric": Pokemon("Manectric", 166, {3, 3}, "electric", "", ["mega"]),
    "Plusle": Pokemon("Plusle", 167, {1, 2}, "electric", ""),
    "Minun": Pokemon("Minun", 168, {1, 2}, "electric", ""),
    "Volbeat": Pokemon("Volbeat", 169, {1, 2}, "bug", ""),
    "Illumise": Pokemon("Illumise", 170, {1, 2}, "bug", ""),
    "Swalot": Pokemon("Swalot", 171, {2, 2}, "poison", ""),
    "Sharpedo": Pokemon("Sharpedo", 172, {3, 3}, "water", "dark", ["mega"]),
    "Wailord": Pokemon("Wailord", 173, {2, 2}, "water", ""),
    "Camerupt": Pokemon("Camerupt", 174, {3, 4}, "fire", "ground", ["mega"]),
    "Torkoal": Pokemon("Torkoal", 175, {3, 4}, "fire", ""),
    "Grumpig": Pokemon("Grumpig", 176, {2, 2}, "psychic", ""),
    "Spinda": Pokemon("Spinda", 177, {1, 2}, "normal", ""),
    "Flygon": Pokemon("Flygon", 178, {5, 5}, "ground", "dragon"),
    "Cacturne": Pokemon("Cacturne", 179, {2, 3}, "grass", "dark"),
    "Altaria": Pokemon("Altaria", 180, {5, 4}, "dragon", "flying", ["mega"]),
    "Zangoose": Pokemon("Zangoose", 181, {2, 3}, "normal", ""),
    "Seviper": Pokemon("Seviper", 182, {2, 3}, "poison", ""),
    "Lunatone": Pokemon("Lunatone", 183, {2, 2}, "rock", "psychic"),
    "Solrock": Pokemon("Solrock", 184, {2, 2}, "rock", "psychic"),
    "Whiscash": Pokemon("Whiscash", 185, {3, 2}, "water", "ground"),
    "Crawdaunt": Pokemon("Crawdaunt", 186, {3, 3}, "water", "dark"),
    "Claydol": Pokemon("Claydol", 187, {3, 3}, "ground", "psychic"),
    "Cradily": Pokemon("Cradily", 188, {3, 2}, "rock", "grass", ["fossil"]),
    "Armaldo": Pokemon("Armaldo", 189, {3, 3}, "rock", "bug", ["fossil"]),
    "Milotic": Pokemon("Milotic", 190, {4, 4}, "water", ""),
    "Castform": Pokemon("Castform", 191, {2, 1}, "normal", ""),
    "Kecleon": Pokemon("Kecleon", 192, {1, 1}, "normal", ""),
    "Banette": Pokemon("Banette", 193, {3, 3}, "ghost", "", ["mega"]),
    "Tropius": Pokemon("Tropius", 194, {2, 2}, "grass", "flying"),
    "Chimecho": Pokemon("Chimecho", 195, {1, 2}, "psychic", ""),
    "Absol": Pokemon("Absol", 196, {4, 3}, "dark", "", ["mega"]),
    "Glalie": Pokemon("Glalie", 197, {3, 4}, "ice", "", ["mega"]),
    "Walrein": Pokemon("Walrein", 198, {3, 4}, "ice", "water"),
    "Huntail": Pokemon("Huntail", 199, {2, 2}, "water", "", ["trade-evo", "item-evo"]),
    "Gorebyss": Pokemon("Gorebyss", 200, {2, 2}, "water", "", ["trade-evo", "item-evo"]),
    "Relicanth": Pokemon("Relicanth", 201, {2, 2}, "water", "rock"),
    "Luvdisc": Pokemon("Luvdisc", 202, {1, 1}, "water", ""),
    "Salamence": Pokemon("Salamence", 203, {4, 5}, "dragon", "flying", ["pseudo"]),
    "Metagross": Pokemon("Metagross", 204, {4, 5}, "steel", "psychic", ["pseudo"]),
    "Regirock": Pokemon("Regirock", 205, {4, 4}, "rock", "", ["legendary"]),
    "Regice": Pokemon("Regice", 206, {4, 4}, "ice", "", ["legendary"]),
    "Registeel": Pokemon("Registeel", 207, {4, 4}, "steel", "", ["legendary"]),
    "Latias": Pokemon("Latias", 208, {4, 4}, "dragon", "psychic", ["legendary", "mega"]),
    "Latios": Pokemon("Latios", 209, {4, 4}, "dragon", "psychic", ["legendary", "mega"]),
    "Kyogre": Pokemon("Kyogre", 210, {5, 4}, "water", "", ["box-art", "legendary", "mega"]),
    "Groudon": Pokemon("Groudon", 211, {4, 4}, "ground", "", ["box-art", "legendary", "mega"]),
    "Rayquaza": Pokemon("Rayquaza", 212, {5, 5}, "dragon", "flying", ["box-art", "legendary", "mega"]),
    "Jirachi": Pokemon("Jirachi", 213, {4, 3}, "steel", "psychic", ["mythical"]),
    "Deoxys": Pokemon("Deoxys", 214, {4, 4}, "psychic", "", ["mythical"]),
    "Torterra": Pokemon("Torterra", 215, {4, 5}, "grass", "ground", ["starter"]),
    "Infernape": Pokemon("Infernape", 216, {5, 5}, "fire", "fighting", ["starter"]),
    "Empoleon": Pokemon("Empoleon", 217, {4, 4}, "water", "steel", ["starter"]),
    "Staraptor": Pokemon("Staraptor", 218, {5, 5}, "normal", "flying"),
    "Bibarel": Pokemon("Bibarel", 219, {2, 2}, "normal", "water"),
    "Kricketune": Pokemon("Kricketune", 220, {3, 3}, "bug", ""),
    "Luxray": Pokemon("Luxray", 221, {4, 4}, "electric", ""),
    "Roserade": Pokemon("Roserade", 222, {4, 4}, "grass", "poison", ["item-evo"]),
    "Rampardos": Pokemon("Rampardos", 223, {4, 4}, "rock", "", ["fossil"]),
    "Bastiodon": Pokemon("Bastiodon", 224, {4, 4}, "rock", "steel", ["fossil"]),
    "Wormadam": Pokemon("Wormadam", 225, {1, 1}, "bug", ""),
    "Mothim": Pokemon("Mothim", 226, {1, 1}, "bug", "flying"),
    "Vespiquen": Pokemon("Vespiquen", 227, {3, 1}, "bug", "flying"),
    "Pachirisu": Pokemon("Pachirisu", 228, {2, 2}, "electric", ""),
    "Floatzel": Pokemon("Floatzel", 229, {3, 3}, "water", ""),
    "Cherrim": Pokemon("Cherrim", 230, {2, 1}, "grass", ""),
    "Gastrodon": Pokemon("Gastrodon", 231, {4, 2}, "water", "ground"),
    "Ambipom": Pokemon("Ambipom", 232, {2, 2}, "normal", ""),
    "Drifblim": Pokemon("Drifblim", 233, {3, 3}, "ghost", "flying"),
    "Lopunny": Pokemon("Lopunny", 234, {3, 3}, "normal", "", ["mega"]),
    "Mismagius": Pokemon("Mismagius", 235, {4, 3}, "ghost", "", ["item-evo"]),
    "Honchkrow": Pokemon("Honchkrow", 236, {3, 3}, "dark", "flying", ["item-evo"]),
    "Purugly": Pokemon("Purugly", 237, {1, 2}, "normal", ""),
    "Skuntank": Pokemon("Skuntank", 238, {2, 2}, "poison", "dark"),
    "Bronzong": Pokemon("Bronzong", 239, {3, 2}, "steel", "psychic"),
    "Chatot": Pokemon("Chatot", 240, {1, 1}, "normal", "flying"),
    "Spiritomb": Pokemon("Spiritomb", 241, {3, 3}, "ghost", "dark"),
    "Garchomp": Pokemon("Garchomp", 242, {4, 4}, "dragon", "ground", ["pseudo", "mega"]),
    "Lucario": Pokemon("Lucario", 243, {4, 5}, "fighting", "steel", ["mega"]),
    "Hippowdon": Pokemon("Hippowdon", 244, {3, 3}, "ground", ""),
    "Drapion": Pokemon("Drapion", 245, {3, 3}, "poison", "dark"),
    "Toxicroak": Pokemon("Toxicroak", 246, {4, 4}, "poison", "fighting"),
    "Carnivine": Pokemon("Carnivine", 247, {2, 3}, "grass", ""),
    "Lumineon": Pokemon("Lumineon", 248, {3, 3}, "water", ""),
    "Abomasnow": Pokemon("Abomasnow", 249, {4, 3}, "grass", "ice", ["mega"]),
    "Weavile": Pokemon("Weavile", 250, {4, 3}, "ice", "dark", ["item-evo"]),
    "Magnezone": Pokemon("Magnezone", 251, {3, 3}, "electric", "steel", ["item-evo"]),
    "Lickilicky": Pokemon("Lickilicky", 252, {2, 3}, "normal", ""),
    "Rhyperior": Pokemon("Rhyperior", 253, {4, 4}, "ground", "rock", ["trade-evo", "item-evo"]),
    "Tangrowth": Pokemon("Tangrowth", 254, {3, 3}, "grass", ""),
    "Electivire": Pokemon("Electivire", 255, {4, 4}, "electric", "", ["trade-evo", "item-evo"]),
    "Magmortar": Pokemon("Magmortar", 256, {4, 4}, "fire", "", ["trade-evo", "item-evo"]),
    "Togekiss": Pokemon("Togekiss", 257, {4, 4}, "fairy", "flying", ["item-evo"]),
    "Yanmega": Pokemon("Yanmega", 258, {4, 4}, "bug", "flying"),
    "Leafeon": Pokemon("Leafeon", 259, {4, 4}, "grass", "", ["item-evo"]),
    "Glaceon": Pokemon("Glaceon", 260, {4, 4}, "ice", "", ["item-evo"]),
    "Gliscor": Pokemon("Gliscor", 261, {4, 4}, "ground", "flying", ["item-evo"]),
    "Mamoswine": Pokemon("Mamoswine", 262, {4, 4}, "ice", "ground"),
    "Porygon-Z": Pokemon("Porygon-Z", 263, {3, 4}, "normal", "", ["trade-evo", "item-evo"]),
    "Gallade": Pokemon("Gallade", 264, {4, 4}, "psychic", "fighting", ["mega", "item-evo"]),
    "Probopass": Pokemon("Probopass", 265, {3, 3}, "rock", "steel", ["item-evo"]),
    "Dusknoir": Pokemon("Dusknoir", 266, {4, 4}, "ghost", "", ["trade-evo", "item-evo"]),
    "Froslass": Pokemon("Froslass", 267, {5, 4}, "ice", "ghost", ["item-evo"]),
    "Rotom": Pokemon("Rotom", 268, {3, 3}, "electric", "ghost"),
    "Uxie": Pokemon("Uxie", 269, {3, 3}, "psychic", "", ["legendary"]),
    "Mesprit": Pokemon("Mesprit", 270, {3, 3}, "psychic", "", ["legendary"]),
    "Azelf": Pokemon("Azelf", 271, {3, 3}, "psychic", "", ["legendary"]),
    "Dialga": Pokemon("Dialga", 272, {4, 4}, "steel", "dragon", ["box-art", "legendary"]),
    "Palkia": Pokemon("Palkia", 273, {4, 4}, "water", "dragon", ["box-art", "legendary"]),
    "Heatran": Pokemon("Heatran", 274, {4, 4}, "fire", "steel", ["legendary"]),
    "Regigigas": Pokemon("Regigigas", 275, {4, 4}, "normal", "", ["legendary"]),
    "Giratina": Pokemon("Giratina", 276, {5, 4}, "ghost", "dragon", ["box-art", "legendary"]),
    "Cresselia": Pokemon("Cresselia", 277, {4, 4}, "psychic", "", ["legendary"]),
    "Phione": Pokemon("Phione", 278, {3, 3}, "water", "", ["mythical"]),
    "Manaphy": Pokemon("Manaphy", 279, {3, 3}, "water", "", ["mythical"]),
    "Darkrai": Pokemon("Darkrai", 280, {4, 4}, "dark", "", ["mythical"]),
    "Shaymin": Pokemon("Shaymin", 281, {4, 4}, "grass", "", ["mythical"]),
    "Arceus": Pokemon("Arceus", 282, {4, 4}, "normal", "", ["mythical"]),
    "Victini": Pokemon("Victini", 283, {4, 4}, "psychic", "fire", ["mythical"]),
    "Serperior": Pokemon("Serperior", 284, {4, 3}, "grass", "", ["starter"]),
    "Emboar": Pokemon("Emboar", 285, {3, 3}, "fire", "fighting", ["starter"]),
    "Samurott": Pokemon("Samurott", 286, {4, 4}, "water", "", ["starter"]),
    "Samurott-H": Pokemon("Samurott-H", 287, {4, 4}, "water", "dark", ["starter", "regional-form", "normal-pre-evo"]),
    "Watchog": Pokemon("Watchog", 288, {1, 1}, "normal", ""),
    "Stoutland": Pokemon("Stoutland", 289, {2, 2}, "normal", ""),
    "Liepard": Pokemon("Liepard", 290, {2, 2}, "dark", ""),
    "Simisage": Pokemon("Simisage", 291, {2, 2}, "grass", "", ["item-evo"]),
    "Simisear": Pokemon("Simisear", 292, {2, 2}, "fire", "", ["item-evo"]),
    "Simipour": Pokemon("Simipour", 293, {2, 2}, "water", "", ["item-evo"]),
    "Musharna": Pokemon("Musharna", 294, {3, 2}, "psychic", "", ["item-moon"]),
    "Unfezant": Pokemon("Unfezant", 295, {3, 2}, "normal", "flying"),
    "Zebstrika": Pokemon("Zebstrika", 296, {3, 4}, "electric", ""),
    "Gigalith": Pokemon("Gigalith", 297, {3, 4}, "rock", "", ["trade-evo"]),
    "Swoobat": Pokemon("Swoobat", 298, {3, 3}, "psychic", "flying"),
    "Excadrill": Pokemon("Excadrill", 299, {4, 4}, "ground", "steel"),
    "Audino": Pokemon("Audino", 300, {3, 3}, "normal", "", ["mega"]),
    "Conkeldurr": Pokemon("Conkeldurr", 301, {3, 3}, "fighting", "", ["trade-evo"]),
    "Seismitoad": Pokemon("Seismitoad", 302, {3, 2}, "water", "ground"),
    "Sawk": Pokemon("Sawk", 303, {2, 2}, "fighting", ""),
    "Throh": Pokemon("Throh", 304, {2, 2}, "fighting", ""),
    "Leavanny": Pokemon("Leavanny", 305, {4, 3}, "bug", "grass"),
    "Scolipede": Pokemon("Scolipede", 306, {3, 3}, "bug", "poison"),
    "Whimsicott": Pokemon("Whimsicott", 307, {3, 2}, "grass", "", ["item-evo"]),
    "Lilligant": Pokemon("Lilligant", 308, {3, 2}, "grass", "", ["item-evo"]),
    "Lilligant-H": Pokemon("Lilligant-H", 309, {4, 4}, "grass", "fighting", ["regional-form", "normal-pre-evo", "item-evo"]),
    "Basculin": Pokemon("Basculin", 310, {2, 2}, "water", ""),
    "Krookodile": Pokemon("Krookodile", 311, {4, 4}, "ground", "dark"),
    "Darmanitan": Pokemon("Darmanitan", 312, {2, 3}, "fire", ""),
    "Darmanitan-G": Pokemon("Darmanitan-G", 313, {3, 3}, "ice", "", ["regional-form", "item-evo"]),
    "Maractus": Pokemon("Maractus", 314, {2, 2}, "grass", "",),
    "Crustle": Pokemon("Crustle", 315, {2, 2}, "bug", "rock"),
    "Scrafty": Pokemon("Scrafty", 316, {3, 3}, "dark", "fighting"),
    "Sigilyph": Pokemon("Sigilyph", 317, {2, 2}, "psychic", "flying"),
    "Cofagrigus": Pokemon("Cofagrigus", 318, {3, 3}, "ghost", ""),
    "Carracosta": Pokemon("Carracosta", 319, {3, 2}, "water", "rock", ["fossil"]),
    "Archeops": Pokemon("Archeops", 320, {3, 3}, "rock", "flying", ["fossil"]),
    "Garbodor": Pokemon("Garbodor", 321, {2, 2}, "poison", ""),
    "Zoroark": Pokemon("Zoroark", 322, {3, 3}, "dark", ""),
    "Zoroark-H": Pokemon("Zoroark-H", 323, {4, 4}, "normal", "ghost", ["regional-form"]),
    "Cinccino": Pokemon("Cinccino", 324, {2, 2}, "normal", "", ["item-evo"]),
    "Gothitelle": Pokemon("Gothitelle", 325, {3, 3}, "psychic", ""),
    "Reuniclus": Pokemon("Reuniclus", 326, {4, 3}, "psychic", ""),
    "Swanna": Pokemon("Swanna", 327, {3, 3}, "water", "flying"),
    "Vanilluxe": Pokemon("Vanilluxe", 328, {3, 2}, "ice", ""),
    "Sawsbuck": Pokemon("Sawsbuck", 329, {2, 2}, "normal", "grass"),
    "Emolga": Pokemon("Emolga", 330, {2, 2}, "electric", "flying"),
    "Escavalier": Pokemon("Escavalier", 331, {3, 3}, "bug", "steel", ["trade-evo"]),
    "Amoongus": Pokemon("Amoongus", 332, {2, 2}, "grass", "poison"),
    "Jellicent": Pokemon("Jellicent", 333, {4, 2}, "water", "ghost"),
    "Alomomola": Pokemon("Alomomola", 334, {3, 2}, "water", ""),
    "Galvantula": Pokemon("Galvantula", 335, {3, 3}, "bug", "electric"),
    "Ferrothorn": Pokemon("Ferrothorn", 336, {3, 2}, "grass", "steel"),
    "Klinklang": Pokemon("Klinklang", 337, {3, 3}, "steel", ""),
    "Eelectross": Pokemon("Eelectross", 338, {3, 3}, "electric", "", ["item-evo"]),
    "Beheeyem": Pokemon("Beheeyem", 339, {2, 2}, "psychic", ""),
    "Chandelure": Pokemon("Chandelure", 340, {4, 4}, "ghost", "fire", ["item-evo"]),
    "Haxorus": Pokemon("Haxorus", 341, {4, 4}, "dragon", ""),
    "Beartic": Pokemon("Beartic", 342, {3, 3}, "ice", ""),
    "Cryogonal": Pokemon("Cryogonal", 343, {2, 2}, "ice", ""),
    "Accelgor": Pokemon("Accelgor", 344, {3, 3}, "bug", "", ["trade-evo"]),
    "Stunfisk": Pokemon("Stunfisk", 345, {2, 2}, "ground", "electric"),
    "Stunfisk-G": Pokemon("Stunfisk-G", 346, {2, 2}, "ground", "steel"),
    "Mienshao": Pokemon("Mienshao", 347, {2, 2}, "fighting", ""),
    "Druddigon": Pokemon("Druddigon", 348, {2, 3}, "dragon", ""),
    "Golurk": Pokemon("Golurk", 349, {3, 3}, "ground", "ghost"),
    "Bouffalant": Pokemon("Bouffalant", 350, {2, 2}, "normal", ""),
    "Braviary": Pokemon("Braviary", 351, {3, 3}, "normal", "flying"),
    "Braviary-H": Pokemon("Braviary-H", 352, {3, 4}, "psychic", "flying", ["regional-form", "normal-pre-evo"]),
    "Mandabuzz": Pokemon("Mandabuzz", 353, {2, 2}, "dark", "flying"),
    "Heatmor": Pokemon("Heatmor", 354, {2, 2}, "fire", ""),
    "Durant": Pokemon("Durant", 355, {2, 3}, "bug", "steel"),
    "Hydreigon": Pokemon("Hydreigon", 356, {5, 4}, "dark", "dragon", ["pseudo"]),
    "Volcorona": Pokemon("Volcorona", 357, {4, 4}, "bug", "fire"),
    "Cobalion": Pokemon("Cobalion", 358, {4, 4}, "steel", "fighting", ["legendary"]),
    "Terrakion": Pokemon("Terrakion", 359, {4, 4}, "rock", "fighting", ["legendary"]),
    "Virizion": Pokemon("Virizion", 360, {4, 4}, "grass", "fighting", ["legendary"]),
    "Tornadus": Pokemon("Tornadus", 361, {4, 4}, "flying", "", ["legendary"]),
    "Thundurus": Pokemon("Thundurus", 362, {4, 4}, "electric", "flying", ["legendary"]),
    "Reshiram": Pokemon("Reshiram", 363, {4, 4}, "dragon", "fire", ["box-art", "legendary"]),
    "Zekrom": Pokemon("Zekrom", 364, {4, 4}, "dragon", "electric", ["box-art", "legendary"]),
    "Landorus": Pokemon("Landorus", 365, {4, 4}, "ground", "flying", ["legendary"]),
    "Kyurem": Pokemon("Kyurem", 366, {4, 4}, "dragon", "ice", ["box-art", "legendary"]),
    "Keldeo": Pokemon("Keldeo", 367, {4, 4}, "water", "fighting", ["mythical"]),
    "Meloetta": Pokemon("Meloetta", 368, {4, 3}, "normal", "psychic", ["mythical"]),
    "Genesect": Pokemon("Genesect", 369, {4, 3}, "bug", "steel", ["mythical"]),
    "Chesnaught": Pokemon("Chesnaught", 370, {3, 4}, "grass", "fighting", ["starter"]),
    "Delphox": Pokemon("Delphox", 371, {4, 4}, "fire", "psychic", ["starter"]),
    "Greninja": Pokemon("Greninja", 372, {5, 4}, "water", "dark", ["starter"]),
    "Diggersby": Pokemon("Diggersby", 373, {2, 3}, "normal", "ground"),
    "Talonflame": Pokemon("Talonflame", 374, {3, 4}, "fire", "flying"),
    "Vivillon": Pokemon("Vivillon", 375, {2, 2}, "bug", "flying"),
    "Pyroar": Pokemon("Pyroar", 376, {2, 2}, "fire", "normal"),
    "Florges": Pokemon("Florges", 377, {3, 2}, "fairy", "", ["item-evo"]),
    "Gogoat": Pokemon("Gogoat", 378, {2, 2}, "grass", ""),
    "Pangoro": Pokemon("Pangoro", 379, {3, 3}, "fighting", "dark"),
    "Furfrou": Pokemon("Furfrou", 380, {2, 2}, "normal", ""),
    "Meowstic": Pokemon("Meowstic", 381, {3, 3}, "psychic", ""),
    "Aegislash": Pokemon("Aegislash", 382, {4, 4}, "steel", "ghost", ["item-evo"]),
    "Aromatisse": Pokemon("Aromatisse", 383, {3, 2}, "fairy", "", ["trade-evo", "item-evo"]),
    "Slurpuff": Pokemon("Slurpuff", 384, {3, 2}, "fairy", "", ["trade-evo", "item-evo"]),
    "Malamar": Pokemon("Malamar", 385, {3, 3}, "dark", "psychic"),
    "Barbaracle": Pokemon("Barbaracle", 386, {3, 2}, "rock", "water"),
    "Dragalge": Pokemon("Dragalge", 387, {3, 2}, "poison", "dragon"),
    "Clawitzer": Pokemon("Clawitzer", 388, {2, 2}, "water", ""),
    "Heliolisk": Pokemon("Heliolisk", 389, {3, 3}, "electric", "normal", ["item-evo"]),
    "Tyrantrum": Pokemon("Tyrantrum", 390, {3, 3}, "rock", "dragon", ["fossil"]),
    "Aurorus": Pokemon("Aurorus", 391, {3, 3}, "rock", "ice", ["fossil"]),
    "Sylveon": Pokemon("Sylveon", 392, {4, 4}, "fairy", ""),
    "Hawlucha": Pokemon("Hawlucha", 393, {3, 3}, "fighting", "flying"),
    "Dedenne": Pokemon("Dedenne", 394, {2, 2}, "electric", "fairy"),
    "Carbink": Pokemon("Carbink", 395, {2, 2}, "rock", "fairy"),
    "Goodra": Pokemon("Goodra", 396, {4, 4}, "dragon", "", ["pseudo"]),
    "Goodra-H": Pokemon("Goodra-H", 397, {4, 4}, "steel", "dragon", ["pseudo", "regional-form"]),
    "Klefki": Pokemon("Klefki", 398, {2, 1}, "steel", "fairy"),
    "Trevenant": Pokemon("Trevenant", 399, {3, 3}, "ghost", "grass", ["trade-evo"]),
    "Gourgeist": Pokemon("Gourgeist", 400, {3, 2}, "ghost", "grass", ["trade-evo"]),
    "Avalugg": Pokemon("Avalugg", 401, {3, 3}, "ice", ""),
    "Avalugg-H": Pokemon("Avalugg-H", 402, {3, 3}, "ice", "rock", ["regional-form", "normal-pre-evo"]),
    "Noivern": Pokemon("Noivern", 403, {4, 4}, "flying", "dragon"),
    "Xerneas": Pokemon("Xerneas", 404, {4, 4}, "fairy", "", ["box-art", "legendary"]),
    "Yveltal": Pokemon("Yveltal", 405, {4, 4}, "dark", "flying", ["box-art", "legendary"]),
    "Zygarde": Pokemon("Zygarde", 406, {4, 4}, "dragon", "ground", ["box-art", "legendary"]),
    "Diancie": Pokemon("Diancie", 407, {4, 3}, "rock", "fairy", ["mythical"]),
    "Hoopa": Pokemon("Hoopa", 408, {4, 4}, "psychic", "ghost", ["mythical"]),
    "Volcanion": Pokemon("Volcanion", 409, {4, 4}, "fire", "water", ["mythical"]),
    "Decidueye": Pokemon("Decidueye", 410, {5, 5}, "grass", "ghost", ["starter"]),
    "Decidueye-H": Pokemon("Decidueye-H", 411, {4, 5}, "grass", "fighting", ["starter", "regional-form", "normal-pre-evo"]),
    "Incineroar": Pokemon("Incineroar", 412, {3, 5}, "fire", "dark", ["starter"]),
    "Primarina": Pokemon("Primarina", 413, {5, 4}, "water", "fairy", ["starter"]),
    "Toucannon": Pokemon("Toucannon", 414, {3, 3}, "normal", "flying"),
    "Gumshoos": Pokemon("Gumshoos", 415, {2, 2}, "normal", ""),
    "Vikavolt": Pokemon("Vikavolt", 416, {4, 4}, "bug", "electric", ["item-evo"]),
    "Crabominable": Pokemon("Crabominable", 417, {3, 3}, "fighting", "ice", ["item-evo"]),
    "Oricorio": Pokemon("Oricorio", 418, {2, 2}, "flying", ""),
    "Ribombee": Pokemon("Ribombee", 419, {5, 2}, "bug", "fairy"),
    "Lycanroc": Pokemon("Lycanroc", 420, {3, 3}, "rock", ""),
    "Wishiwashi": Pokemon("Wishiwashi", 421, {3, 3}, "water", ""),
    "Toxapex": Pokemon("Toxapex", 422, {4, 2}, "poison", "water"),
    "Mudsdale": Pokemon("Mudsdale", 423, {3, 3}, "ground", ""),
    "Araquanid": Pokemon("Araquanid", 424, {4, 3}, "water", "bug"),
    "Lurantis": Pokemon("Lurantis", 425, {3, 2}, "grass", ""),
    "Shiinotic": Pokemon("Shiinotic", 426, {2, 2}, "grass", "fairy"),
    "Salazzle": Pokemon("Salazzle", 427, {4, 3}, "poison", "fire"),
    "Bewear": Pokemon("Bewear", 428, {3, 3}, "normal", "fighting"),
    "Tsareena": Pokemon("Tsareena", 429, {4, 4}, "grass", ""),
    "Comfey": Pokemon("Comfey", 430, {2, 2}, "fairy", ""),
    "Oranguru": Pokemon("Oranguru", 431, {2, 2}, "normal", "psychic"),
    "Passimian": Pokemon("Passimian", 432, {2, 2}, "fighting", ""),
    "Golisopod": Pokemon("Golisopod", 433, {4, 3}, "bug", "water"),
    "Palossand": Pokemon("Palossand", 434, {3, 3}, "ghost", "ground"),
    "Pyukumuku": Pokemon("Pyukumuku", 435, {2, 2}, "water", ""),
    "Silvally": Pokemon("Silvally", 436, {3, 3}, "normal", ""),
    "Minior": Pokemon("Minior", 437, {3, 2}, "rock", "flying"),
    "Komala": Pokemon("Komala", 438, {1, 2}, "normal", ""),
    "Turtonator": Pokemon("Turtonator", 439, {4, 4}, "fire", "dragon"),
    "Togedamaru": Pokemon("Togedamaru", 440, {3, 3}, "electric", "steel"),
    "Mimikyu": Pokemon("Mimikyu", 441, {4, 4}, "ghost", "fairy"),
    "Bruxish": Pokemon("Bruxish", 442, {3, 2}, "water", "psychic"),
    "Drampa": Pokemon("Drampa", 443, {4, 4}, "normal", "dragon"),
    "Dhelmise": Pokemon("Dhelmise", 444, {3, 3}, "ghost", "grass"),
    "Kommo-o": Pokemon("Kommo-o", 445, {4, 4}, "dragon", "fighting", ["pseudo"]),
    "Tapu-Koko": Pokemon("Tapu-Koko", 446, {4, 4}, "electric", "fairy", ["legendary"]),
    "Tapu-Lele": Pokemon("Tapu-Lele", 447, {4, 4}, "psychic", "fairy", ["legendary"]),
    "Tapu-Bulu": Pokemon("Tapu-Bulu", 448, {4, 4}, "grass", "fairy", ["legendary"]),
    "Tapu-Fini": Pokemon("Tapu-Fini", 449, {4, 4}, "water", "fairy", ["legendary"]),
    "Solgaleo": Pokemon("Solgaleo", 450, {4, 4}, "psychic", "steel", ["box-art", "legendary"]),
    "Lunala": Pokemon("Lunala", 451, {4, 4}, "psychic", "ghost", ["box-art", "legendary"]),
    "Nihilego": Pokemon("Nihilego", 452, {4, 4}, "rock", "poison", ["ultra-beast"]),
    "Buzzswole": Pokemon("Buzzswole", 453, {4, 4}, "bug", "fighting", ["ultra-beast"]),
    "Pheromosa": Pokemon("Pheromosa", 454, {4, 4}, "bug", "fighting", ["ultra-beast"]),
    "Xurkitree": Pokemon("Xurkitree", 455, {4, 4}, "electric", "", ["ultra-beast"]),
    "Celesteela": Pokemon("Celesteela", 456, {4, 4}, "steel", "flying", ["ultra-beast"]),
    "Kartana": Pokemon("Kartana", 457, {4, 4}, "grass", "steel", ["ultra-beast"]),
    "Guzzlord": Pokemon("Guzzlord", 458, {4, 4}, "dark", "dragon", ["ultra-beast"]),
    "Necrozma": Pokemon("Necrozma", 459, {4, 4}, "psychic", "", ["box-art", "legendary"]),
    "Magearna": Pokemon("Magearna", 460, {4, 3}, "steel", "fairy", ["mythical"]),
    "Marshadow": Pokemon("Marshadow", 461, {4, 4}, "fighting", "ghost", ["mythical"]),
    "Naganadel": Pokemon("Naganadel", 462, {4, 4}, "poison", "dragon", ["ultra-beast"]),
    "Stakataka": Pokemon("Stakataka", 463, {4, 4}, "rock", "steel", ["ultra-beast"]),
    "Blacephalon": Pokemon("Blacephalon", 464, {4, 4}, "fire", "ghost", ["ultra-beast"]),
    "Zeraora": Pokemon("Zeraora", 465, {3, 4}, "electric", "", ["mythical"]),
    "Melmetal": Pokemon("Melmetal", 466, {3, 4}, "steel", "", ["mythical"]),
    "Rillaboom": Pokemon("Rillaboom", 467, {4, 4}, "grass", "", ["starter"]),
    "Cinderace": Pokemon("Cinderace", 468, {4, 4}, "fire", "", ["starter"]),
    "Inteleon": Pokemon("Inteleon", 469, {3, 3}, "water", "", ["starter"]),
    "Greedent": Pokemon("Greedent", 470, {1, 3}, "normal", ""),
    "Corviknight": Pokemon("Corviknight", 471, {4, 4}, "flying", "steel"),
    "Orbeetle": Pokemon("Orbeetle", 472, {3, 4}, "bug", "psychic"),
    "Thievul": Pokemon("Thievul", 473, {2, 2}, "dark", ""),
    "Eldegoss": Pokemon("Eldegoss", 474, {2, 3}, "grass", ""),
    "Dubwool": Pokemon("Dubwool", 475, {2, 2}, "normal", ""),
    "Drednaw": Pokemon("Drednaw", 476, {3, 3}, "water", "rock"),
    "Boltund": Pokemon("Boltund", 477, {2, 2}, "electric", ""),
    "Coalossal": Pokemon("Coalossal", 478, {4, 4}, "rock", "fire"),
    "Flapple": Pokemon("Flapple", 479, {4, 4}, "grass", "dragon", ["item-evo"]),
    "Appletun": Pokemon("Appletun", 480, {4, 4}, "grass", "dragon", ["item-evo"]),
    "Sandaconda": Pokemon("Sandaconda", 481, {2, 2}, "ground", ""),
    "Cramorant": Pokemon("Cramorant", 482, {3, 3}, "flying", "water"),
    "Barraskewda": Pokemon("Barraskewda", 483, {2, 2}, "water", ""),
    "Toxtricity": Pokemon("Toxtricity", 484, {4, 4}, "electric", "poison"),
    "Centiskorch": Pokemon("Centiskorch", 485, {3, 3}, "fire", "bug"),
    "Grapploct": Pokemon("Grapploct", 486, {3, 3}, "fighting", ""),
    "Polteageist": Pokemon("Polteageist", 487, {3, 3}, "ghost", "", ["item-evo"]),
    "Hatterene": Pokemon("Hatterene", 488, {4, 4}, "psychic", ""),
    "Grimmsnarl": Pokemon("Grimmsnarl", 489, {4, 4}, "dark", "fairy"),
    "Obstagoon": Pokemon("Obstagoon", 490, {3, 3}, "dark", "normal"),
    "Perrserker": Pokemon("Perrserker", 491, {3, 3}, "steel", ""),
    "Cursola": Pokemon("Cursola", 492, {3, 3}, "ghost", ""),
    "Sirfetch'd": Pokemon("Sirfetch'd", 493, {3, 4}, "fighting", ""),
    "Mr.Rime": Pokemon("Mr.Rime", 494, {3, 4}, "ice", "psychic"),
    "Runegrigus": Pokemon("Runegrigus", 495, {3, 3}, "ground", "ghost"),
    "Alcremie": Pokemon("Alcremie", 496, {3, 3}, "fairy", ""),
    "Falinks": Pokemon("Falinks", 497, {3, 4}, "fighting", ""),
    "Pincurchin": Pokemon("Pincurchin", 498, {2, 2}, "electric", ""),
    "Frosmoth": Pokemon("Frosmoth", 499, {3, 3}, "ice", "bug"),
    "Stonjourner": Pokemon("Stonjourner", 500, {2, 2}, "rock", ""),
    "Eiscue": Pokemon("Eiscue", 501, {3, 3}, "ice", ""),
    "Indeedee": Pokemon("Indeedee", 502, {2, 2}, "psychic", "normal"),
    "Morpeko": Pokemon("Morpeko", 503, {3, 3}, "electric", "dark"),
    "Copperajah": Pokemon("Copperajah", 504, {3, 3}, "steel", ""),
    "Dracozolt": Pokemon("Dracozolt", 505, {3, 4}, "electric", "dragon", ["fossil"]),
    "Arctozolt": Pokemon("Arctozolt", 506, {3, 4}, "electric", "ice", ["fossil"]),
    "Dracovish": Pokemon("Dracovish", 507, {3, 4}, "water", "dragon", ["fossil"]),
    "Arctovish": Pokemon("Arctovish", 508, {3, 3}, "water", "ice", ["fossil"]),
    "Dragapult": Pokemon("Dragapult", 509, {4, 4}, "dragon", "ghost", ["pseudo"]),
    "Zacian": Pokemon("Zacian", 510, {4, 4}, "fairy", "", ["box-art", "legendary"]),
    "Zamazenta": Pokemon("Zamazenta", 511, {4, 4}, "fighting", "", ["box-art", "legendary"]),
    "Eternatus": Pokemon("Eternatus", 512, {4, 4}, "poison", "dragon", ["box-art", "legendary"]),
    "Urshifu": Pokemon("Urshifu", 513, {4, 5}, "fighting", "", ["legendary"]),
    "Zarude": Pokemon("Zarude", 514, {4, 4}, "dark", "grass", ["mythical"]),
    "Regieleki": Pokemon("Regieleki", 515, {4, 5}, "electric", "", ["legendary"]),
    "Regidrago": Pokemon("Regidrago", 516, {4, 4}, "dragon", "", ["legendary"]),
    "Glastrier": Pokemon("Glastrier", 517, {4, 4}, "ice", "", ["legendary"]),
    "Spectrier": Pokemon("Spectrier", 518, {4, 4}, "ghost", "", ["legendary"]),
    "Calyrex": Pokemon("Calyrex", 519, {4, 4}, "psychic", "grass", ["legendary"]),
    "Wyrrdeer": Pokemon("Wyrrdeer", 520, {3, 4}, "normal", "psychic"),
    "Kleavor": Pokemon("Kleavor", 521, {3, 5}, "bug", "rock", ["item-evo"]),
    "Ursaluna": Pokemon("Ursaluna", 522, {3, 5}, "ground", "normal", ["item-evo"]),
    "Basulegion": Pokemon("Basulegion", 523, {3, 5}, "water", "ghost"),
    "Sneasler": Pokemon("Sneasler", 524, {3, 4}, "fighting", "poison", ["item-evo"]),
    "Overqwil": Pokemon("Overqwil", 525, {3, 5}, "dark", "poison"),
    "Enamorus": Pokemon("Enamorus", 526, {3, 4}, "fairy", "flying", ["legendary"]),
    "Meowscarada": Pokemon("Meowscarada", 527, {4, 4}, "grass", "dark", ["starter"]),
    "Skeledirge": Pokemon("Skeledirge", 528, {4, 5}, "fire", "ghost", ["starter"]),
    "Quaquaval": Pokemon("Quaquaval", 529, {3, 4}, "water", "fighting", ["starter"]),
    "Oinkologne": Pokemon("Oinkologne", 530, {1, 2}, "normal", ""),
    "Spidops": Pokemon("Spidops", 531, {1, 1}, "bug", ""),
    "Lokix": Pokemon("Lokix", 532, {2, 2}, "bug", "dark"),
    "Pawmot": Pokemon("Pawmot", 533, {3, 3}, "electric", "fighting"),
    "Maushold": Pokemon("Maushold", 534, {3, 3}, "normal", ""),
    "Dachsbun": Pokemon("Dachsbun", 535, {3, 2}, "fairy", ""),
    "Arboliva": Pokemon("Arboliva", 536, {2, 2}, "grass", "normal"),
    "Squawkabilly": Pokemon("Squawkabilly", 537, {1, 2}, "normal", "flying"),
    "Garganacl": Pokemon("Garganacl", 538, {3, 3}, "rock", ""),
    "Armarouge": Pokemon("Armarouge", 539, {3, 5}, "fire", "psychic", ["item-evo"]),
    "Ceruledge": Pokemon("Ceruledge", 540, {4, 5}, "fire", "ghost", ["item-evo"]),
    "Bellibolt": Pokemon("Bellibolt", 541, {3, 4}, "electric", "", ["item-evo"]),
    "Kilowattrel": Pokemon("Kilowattrel", 542, {2, 3}, "electric", "flying"),
    "Mabosstiff": Pokemon("Mabosstiff", 543, {3, 4}, "dark", ""),
    "Grafaiai": Pokemon("Grafaiai", 544, {2, 4}, "poison", "normal"),
    "Brambleghast": Pokemon("Brambleghast", 545, {2, 3}, "grass", "ghost"),
    "Toedscruel": Pokemon("Toedscruel", 546, {3, 3}, "ground", "grass"),
    "Klawf": Pokemon("Klawf", 547, {2, 3}, "rock", ""),
    "Scovillain": Pokemon("Scovillain", 548, {3, 4}, "grass", "fire", ["item-evo"]),
    "Rabsca": Pokemon("Rabsca", 549, {3, 3}, "bug", "psychic"),
    "Espathra": Pokemon("Espathra", 550, {3, 2}, "psychic", ""),
    "Tinkaton": Pokemon("Tinkaton", 551, {3, 4}, "fairy", "steel"),
    "Wugtrio": Pokemon("Wugtrio", 552, {2, 3}, "water", ""),
    "Bombirdier": Pokemon("Bombirdier", 553, {2, 3}, "flying", "dark"),
    "Palafin": Pokemon("Palafin", 554, {3, 4}, "water", ""),
    "Revavroom": Pokemon("Revavroom", 555, {3, 3}, "steel", "poison"),
    "Cyclizar": Pokemon("Cyclizar", 556, {3, 3}, "dragon", "normal"),
    "Orthworm": Pokemon("Orthworm", 557, {3, 3}, "steel", ""),
    "Glimmora": Pokemon("Glimmora", 558, {3, 2}, "rock", "poison"),
    "Houndstone": Pokemon("Houndstone", 559, {3, 4}, "ghost", ""),
    "Flamigo": Pokemon("Flamigo", 560, {3, 2}, "flying", "fighting"),
    "Cetitan": Pokemon("Cetitan", 561, {3, 3}, "ice", "", ["item-evo"]),
    "Veluza": Pokemon("Veluza", 562, {3, 3}, "water", "psychic"),
    "Dondozo": Pokemon("Dondozo", 563, {3, 3}, "water", ""),
    "Tatsugiri": Pokemon("Tatsugiri", 564, {3, 3}, "dragon", "water"),
    "Annihilape": Pokemon("Annihilape", 565, {5, 5}, "fighting", "ghost"),
    "Clodsire": Pokemon("Clodsire", 566, {3, 3}, "poison", "ground"),
    "Farigiraf": Pokemon("Farigiraf", 567, {3, 3}, "normal", "psychic"),
    "Dudunsparce": Pokemon("Dudunsparce", 568, {2, 3}, "normal", ""),
    "Kingambit": Pokemon("Kingambit", 569, {4, 4}, "dark", "steel"),
    "Great Tusk": Pokemon("Great Tusk", 570, {4, 4}, "ground", "fighting", ["paradox"]),
    "Scream Tail": Pokemon("Scream Tail", 571, {3, 3}, "fairy", "psychic", ["paradox"]),
    "Brute Bonnet": Pokemon("Brute Bonnet", 572, {3, 3}, "grass", "dark", ["paradox"]),
    "Flutter Mane": Pokemon("Flutter Mane", 573, {5, 4}, "ghost", "fairy", ["paradox"]),
    "Slither Wing": Pokemon("Slither Wing", 574, {3, 4}, "bug", "fighting", ["paradox"]),
    "Sandy Shocks": Pokemon("Sandy Shocks", 575, {3, 3}, "electric", "ground", ["paradox"]),
    "Iron Treads": Pokemon("Iron Treads", 576, {3, 3}, "ground", "steel", ["paradox"]),
    "Iron Bundle": Pokemon("Iron Bundle", 577, {4, 4}, "ice", "water", ["paradox"]),
    "Iron Hands": Pokemon("Iron Hands", 578, {4, 4}, "fighting", "electric", ["paradox"]),
    "Iron Jugalis": Pokemon("Iron Jugalis", 579, {4, 4}, "dark", "flying", ["paradox"]),
    "Iron Moth": Pokemon("Iron Moth", 580, {3, 4}, "fire", "poison", ["paradox"]),
    "Iron Thorns": Pokemon("Iron Thorns", 581, {3, 4}, "rock", "electric", ["paradox"]),
    "Baxscalibur": Pokemon("Baxscalibur", 582, {4, 4}, "dragon", "ice", ["pseudo"]),
    "Gholdengo": Pokemon("Gholdengo", 583, {3, 4}, "steel", "ghost"),
    "Wo-Chien": Pokemon("Wo-Chien", 584, {3, 4}, "dark", "grass", ["legendary"]),
    "Chien-Pao": Pokemon("Chien-Pao", 585, {4, 4}, "dark", "ice", ["legendary"]),
    "Ting-Lu": Pokemon("Ting-Lu", 586, {3, 4}, "dark", "ground", ["legendary"]),
    "Chi-Yu": Pokemon("Chi-Yu", 587, {4, 4}, "dark", "fire", ["legendary"]),
    "Roaring Moon": Pokemon("Roaring Moon", 588, {4, 4}, "dragon", "dark", ["paradox"]),
    "Iron Valiant": Pokemon("Iron Valiant", 589, {4, 4}, "fairy", "fighting", ["paradox"]),
    "Koraidon": Pokemon("Koraidon", 590, {4, 4}, "fighting", "dragon", ["box-art", "legendary"]),
    "Miraidon": Pokemon("Miraidon", 591, {4, 4}, "electric", "dragon", ["box-art", "legendary"]),
    "Walking Wake": Pokemon("Walking Wake", 592, {4, 4}, "water", "dragon", ["paradox"]),
    "Iron Leaves": Pokemon("Iron Leaves", 593, {4, 4}, "grass", "psychic", ["paradox"]),
    "Sinistcha": Pokemon("Sinistcha", 594, {3, 4}, "grass", "ghost"),
    "Okidogi": Pokemon("Okidogi", 595, {3, 4}, "poison", "fighting", ["legendary"]),
    "Munkidori": Pokemon("Munkidori", 596, {3, 4}, "poison", "psychic", ["legendary"]),
    "Fezandipiti": Pokemon("Fezandipiti", 597, {3, 4}, "poison", "fairy", ["legendary"]),
    "Ogerpon": Pokemon("Ogerpon", 598, {4, 5}, "grass", "", ["legendary"]),
    "Archaludon": Pokemon("Archaludon", 599, {3, 5}, "steel", "dragon", ["item-evo"]),
    "Hydrapple": Pokemon("Hydrapple", 600, {4, 5}, "grass", "dragon", ["item-evo"]),
    "Gouging Fire": Pokemon("Gouging Fire", 601, {4, 4}, "fire", "dragon", ["paradox"]),
    "Raging Bolt": Pokemon("Raging Bolt", 602, {4, 4}, "electric", "dragon", ["paradox"]),
    "Iron Boulder": Pokemon("Iron Boulder", 603, {4, 4}, "rock", "psychic", ["paradox"]),
    "Iron Crown": Pokemon("Iron Crown", 604, {4, 4}, "steel", "psychic", ["paradox"]),
    "Terapagos": Pokemon("Terapagos", 605, {4, 4}, "normal", "", ["legendary"]),
    "Pecharunt": Pokemon("Pecharunt", 606, {4, 5}, "poison", "ghost", ["mythical"]),
}

s_rank = 5
a_rank = 4
b_rank = 3
c_rank = 2
d_rank = 1

print_lists = True
bans = False
banned_tags = ["starter", "legendary", "mythical"]
banned_tags_string = ', '.join(banned_tags)

s_rank_list = []
a_rank_list = []
b_rank_list = []
c_rank_list = []
d_rank_list = []

#Standard rank calculation
if bans == False:

    for mon in pokemon_dict:
        average = pokemon_dict[mon].get_average()
        if average > a_rank:
            s_rank_list.append(mon)
        elif a_rank >= average and average > b_rank:
            a_rank_list.append(mon)
        elif b_rank >= average and average > c_rank:
            b_rank_list.append(mon)
        elif c_rank >= average and average > d_rank:
            c_rank_list.append(mon)
        else:
            d_rank_list.append(mon)

#Banned rank calculation
'''
s_rank_banned_list = []
a_rank_banned_list = []
b_rank_banned_list = []
c_rank_banned_list = []
d_rank_banned_list = []
banned_list = []
'''

if bans == True:
    banned_list = []
    for mon in pokemon_dict:
        if set(banned_tags).isdisjoint(pokemon_dict[mon].tags):
            average = pokemon_dict[mon].get_average()
            if average > a_rank:
                s_rank_list.append(mon)
            elif a_rank >= average and average > b_rank:
                a_rank_list.append(mon)
            elif b_rank >= average and average > c_rank:
                b_rank_list.append(mon)
            elif c_rank >= average and average > d_rank:
                c_rank_list.append(mon)
            else:
                d_rank_list.append(mon)
        else:
            banned_list.append(mon)
    banned_string = ', '.join(banned_list)

'''
s_rank_banned_string = ', '.join(s_rank_banned_list)
a_rank_banned_string = ', '.join(a_rank_banned_list)
b_rank_banned_string = ', '.join(b_rank_banned_list)
c_rank_banned_string = ', '.join(c_rank_banned_list)
d_rank_banned_string = ', '.join(d_rank_banned_list)
banned_string = ', '.join(banned_list)
'''

s_rank_string = ', '.join(s_rank_list)
a_rank_string = ', '.join(a_rank_list)
b_rank_string = ', '.join(b_rank_list)
c_rank_string = ', '.join(c_rank_list)
d_rank_string = ', '.join(d_rank_list)

if print_lists == True:
    if bans == False:
        print("The S-Rank list is: " + s_rank_string + "\n")
        print("The A-Rank list is: " + a_rank_string + "\n")
        print("The B-Rank list is: " + b_rank_string + "\n")
        print("The C-Rank list is: " + c_rank_string + "\n")
        print("The D-Rank list is: " + d_rank_string + "\n")
    else:
        print("The banned categories of Pokémon are: " + banned_tags_string + "\n")
        print("The list of banned Pokémon is: " + banned_string + "\n")
        print("The S-Rank list without banned Pokémon is: " + s_rank_string + "\n")
        print("The A-Rank list without banned Pokémon is: " + a_rank_string + "\n")
        print("The B-Rank list without banned Pokémon is: " + b_rank_string + "\n")
        print("The C-Rank list without banned Pokémon is: " + c_rank_string + "\n")
        print("The D-Rank list without banned Pokémon is: " + d_rank_string + "\n")

s_ranked_counters = []
a_ranked_counters = []
b_ranked_counters = []
type_to_counter = "rock"
type_to_counter_2 = "fighting"
weaknesses = []
weaknesses_2 = []
combo = False
print_counters = False

def get_weakness(type):
    match type:
        case "normal":
            counter_types = ["fighting"]
        case "grass":
            counter_types = ["fire", "bug", "poison", "ice", "flying"]
        case "fire":
            counter_types = ["water", "rock", "ground"]
        case "water":
            counter_types = ["grass", "electric"]
        case "bug":
            counter_types = ["fire", "flying", "rock"]
        case "poison":
            counter_types = ["psychic", "ground"]
        case "electric":
            counter_types = ["ground"]
        case "rock":
            counter_types = ["water", "grass", "fighting", "steel", "ground"]
        case "steel":
            counter_types = ["fire", "fighting", "ground"]
        case "ground":
            counter_types = ["grass", "water"]
        case "flying":
            counter_types = ["electric", "rock", "ice"]
        case "ice":
            counter_types = ["fire", "rock", "steel", "fighting"]
        case "fighting":
            counter_types = ["psychic", "flying", "fairy"]
        case "psychic":
            counter_types = ["bug", "dark", "ghost"]
        case "ghost":
            counter_types = ["ghost", "dark"]
        case "dark":
            counter_types = ["bug", "fighting", "fairy"]
        case "dragon":
            counter_types = ["ice", "dragon", "fairy"]
        case "fairy":
            counter_types = ["steel", "poison"]
        case _:
            counter_types = []
    return counter_types

weaknesses = get_weakness(type_to_counter)
weaknesses_2 = get_weakness(type_to_counter_2)


for mon in s_rank_list:
    if pokemon_dict[mon].type_1 in weaknesses or pokemon_dict[mon].type_2 in weaknesses:
        s_ranked_counters.append(mon)

for mon in a_rank_list:
    if pokemon_dict[mon].type_1 in weaknesses or pokemon_dict[mon].type_2 in weaknesses:
        a_ranked_counters.append(mon)

for mon in b_rank_list:
    if pokemon_dict[mon].type_1 in weaknesses or pokemon_dict[mon].type_2 in weaknesses:
        b_ranked_counters.append(mon)

s_rank_counter_string = ', '.join(s_ranked_counters)
a_rank_counter_string = ', '.join(a_ranked_counters)
b_rank_counter_string = ', '.join(b_ranked_counters)


s_ranked_combo_counters = []
a_ranked_combo_counters = []
b_ranked_combo_counters = []

for mon in s_ranked_counters:
    if pokemon_dict[mon].type_1 in weaknesses_2 or pokemon_dict[mon].type_2 in weaknesses_2:
        s_ranked_combo_counters.append(mon)

for mon in a_ranked_counters:
    if pokemon_dict[mon].type_1 in weaknesses_2 or pokemon_dict[mon].type_2 in weaknesses_2:
        a_ranked_combo_counters.append(mon)

for mon in b_ranked_counters:
    if pokemon_dict[mon].type_1 in weaknesses_2 or pokemon_dict[mon].type_2 in weaknesses_2:
        b_ranked_combo_counters.append(mon)

s_rank_combo_counter_string = ', '.join(s_ranked_combo_counters)
a_rank_combo_counter_string = ', '.join(a_ranked_combo_counters)
b_rank_combo_counter_string = ', '.join(b_ranked_combo_counters)

if print_counters == True:
    if combo == False:
        print("Counters for the " + type_to_counter.upper() + " type:\n")
        print("The list of S-Rank counters is: " + s_rank_counter_string + "\n")
        print("The list of A-Rank counters is: " + a_rank_counter_string + "\n")
        print("The list of B-Rank counters is: " + b_rank_counter_string + "\n")
    else:
        print("Counters for the " + type_to_counter.upper() + " and " + type_to_counter_2.upper() + " types:\n")
        print("The list of S-Rank combo counters is: " + s_rank_combo_counter_string + "\n")
        print("The list of A-Rank combo counters is: " + a_rank_combo_counter_string + "\n")
        print("The list of B-Rank combo counters is: " + b_rank_combo_counter_string + "\n")