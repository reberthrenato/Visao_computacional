# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib

print('QUESTÃO 1:')
print('a) Apresente a imagem e as informações de número de linhas e colunas; número de canais e')
print('número total de pixels;')

nome_arquivo = 'img_reo2.jpg' # imagem que devemos utilizar # Nome do arquivo a ser utilizado na análise
img_bgr = cv2.imread(nome_arquivo,1) # Carrega imagem colorida em BGR
img_cinza = cv2.imread(nome_arquivo,0) # Carrega imagem em escala de cinza
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM COLORIDA')
print('----------------------------------------------------------------------------------------------------------------')
print('Canal Azul') # B0 G1 R2
print(img_bgr[:,:,0]) # todas as linhas e colunas da azul.
print('Canal Verde')
print(img_bgr[:,:,1])
print('Canal Vermelho')
print(img_bgr[:,:,2])

print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM EM ESCALA DE CINZA')
print('----------------------------------------------------------------------------------------------------------------')
print(img_cinza)
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais = np.shape(img_bgr) # linhas, colunas e canais quando a imagem é colorida.
print('Dimensão: ' + str(lin) +' x '+ str(col)) # número de pixel só multiplicar um pelo outro.
print('Número de pixel: ', (lin*col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Número de Canais: ' + str(canais)) # tem três canais RGB.
print('----------------------------------------------------------------------------------------------------------------')
# Alternativa 2: conversão de brg para RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # transforma de bgr 2 = to para RGB.

print('b) Faça um recorte da imagem para obter somente a área de interesse. Utilize esta imagem para')
print('a solução das próximas alternativas;')
plt.figure ("visualizar")
plt.imshow(img_rgb, cmap ="gray")
plt.show()
img_intensidade2 = img_cinza
img_intensidade = img_rgb
img_recorte = img_intensidade[837:2170,1470:2722] # X1:X2, y1:2722
img_recorte2 = img_intensidade2[837:2170,1470:2722] # X1:X2, y1:2722
# Recortar uma imagem
#img_recorte = img_intensidade[350:,0:800]
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES IMAGEM RECORTE')
print('----------------------------------------------------------------------------------------------------------------')
#lin_r, col_r = np.shape(img_recorte) # linha e coluna da imagem recortada
#print('Dimensão: ' + str(lin_r) +' x '+ str(col_r)) # dúvida ???
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens no matplotlib (tem que ser em RGB)
plt.figure('Imagens')
plt.subplot(1,2,1) # uma linha e duas colunas com a imagem inteira
plt.imshow(img_rgb,cmap="jet") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.title("Escala de Cinza")


plt.subplot(1,2,2) # uma linha e duas colunas na posição dois imagem recortada.
plt.imshow(img_recorte,cmap="jet") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.title('RECORTE')

plt.show()

print('c) Converta a imagem colorida para uma de escala de cinza (intensidade) e a apresente utilizando')
print('os mapas de cores “Escala de Cinza” e “JET”')
# Imagem Em RGB
plt.figure('Imagem em RGB')
plt.imshow(img_recorte)
plt.title("Imagem em RGB") # título da imagem
plt.show()

# Todas em uma única figura
plt.figure('Imagens')
plt.subplot(221) # duas linhas duas colunas posição 1 2x2 = 4 imagens
plt.imshow(img_recorte)
plt.title("RGB")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation = 'horizontal') # barra de cores

img_bgr2 = cv2.cvtColor(img_recorte, cv2.COLOR_RGB2BGR)
plt.subplot(222) # dois por dois na posição 2
plt.imshow(img_bgr2)
plt.title("BGR")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation = 'horizontal') # barra de cores

plt.subplot(223)
plt.imshow(img_recorte2, cmap = 'gray') # transforma a imagem para escala de cinza.
plt.title("Escala de Cinza")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation = 'horizontal') # barra de cores

