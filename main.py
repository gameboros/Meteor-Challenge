from PIL import Image
from message import count_dots
import modules

RED = (255, 0, 0, 255)
WHITE = (255, 255, 255, 255)
WATER_BLUE = (0, 0, 255, 255)

def count_pixels(image_path):
    meteors = 0
    stars = 0
    water_level = float('inf')
    water_width = set()
    meteor_widths = set()
    pixels, width, height = modules.open_image(image_path)
    
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == RED:
                meteors += 1
                meteor_widths.add(x)
            elif pixels[x, y] == WHITE:
                stars += 1
            elif pixels[x, y] == WATER_BLUE:
                # salva a menor altura já que estamos checando o nivel da agua de cima para baixo
                water_level = min(water_level, y)
                water_width.add(x)

    # fazendo a interseção entre as listas e ordenando de forma ascendente
        # contando apos intersecao
    meteor_widths = len(meteor_widths.intersection(water_width))
    return meteors, stars, meteor_widths

#chamando  funcoes principais e printando resultados
meteors, stars, meteorWidths = count_pixels("meteor_challenge_01.png")
second_part, first_part= (count_dots("meteor_challenge_01.png"))
print(f"Number of meteors: {meteors}\nNumber of stars: {stars}\nMeteors landing on water: {meteorWidths}")
print("=============================")
print("Hidden Message: " + first_part + second_part)
