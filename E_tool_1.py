encrypting_tool = {
    "a":'`',
    "b":'~',
    "c":'!',
    "d":'@',
    "e":'#',
    "f":'$',
    "g":'%',
    "h":'^',
    "i":'&',
    "j":'*',
    "k":'(',
    "l":')',
    "m":'_',
    "n":'-',
    "o":'+',
    "p":'=',
    "q":'{',
    "r":'}',
    "s":'[',
    "t":']',
    "u":'|',
    "v":':',
    "w":';',
    "x":'<',
    "y":'>',
    "z":'?',
    " ":'.',
}

decrypting_tool = {
    "`":'a',
    "~":'b',
    "!":'c',
    "@":'d',
    "#":'e',
    "$":'f',
    "%":'g',
    "^":'h',
    "&":'i',
    "*":'j',
    "(":'k',
    ")":'l',
    "_":'m',
    "-":'n',
    "+":'o',
    "=":'p',
    "{":'q',
    "}":'r',
    "[":'s',
    "]":'t',
    "|":'u',
    ":":'v',
    ";":'w',
    "<":'x',
    ">":'y',
    "?":'z',
    ".":' ',
}


while True:
    print("""
    1 - Encrypt MSG
    2 - Decrypt MSG
    3 - Exit
    """)
    option = int(input("Enter Your Option : "))
    if option == 1:
        MSG = input("Enter The MSG you want to Encrypt : ")
    
    if option == 2:
        pass

    if option == 3:
        break
























