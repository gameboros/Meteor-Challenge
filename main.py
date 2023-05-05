from PIL import Image
import bisect

# valores rgb das cores a serem analisadas
red = (255, 0, 0, 255)
white = (255, 255, 255, 255)
waterBlue = (0, 0, 255, 255)

# funcao que itera sob os pixels e soma nos respectivos contadores


def count_pixels(image_path):
    meteors, stars = 0, 0
    waterLevel = float('inf')
    waterLevelWidth = []
    meteorWidths = []
    with Image.open(image_path) as im:
        pixels = im.load()
        width, height = im.size
        for y in range(height):
            for x in range(width):
                if pixels[x, y] == red:
                    meteors += 1
                    meteorWidths.append(x)
                elif pixels[x, y] == white:
                    stars += 1
                elif pixels[x, y] == waterBlue:
                    # checa o menor valor já que estamos checando o nivel da agua inversamente
                    waterLevel = min(waterLevel, y)
                    waterLevelWidth.append(x)

        # fazendo a interseção entre as listas e ordenando de forma ascendent
        meteorWidths = list(
            set(meteorWidths).intersection(set(waterLevelWidth)))
        meteorWidths.sort()

        return meteors, stars, meteorWidths


meteors, stars, meteorWidths = count_pixels(
    "meteor_challenge_01.png")
print(f"Number of red pixels: {meteors}, Number of white pixels: {stars}, Meteors landing on water: {meteorWidths}")
print(meteorWidths)

# 255 255 255 255 branco
# 255 0 0 255 vermelho
# 0 0 0 255 preto
# 0 0 255 255 azul agua
