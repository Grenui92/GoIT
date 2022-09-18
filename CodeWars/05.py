def decode_morse(morse_code):
    result = [[MORSE_CODE[i] for i in j.split()] for j in morse_code.strip().split('  ')]
    return ' '.join([''.join(i) for i in result])