plt.subplot(224)
plt.imshow(img_recorte2, cmap = 'jet')
plt.title("JET")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation = 'horizontal') # barra de cores

plt.show()
'''
# Outra forma de converter a matriz é:
# nome_arquivo = 'img_reo2.jpg'
# img_bgr = cv2.imread(nome_arquivo,1) # 1 porque é imagem colorida
# img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB) # converte bgr para rgb
# img_cinza = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY) # trabalha em escala de cinza

# Salvar imagens
# Salvar imagem em RGB
cv2.imwrite('exemplo.png',img_bgr)
# Salvar imagem em escala de cinza
cv2.imwrite('exemplo_cinza.png',img_cinza)

# Apresentar imagens no matplotlib (tem que ser em RGB)
plt.figure('Imagens')
plt.subplot(1,2,1) # uma linha e duas colunas com a imagem inteira
plt.imshow(img_rgb,cmap="jet") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.title("Escala de Cinza")
plt.colorbar(orientation = 'horizontal') # barra de cores

plt.subplot(1,2,2) # uma linha e duas colunas na posição dois imagem recortada.
plt.imshow(img_recorte,cmap="jet") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.title('RECORTE')
plt.colorbar(orientation = 'horizontal')
plt.show()
'''
print('d) Apresente a imagem em escala de cinza e o seu respectivo histograma; Relacione o histograma')
print('e a imagem.')

# Histograma da imagem
histograma = cv2.calcHist([img_recorte],[0],None,[256],[0,256]) #histograma calcula a frequência dos pixels para cada valor possível
# tem que colocar a imagem, o canal 0 porque é binária cinza, none mascara identificação de região específica.
# não vai usar máscara none, 256 pontos, porque varia de 0 a 255.
# o histograma é um vetor.
print('----------------------------------------------------------------------------------------------------------------')
print('Histograma') # apresenta o histograma.
print(histograma)
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DA IMAGEM')
print('----------------------------------------------------------------------------------------------------------------')
dim = len(histograma) # vetor cada posição dá a quantidade de pixel relacionada com a intensidade.
print('Dimensão do Histograma: ',dim) # 256 valores possíveis elementos.
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(1,2,1) # uma linha e duas colunas duas imagens possíveis.
plt.imshow(img_recorte,cmap="gray") # escala de cinza
plt.title("IMAGEM")

plt.subplot(1,2,2)
plt.plot(histograma,color = 'black') # histograma vai fazer a curva com a cor preta
plt.title("Histograma") # título
plt.xlabel("Valores Pixels") #título dos eixos
plt.ylabel("Número de Pixels")

plt.show()

print('e) Utilizando a imagem em escala de cinza (intensidade) realize a segmentação da imagem de')
print('modo a remover o fundo da imagem utilizando um limiar manual e o limiar obtido pela técnica')
print('de Otsu. Nesta questão apresente o histograma com marcação dos limiares utilizados, a')
print('imagem limiarizada (binarizada) e a imagem colorida final obtida da segmentação. Explique')
print('os resultados.')

hist_cinza3 = cv2.calcHist([img_recorte2],[0], None, [256],[0,256])
# calculo do histograma a imagem tem que estar entre colchetes.
# acima de 140 255
#abaixo será 0
########################################################################################################################
# Limiarização - Thresholding
limiar_cinza = 77 # determina o valor que é o limiar
(L, img_limiar) = cv2.threshold(img_recorte2,limiar_cinza,255,cv2.THRESH_BINARY)
# imagem em escala de cinza, valor 140, máx 255, binário duas classes acima ou abixo do limiar.
(L, img_limiar_inv) = cv2.threshold(img_recorte2,limiar_cinza,255,cv2.THRESH_BINARY_INV)
# inv = ele vai inverter abixo do limiar 255 acima vai receber 0.
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES: ')
print('----------------------------------------------------------------------------------------------------------------')
print('Limiar: ' + str(L)) # impressão do limiar
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Limiar automático: OTSU
(L,img_otsu) = cv2.threshold(img_recorte2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Aula 3 ex2
# coloca adição mais outro parâmetro e identifica o melhor limiar.
# retorna duas variáveis o valor do limiar, e a imagem.
# faz o que é possível de acordo com a imagem.
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,3,1) # total de 6 imagens
plt.imshow(img_recorte)
plt.title('RGB')

