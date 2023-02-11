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

alphabet = {"a": "al a","b": "al b","c": "al c","d": "al d","e": "al e","f": "al f","g": "al g","h": "al h","i": "al i",
            "j": "al j","k": "al k","l": "al l","m": "al m","n": "al n","o": "al o","p": "al p","q": "al q","r": "al r",
            "s": "al s","t": "al t","u": "al u","v": "al v","w": "al w","x": "al x","y": "al y","z":"al z"}

numbers = {"0": "nu 0", "1": "nu 1","2": "nu 2","3": "nu 3","4": "nu 4","5": "nu 5","6": "nu 6","7": "nu 7",
            "8": "nu 8","9": "nu 9"}

variables = {}

def lexer (file_name:str)->dict:

    file = open(file_name)
    file_r = file.read()
    program = file_r.split('\n')
    all_tokens = []

    for line in program:
        line = line.lower()
        line_tokens = line.split(" ")
        if " " not in line:
            line_tokens = [line]

        for token in line_tokens:
            for separator in separators:
                replacing = " " + separator + " "
                token=token.replace(separator, replacing)
                tokens = token.split(" ")

            if tokens != " ":
                if tokens in keywords:
                    all_tokens.append(keywords[tokens])

                elif tokens in separators:
                    all_tokens.append(separators[tokens])

                elif tokens in commands:
                    all_tokens.append(commands[tokens])

                elif tokens in control:
                    all_tokens.append(control[tokens])

                elif tokens in conditions:
                    all_tokens.append(conditions[tokens])

                else:
                    if tokens[0] in alphabet:
                        agregar=True
                        for t in tokens:
                            if t in alphabet or numbers:
                                agregar=True
                            else:
                                agregar=False
                    else:
                        agregar=False
                
                    if agregar==True:
                        all_tokens.append(keywords[tokens])
                    elif agregar==False:
                        return "Lexical error"

    return all_tokens

print (lexer("test.txt"))
                