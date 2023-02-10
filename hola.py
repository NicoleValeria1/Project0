# el parser no entiende typos


separators = {"[": "sp [", "]": "sp ]", ":": "sp :", ";": "sp ;", "|": "sp |", ",": "sp ,"}

commands = {"assignto": "cm assignTo", "goto": "cm goto", "move": "cm move", "turn": "cm turn", 
            "face": "cm face", "put": "cm put", "pick": "cm pick", "movetothe": "cm moveToThe", 
            "moveindir": "cm moveInDir", "jumptothe": "cm jumpToThe", "jumpindir": "cm jumpInDir", 
            "nop": "cm nop"
        }


def comparison(toke, list):
    if toke in separators:
        list.append(separators[token])

    elif toke in commands:
        list.append(commands[token])


string = "|c,b|"

line_tokens = string.split(" ")
if " " not in string:
    line_tokens = [string]

for token in line_tokens:
    for separator in separators:
        replacing = " " + separator + " "
        token.replace(separator, replacing)
        tokens = token.split(" ")
print(tokens)
            




