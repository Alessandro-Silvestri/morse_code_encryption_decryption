'''
MORSE CODE ENCRIPTION DECRIPTION

Software for translating text to Morse code and vice versa.
The program understands if you insert a text or a morse code.
Enjoy! :)
Made by Alessandro Silvestri 2023 <alessandro.silvestri.work@gmail.com>
'''

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', '!': '-.-.--', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '', '\'': '.----.', ':': '---...', '  ': ' '}
morse_values = list(MORSE_CODE_DICT.values())
morse_keys = list(MORSE_CODE_DICT.keys())


def text_to_morse(text: str):
    ''' Converting test to morse'''
    for i in text.upper():
        print(MORSE_CODE_DICT[i])


def morse_to_text(morse_input: str):
    ''' Converting morse to text and checking the valid input'''
    text = ''
    morse_input = morse_input.split(' ')
    for i in morse_input:
        if i not in morse_values:  # checking a valid input
            text = 'Wrong input'
            break
        location = morse_values.index(i)
        text += morse_keys[location]
    print(text)


def check_input(txt_input: str) -> bool:
    return set(txt_input) | {'.', '-', ' '} == {'.', '-', ' '}


if __name__ == '__main__':
    quest = input('''
    insert text or morse (if it is morse use the spaces between the morse values):
    insert double for separating the words:
    -------> ''')
    if check_input(quest):
        morse_to_text(quest)
    else:
        text_to_morse(quest)
