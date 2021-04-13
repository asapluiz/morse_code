
app_on = True
morse_letters = {'A':'. ___   ', 'B':'___ . . .   ', 'C':'___ . ___ .   ', 'D':'___ . .   ', 'E':'.   ', 'F':'. . ___ .   ', 'G':'___ ___ .   ',
                 'H':'. . . .   ', 'I':'. .   ', 'J':'. ___ ___ ___   ', 'K':'___ . ___   ', 'L':'. ___ . .   ', 'M':'___ ___   ', 'N':'___ .   ',
                 'O':'___ ___ ___   ', 'P':'. ___ ___ .   ', 'Q':'___ ___ . ___   ', 'R':'. ___ .   ', 'S':'. . .   ', 'T':'___   ', 'U':'. . ___   ',
                 'V':'. . . ___   ', 'W':'. ___ ___   ', 'X':'___ . . ___   ', 'Y':'___ . ___ ___   ', 'Z':'___ ___ . .   ', '1':'. ___ ___ ___ ___   ',
                 '2':'. . ___ ___ ___   ', '3':'. . . ___ ___   ', '4':'. . . . ___   ', '5':'. . . . .   ', '6':'___ . . . .   ',
                 '7':'___ ___ . . .   ', '8':'___ ___ ___ . .   ', '9':'___ ___ ___ ___ .   ', '0':'___ ___ ___ ___ ___   ', ' ':'       '}

while app_on:
    letter_array = []
    morse_array = []
    letter_input = input('input letter to translate to morse_code : ').upper()

    for element in letter_input:
        letter_array.append(element)

    for element in letter_array:
        morse_array.append(morse_letters[element])

    morse_code = ''.join([elem for elem in morse_array])
    print(morse_code)