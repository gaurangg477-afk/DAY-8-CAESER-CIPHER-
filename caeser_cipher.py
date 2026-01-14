def caser_cypher(text,shift,direction):
    result = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = (position + shift) % len(alphabet)
            elif direction == "decode":
                new_position = (position - shift) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += char
    print(f"The {direction}d text is: {result}")
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = ''' ________  ________  _______   ________  ________  ________          ________  ___  ________  ___  ___  _______   ________     
|\   ____\|\   __  \|\  ___ \ |\   ____\|\   __  \|\   __  \        |\   ____\|\  \|\   __  \|\  \|\  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \   __/|\ \  \___|\ \  \|\  \ \  \|\  \       \ \  \___|\ \  \ \  \|\  \ \  \\\  \ \   __/|\ \  \|\  \   
 \ \  \    \ \   __  \ \  \_|/_\ \_____  \ \   __  \ \   _  _\       \ \  \    \ \  \ \   ____\ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \____\ \  \ \  \ \  \_|\ \|____|\  \ \  \ \  \ \  \\  \|       \ \  \____\ \  \ \  \___|\ \  \ \  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\ \_______\____\_\  \ \__\ \__\ \__\\ _\        \ \_______\ \__\ \__\    \ \__\ \__\ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|_______|\_________\|__|\|__|\|__|\|__|        \|_______|\|__|\|__|     \|__|\|__|\|_______|\|__|\|__|
                                 \|_________|                                                                                  
                                                                                                                               
'''
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caser_cypher(text,shift,direction)
choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
while choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caser_cypher(text,shift,direction)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()