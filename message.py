from PIL import Image
import numpy as np
import modules

RED = (255, 0, 0, 255)
WHITE = (255, 255, 255, 255)
WATER_BLUE = (0, 0, 255, 255)

def decode_binary_string(binary_string):
    # divide string binarias em grupos de 8 caracteres
    binary_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    
    # converte strings binarias em caracteres
    decoded_chars = [chr(int(chunk, 2)) for chunk in binary_chunks]
    # concatena os chars na string
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
                
    string_1 = ''.join(map(str, count_wt_red))
    string_1 = decode_binary_string(string_1)
    string_2 = ''.join(map(str, count_wt_white))
    string_2 = decode_binary_string(string_2)
    return string_1, string_2

