import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50, threshold=0)

def getImagemComId():
    caminhos = [os.path.join('imagens', f) for f in os.listdir('imagens')]
    faces = []
    ids = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids), faces

ids, faces = getImagemComId()

print('Treinando...')

eigenface.train(faces, ids)
eigenface.write('classificador/classificadorEigen.yml')
print('Treinamento realizado!')
