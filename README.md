<h1>Reconhecimento facial</h1>
<h2>Reconhecimento facial com python e openCV</h2>

<p>Para o desenvolvimento deste projeto usamos o python3, openCV, numPy e OS.</p>
<p>Você pode obter o python em python.org e o openCV com o pip:</p>

<code>pip install opencv-python</code>

<p>Para obter o numPy:</p>

<code>pip install numpy</code>

<p>O 'OS' já acompanha o python.</p>

<h3>Esse projeto se divide em 4 partes:</h3>
<ul>
<li>Haarcascade;</li>
<li>Captura;</li>
<li>Treinamento;</li>
<li>Reconhecimento.</li>
</ul>

<ol>
<div name='1'>
<li><h3>Haarcascade</h3></li>
<p>O algoritmo Haar Cascade, é um algoritmo de detecção de objetos, que utiliza diversos classificadores.</p>
<p>Frontal face: Responsável por classificar a parte frontal de uma face.</p>
<p>Eye: Classificar os olhos em uma face.</p>
</div>

<div name='2'>
<li><h3>Captura</h3></li>
<p>Responsável por realizar a captura das imagens do rosto para o treinamento.</p>
</div>

<div name='3'>
<li><h3>Treinamento</h3></li>
<p>Com base nas imagens coletadas realiza o treinamento para reconhecimento facial do indivíduo.</p>
<p>A função getImagemComId, é responsável por realizar a leitura dos caminhos das imagens, passar as imagens para cinza e salvar as imagens em uma variável.</p>
<p>O eigenface é o responsável por todo o treinamento do algoritmo. Nesse caso, passamos as imagens salvas em cinza que estão em 'face' e seus respectivos ids.
Os ids, são responsáveis por diferenciar um indivíduo do outro, cada indivíduo é um dígito '1+'.</p>
<p>O treinamento resulta em um arquivo 'yml'. Nesse arquivo, está um tipo de classificador, com as características de todos os indivíduos treinados.</p>
</div>

<div name='4'>
<li><h3>Reconhecimento</h3></li>
<p>Utilizando o classificador gerado no treinamento, ele realiza um reconhecimento entre a imagem da live com as características do indivíduo treinado.</p>
</div>
</ol>

<h3>Exemplo:</h3>

![Exemplo Reconhecimento](https://user-images.githubusercontent.com/51063415/138610543-d3cde6a4-3237-455d-bb41-cd8c3378d993.png)

