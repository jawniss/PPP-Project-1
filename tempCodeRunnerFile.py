with open("bot_Token.txt", "rb") as myfile:
    token = "".join( myfile.readlines()[ 1: ] )
    print( token )

print( token )