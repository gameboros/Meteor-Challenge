from PIL import Image

# valores rgb das cores a serem analisadas
RED = (255, 0, 0, 255)
WHITE = (255, 255, 255, 255)
WATER_BLUE = (0, 0, 255, 255)

# funcao que itera sob os pixels e soma nos respectivos contadores
def open_image(image_path):
    with Image.open(image_path) as image:
        pixels = image.load()
        width, height = image.size
    return pixels, width, height