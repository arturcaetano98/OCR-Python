# Bibliotecas importadas.
import cv2 as OpenCV
import pytesseract as OCR

# Recebe o texto contendo o caminho do arquivo a ser aberto.
NomeArquivo = input("Digite o arquivo que você quer abrir?:\n")

# Importa imagem ainda em RGB.
ImagemRGB = OpenCV.imread(NomeArquivo)

# Realiza uma interpolação intercubica na ImagemRGB
ImagemEscalonada = OpenCV.resize(ImagemRGB, None, fx=8, fy=8, interpolation=OpenCV.INTER_CUBIC)

# Converte a imagem escalonada para escala de cinza.
ImagemCinza = OpenCV.cvtColor(ImagemEscalonada, OpenCV.COLOR_BGR2GRAY)

# Realiza a limiarização na imagem em escala de cinza.
_, ImagemBinaria = OpenCV.threshold(ImagemCinza, 70, 255, OpenCV.THRESH_BINARY)

# Realiza a suavização da imagem com um filtro Gaussiano.
ImagemSuavizada = OpenCV.GaussianBlur(ImagemBinaria, (5, 5), 0)

# Declara a configuração ao Tesseract.
Configuracao = r'tesseract -l eng test-out'

# Envia a imagem pronta ao Tesseract passando as configurações necessárias.
Texto = OCR.image_to_string(ImagemSuavizada, lang="eng", config=Configuracao)

# Criando e escrevendo em arquivos de texto (modo 'a').
Arquivo = open('TextoOCR.txt','a')
Arquivo.write("\n"+Texto+"\n")
Arquivo.write("--------------------------------------------------------------------")
Arquivo.close()

# Escreve o texto detectado retornado pelo Tesseract.
print("\nExtração concluída\n")

# Exibe a imagem RGB.
OpenCV.imshow("Imagem Carregada - "+NomeArquivo, ImagemRGB)

# Finaliza a aplicação
OpenCV.waitKey(0)
OpenCV.destroyAllWindows()
