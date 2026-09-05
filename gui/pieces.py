
#loading chess piece's png
def loadPNG(path):
    import pygame
    from PIL import Image
    img = Image.open(path).convert("RGBA")
    surface = pygame.image.frombytes(img.tobytes(), img.size, "RGBA")
    return pygame.transform.smoothscale(surface, (70, 70))

p={
    "bk":loadPNG("gui/assets/pieces/bk.png"),
    "bq":loadPNG("gui/assets/pieces/bq.png"),
    "bn":loadPNG("gui/assets/pieces/bn.png"),
    "bb":loadPNG("gui/assets/pieces/bb.png"),
    "br":loadPNG("gui/assets/pieces/br.png"),
    "bp":loadPNG("gui/assets/pieces/bp.png"),

    "wk":loadPNG("gui/assets/pieces/wk.png"),
    "wq":loadPNG("gui/assets/pieces/wq.png"),
    "wn":loadPNG("gui/assets/pieces/wn.png"),
    "wb":loadPNG("gui/assets/pieces/wb.png"),
    "wr":loadPNG("gui/assets/pieces/wr.png"),
    "wp":loadPNG("gui/assets/pieces/wp.png"),
}