plt.subplot(2,3,2)
plt.imshow(img_recorte2,cmap='gray')
plt.title('Escala de Cinza')

plt.subplot(2,3,3)
plt.plot(hist_cinza3,color = 'black')
plt.axvline(x=limiar_cinza,color = 'r') # ponto do X do limiar e de cor r de vermelho
plt.axvline(x=L,color = 'b')
plt.title("Histograma - b (L.Manual) r (L.OTSU)")
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,4)
plt.imshow(img_limiar,cmap='gray')
plt.title('Binário - L: ' + str(limiar_cinza))

plt.subplot(2,3,5)
plt.imshow(img_limiar_inv,cmap='gray')
plt.title('Binário Invertido: L: ' + str(limiar_cinza))

plt.subplot(2,3,6)
plt.imshow(img_otsu,cmap='gray')
plt.title('OTSU - L: ' + str(L))
plt.xticks([])
plt.yticks([])

plt.show()

img_segmentada1 = cv2.bitwise_and(img_recorte,img_recorte,mask=img_limiar)
img_segmentada2 = cv2.bitwise_and(img_recorte2,img_recorte2,mask=img_limiar)

plt.figure('Segmentação')
plt.subplot(1,1,1)
plt.imshow(img_segmentada1)
plt.title('Segmentada RGB')
plt.xticks([])
plt.yticks([])

plt.show()

print('f) Apresente uma figura contento a imagem selecionada nos sistemas RGB,\n'
      ' Lab, HSV e YCrCb.')
img_lab = cv2.cvtColor(img_recorte, cv2.COLOR_RGB2LAB)
img_hsv = cv2.cvtColor(img_recorte, cv2.COLOR_RGB2HSV)
img_ycrcb = cv2.cvtColor(img_recorte, cv2.COLOR_RGB2YCrCb)

plt.figure("Formatos de imagem")
plt.subplot(1,4,1)
plt.imshow(img_recorte)
plt.title('RGB')
plt.xticks([])
plt.yticks([])

plt.figure("Formatos de imagem")
plt.subplot(1,4,2)
plt.imshow(img_lab)
plt.title('LAB')
plt.xticks([])
plt.yticks([])

plt.figure("Formatos de imagem")
plt.subplot(1,4,3)
plt.imshow(img_hsv)
plt.title('HSV')
plt.xticks([])
plt.yticks([])

plt.figure("Formatos de imagem")
plt.subplot(1,4,4)
plt.imshow(img_ycrcb)
plt.title('Ycrcb')
plt.xticks([])
plt.yticks([])

plt.show()

print('g) Apresente uma figura para cada um dos sistemas de cores (RGB, HSV, Lab e YCrCb)\n'
      'contendo a imagem de cada um dos canais e seus respectivos histogramas.')

