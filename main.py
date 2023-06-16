from PIL import Image
from rembg import remove

# Abrir as imagens da camiseta e da estampa
camiseta = Image.open("camiseta.png")
estampa = "estampa.jpg"

with open(estampa , "rb") as f:
    with open("estampa_sem_fundo.png", "wb") as g:
        estampa = remove(f.read())
        g.write(estampa)

estampa = Image.open("estampa_sem_fundo.png")

# Redimensionar a estampa para que caiba na camiseta
# Aqui estamos assumindo que queremos que a estampa seja metade da largura da camiseta
largura_camiseta, altura_camiseta = camiseta.size
largura_estampa = largura_camiseta // 2
# Mantendo a proporção da estampa
altura_estampa = int(largura_estampa * estampa.size[1] / estampa.size[0])
estampa = estampa.resize((largura_estampa, altura_estampa))

# Posicionar a estampa no centro da camiseta
posicao_x = (largura_camiseta - largura_estampa) // 2
posicao_y = (altura_camiseta - altura_estampa) // 2 - 60

# Colocar a estampa na camiseta
camiseta.paste(estampa, (posicao_x, posicao_y), estampa)

# Salvar a imagem final
camiseta.save("camiseta_com_estampa.png")