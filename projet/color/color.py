red= 'red'
red_hex= '#ff0000'

blue='blue'
blue_hex= '#0000ff'

black='black'
black_hex= '#000000'

yellow='yellow'
yellow_hex= '#ffff00'

list_str= []
list_hex= []
list_str.append(red)
list_hex.append(red_hex)
list_str.append(blue)
list_hex.append(blue_hex)
list_str.append(black)
list_hex.append(black_hex)
list_str.append(yellow)
list_hex.append(yellow_hex)


def trad_hex_to_rgb(hex_str):
    """
    prend la chaine hexa et la transforme en list rgb
    """
    if hex_str.startswith('#'):
        hex_str = hex_str[1:]
    return [int(hex_str[i:i + 2], 16) for i in range(0, len(hex_str), 2)]


def trad_str_to_rgb(nom):
    """
    prend la chaine de charactere et la transforme en list rgb
    et retourn 0,0,0 si n'existe pas
    """
    for i in range(len(list_str)):
        if nom == list_str[i]:
            return trad_hex_to_rgb(list_hex[i])
    return [0,0,0]
