import cv2
import numpy as np

classificador = cv2.CascadeClassifier('haarcascade/haarcascade-frontalface-default.xml')
classificadorOlho = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 50
id = input('Digite o id: ')
print("'Q' para capturar...")
largura, altura = 220, 220

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for x, y, l, a in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for ox,oy,ol,oa in olhosDetectados:
            cv2.rectangle(regiao, (ox,oy), (ox + ol, oy + oa), (0, 0, 255), 2)
            if cv2.waitKey(1) & 0xFF == ord('q'):

                if np.average(imagemCinza) > 110:
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite('imagens/pessoa.' + str(id) + '.' + str(amostra) + '.jpg', imagemFace)
                    print('[Foto ' + str(amostra) + ' capturada  com sucesso]')
                    amostra += 1

    cv2.imshow('Capturar', imagem)
    cv2.waitKey(1)

    if amostra >= numeroAmostras + 1:
        break

camera.release()
cv2.destroyAllWindows()
