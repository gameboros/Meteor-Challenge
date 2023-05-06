from PIL import Image
import numpy as np
import modules

RED = (255, 0, 0, 255)
WHITE = (255, 255, 255, 255)
WATER_BLUE = (0, 0, 255, 255)

def decode_binary_string(binary_string):
    # Split binary string into groups of 8 characters
    binary_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    
    # Convert binary chunks to ASCII characters
    decoded_chars = [chr(int(chunk, 2)) for chunk in binary_chunks]
    
    # Join the characters to form the decoded string
    decoded_string = ''.join(decoded_chars)
    
    return decoded_string

def count_dots(image_path):
    pixels, width, height = modules.open_image(image_path)
    count_wt_red = np.zeros(width, dtype='int16')
    count_wt_white = np.zeros(width, dtype='int16')
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == RED:
                count_wt_red[x] += 1
            elif pixels[x, y] == WHITE:
                count_wt_white[x] += 1
                
    teste = ''.join(map(str, count_wt_red))
    teste = decode_binary_string(teste)
    teste2 = ''.join(map(str, count_wt_white))
    teste2 = decode_binary_string(teste2)
    return teste, teste2

