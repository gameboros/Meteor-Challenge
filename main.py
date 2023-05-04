from PIL import Image

#valores rgb das cores a serem analisadas
red = (255, 0, 0, 255)
white = (255, 255, 255, 255)
waterBlue = (0, 0, 255, 255)

#funcao que itera sob os pixels e soma nos respectivos contadores
def count_pixels(image_path):
    redCount, whiteCount= 0,0
    waterLevel = float('inf')
    with Image.open(image_path) as im:
        pixels = im.load()
        width, height = im.size
        for y in range(height):
            for x in range(width):
                if pixels[x, y] == red:
                    redCount += 1
                elif pixels[x, y] == white:
                    whiteCount += 1
                elif pixels[x, y] == waterBlue:
                    #checa o menor valor já que estamos checando o nivel da agua inversamente
                    waterLevel = min(waterLevel, y)
                    
        return [redCount, whiteCount, waterLevel]

count = count_pixels("meteor_challenge_01.png")
print(f"Number of red pixels: {count[0]}, Number of white pixels: {count[1]}, Water level: {count[2]}")

#255 255 255 255 branco
#255 0 0 255 vermelho
#0 0 0 255 preto
#0 0 255 255 azul agua