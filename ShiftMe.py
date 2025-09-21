alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def shift_message(text, shift, direction):
    normal_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = (position + shift) % len(alphabet)
            elif direction == "decode":
                new_position = (position - shift) % len(alphabet)
            normal_text += alphabet[new_position]
        else:
            normal_text += char  
    print(f"Result: {normal_text}")


cont = True
while cont:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift_message(text, shift, direction)

    cont_or_end = input("Do you want to continue? yes or no.\n").lower()
    if cont_or_end == "no":
        cont = False