# RGB #
plt.figure("Formato RGB")
plt.subplot(1,4,1)
plt.imshow(img_recorte)
plt.title('RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,4,2)
plt.plot(cv2.calcHist([img_recorte],[0],None,[256],[0,256]), color = 'r')
plt.title('Canal R')

plt.subplot(1,4,3)
plt.plot(cv2.calcHist([img_recorte],[1],None,[256],[0,256]), color = 'g')
plt.title('Canal G')

plt.subplot(1,4,4)
plt.plot(cv2.calcHist([img_recorte],[2],None,[256],[0,256]), color = 'b')
plt.title('Canal B')

plt.show()

# LAB

plt.figure("Formato LAB")
plt.subplot(1,4,1)
plt.imshow(img_lab)
plt.title('LAB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,4,2)
plt.plot(cv2.calcHist([img_lab],[0],None,[256],[0,256]), color = 'black')
plt.title('Canal L')

plt.subplot(1,4,3)
plt.plot(cv2.calcHist([img_lab],[1],None,[256],[0,256]), color = 'red')
plt.title('Canal A')

plt.subplot(1,4,4)
plt.plot(cv2.calcHist([img_lab],[2],None,[256],[0,256]), color = 'yellow')
plt.title('Canal B')

plt.show()

# HSV

plt.figure("Formato HSV")
plt.subplot(1,4,1)
plt.imshow(img_hsv)
plt.title('HSV')
plt.xticks([])
plt.yticks([])

plt.subplot(1,4,2)
plt.plot(cv2.calcHist([img_hsv],[0],None,[256],[0,256]), color = 'gray')
plt.title('Canal H')

plt.subplot(1,4,3)
plt.plot(cv2.calcHist([img_hsv],[1],None,[256],[0,256]), color = 'red')
plt.title('Canal S')

plt.subplot(1,4,4)
plt.plot(cv2.calcHist([img_hsv],[2],None,[256],[0,256]), color = 'black')
plt.title('Canal V')

plt.show()

# YCrCb

plt.figure("Formato YCrCb")
plt.subplot(1,4,1)
plt.imshow(img_ycrcb)
plt.title('YCrCb')
plt.xticks([])
plt.yticks([])

plt.subplot(1,4,2)
plt.plot(cv2.calcHist([img_ycrcb],[0],None,[256],[0,256]), color = 'gray')
plt.title('Canal Y')

plt.subplot(1,4,3)
plt.plot(cv2.calcHist([img_ycrcb],[1],None,[256],[0,256]), color = 'red')
plt.title('Canal Cr')

plt.subplot(1,4,4)
plt.plot(cv2.calcHist([img_hsv],[2],None,[256],[0,256]), color = 'black')
plt.title('Canal Cb')

plt.show()

print('h) Encontre o sistema de cor e o respectivo canal que propicie melhor segmentação \n'
      ' da imagem de modo a remover o fundo da imagem utilizando limiar manual e limiar obtido\n'
      ' pela técnica de Otsu. Nesta questão apresente o histograma com marcação dos limiares\n'
      ' utilizados, a imagem limiarizada (binarizada) e a imagem colorida final obtida\n'
      ' da segmentação. Explique os resultados e sua escolha pelo sistema de cor e canal\n'
      ' utilizado na segmentação. Nesta questão apresente a imagem limiarizada (binarizada)')
# Histograma:

hist_labb = cv2.calcHist([img_lab],[0],None,[256],[0,256])

# Limiarização - Thresholding

limiar_labb = 140 # determina o valor que é o limiar
(L, img_limiarlabb) = cv2.threshold(img_lab[:,:,2],limiar_labb,255,cv2.THRESH_BINARY)
# imagem em escala de cinza, valor 140, máx 255, binário duas classes acima ou abixo do limiar.

# Limiar automático: OTSU
(P,img_otsu1) = cv2.threshold(img_lab[:,:,2],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Aula 3 ex2

# Segmentar:
img_segmentadalabb = cv2.bitwise_and(img_lab,img_lab,mask=img_limiarlabb)
img_segmentada_rgb = cv2.cvtColor(img_segmentadalabb, cv2.COLOR_LAB2RGB)

# Apresentar figuras
plt.figure('Thresholding LAB')
plt.subplot(3,3,2) # total de 6 imagens
plt.imshow(img_recorte)
plt.title('RBG')

plt.subplot(3,3,4)
plt.imshow(img_lab)
plt.title('LAB')

plt.subplot(3,3,5)
plt.plot(hist_labb,color = 'black')
plt.axvline(x=limiar_labb,color = 'r') # ponto do X do limiar e de cor r de vermelho
plt.title("Histograma -(L.Manual) Canal B")
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_segmentadalabb)
plt.title('Segmentada - LAB b')

plt.subplot(3,3,7)
plt.imshow(img_lab)
plt.title('LAB')

plt.subplot(3,3,8)
plt.plot(hist_labb,color = 'black')
plt.axvline(x=P,color = 'r') # ponto do X do limiar e de cor r de vermelho
plt.title("Histograma -(L.OTSU)")
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,9)
plt.imshow(img_otsu1, cmap= 'gray')
plt.title('OTSU')
plt.xticks([])
plt.yticks([])

plt.show()

img_segmentada1 = cv2.bitwise_and(img_recorte,img_recorte,mask=img_limiar)
img_segmentada2 = cv2.bitwise_and(img_recorte2,img_recorte2,mask=img_otsu1)

plt.figure('Segmentação')
plt.subplot(1,2,1)
plt.imshow(img_segmentada1)
plt.title('Segmentada RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(img_segmentada2, cmap= 'gray')
plt.title('Segmentada')
plt.xticks([])
plt.yticks([])

plt.show()

print('i) Obtenha o histograma de cada um dos canais da imagem em RGB, utilizando como mascara \n'
      'a imagem limiarizada (binarizada) da letra h.')

# histograma para cada um dos canais da imagem em RGB:
hist_sementes_r = cv2.calcHist([img_segmentada1],[0],img_limiarlabb,[256],[0,256]) # MASCARA SÓ DOS GRÃOS. IDENTIFICA SÓ OS GRÃOS.
hist_sementes_g = cv2.calcHist([img_segmentada1],[1],img_limiarlabb,[256],[0,256])
hist_sementes_b = cv2.calcHist([img_segmentada1],[2],img_limiarlabb,[256],[0,256])

plt.subplot(1,3,1)
plt.plot(hist_sementes_r,color = 'r')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(1,3,2)
plt.plot(hist_sementes_g,color = 'black')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(1,3,3)
plt.plot(hist_sementes_b,color = 'b')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()

print('j) Realize operações aritméticas na imagem em RGB de modo a realçar os aspectos de seu \n'
      'interesse. Exemplo (2*R-0.5*G). Explique a sua escolha pelas operações aritméticas. Segue \n'
      'abaixo algumas sugestões.')

# Operações nos canais da imagem
#img_opr_01 = np.uint8(1.5*img_rgb[:,:,2]) - np.uint8(2*img_rgb[:,:,0])
img_opr_01 = 1.5*img_segmentada_rgb[:,:,2] - 2*img_segmentada_rgb[:,:,0] # subtrai o canal azul do canal verde
img_opr_02 = 1.5*img_segmentada_rgb[:,:,2] - 1.5*img_segmentada_rgb[:,:,0]
img_opr_03 = 1.8*img_segmentada_rgb[:,:,2] - 1.5*img_segmentada_rgb[:,:,0] - img_segmentada_rgb[:,:,1]
print(img_opr_01)
#img_opr_01 = img_opr_01.astype(np.uint8) # converte ela novamente para inteiro de 8 bits
#print(img_opr_01.astype(np.uint8))

########################################################################################################################
# Apresentar imagens

# Figura das modificações

plt.figure('MODIFICAÇÕES')
plt.subplot(2,2,1)
plt.imshow(img_rgb,cmap='gray')
plt.title("RGB")

plt.subplot(2,2,2)
plt.imshow(img_opr_01,cmap='gray')
plt.title("1.5B-2R")

plt.subplot(2,2,3)
plt.imshow(img_opr_02,cmap='gray')
plt.title("1.5B-1.5R")

plt.subplot(2,2,4)
plt.imshow(img_opr_03,cmap='gray')
plt.title("1.8B-1.5R-G")

plt.show()