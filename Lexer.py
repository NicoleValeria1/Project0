keywords = {"robot_r": "kw ROBOT_R", "vars": "kw VARS", "PROCS": "kw PROCS"}

separators = {"[": "sp [", "]": "sp ]", ":": "sp :", ";": "sp ;", "|": "sp |", ",": "sp ,"}

commands = {"assignto": "cm assignTo", "goto": "cm goto", "move": "cm move", "turn": "cm turn", 
            "face": "cm face", "put": "cm put", "pick": "cm pick", "movetothe": "cm moveToThe", 
            "moveindir": "cm moveInDir", "jumptothe": "cm jumpToThe", "jumpindir": "cm jumpInDir", 
            "nop": "cm nop"
        }

control = {"if": "ct if", "then": "ct then", "else": "ct else", "while": "ct while", "do": "ct do", 
            "repeat": "ct repeat"
            }

conditions = {"facing":"cd facing", "canput": "cd canPut", "canpick": "cd canPick", "canmoveindir": "cd canMoveInDir", 
            "canjumpindir": "cd canJumpInDir", "canmovetothe": "cd canMoveToThe", "canjumptothe": "cd canJumpToThe", 
            "not": "cd not"
            }
data_type = {"int": "dt int",}

identifier = {}




file_name = input("Type the file's name: ")

file = open(file_name)

file_r = file.read()

program = file_r.split('\n')

all_tokens = []

for line in program:
    line = line.lower()
    
    line_tokens = line.split(" ") ## what if there're 2 spaces?
    
    for token in line_tokens:
        if token != " ":
            if token in keywords:
                all_tokens.append(keywords[token])

            elif token in separators:
                all_tokens.append(separators[token])

            elif token in commands:
                all_tokens.append(commands[token])

            elif token in control:
                all_tokens.append(control[token])

            elif token in conditions:
                all_tokens.append(conditions[token])


print(all_tokens)

    

