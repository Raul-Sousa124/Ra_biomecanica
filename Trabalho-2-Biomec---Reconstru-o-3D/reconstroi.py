import numpy as np
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordenadas 3D do código 1
coordenadas_3d = """
0.0040106999 0.0015723430 -0.0030787174
0.0013577836 1.4664854805 -0.0002735983
0.7795888759 1.4656860934 0.0018643970
0.7783916484 -0.0011725950 0.0016910910
-0.0015136248 -0.0004110288 0.4560298087
-0.0009480126 1.4654112552 0.4498028609
0.7801485176 1.4676494054 0.4457739916
0.7823768551 -0.0016201118 0.4491580505
0.0002223853 0.0008604155 0.9077355917
-0.0032767154 1.4643818642 0.9040679833
0.7859380907 1.4664276940 0.9016854725
0.7797204682 0.0007359357 0.9015623184
"""

# Use uma expressão regular para extrair as coordenadas
coordenadas_3d = [list(map(float, re.findall(r'-?\d+\.\d+', line))) for line in coordenadas_3d.split('\n') if line.strip()]

# Converte as coordenadas em uma matriz NumPy
cc3d = np.array(coordenadas_3d)

# Cria uma figura 3D para as coordenadas 3D do código 1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Separe as coordenadas X, Y e Z dos pontos 3D
x = cc3d[:, 0]
y = cc3d[:, 1]
z = cc3d[:, 2]

# Plota os pontos 3D do código 1
ax.scatter(x, y, z, c='b', marker='o')

# Coordenadas do objeto
coordenadas_objeto = """
0.3537524653 1.0215110446 -0.0161074861
0.3539499485 1.0219292423 -0.0157431825
0.3538842601 1.0216722302 -0.0185440471
0.3538293702 1.0216198462 -0.0153621359
0.3538921912 1.0219432228 -0.0122887099
0.3539611420 1.0220658670 -0.0150715052
0.3538955256 1.0218089300 -0.0178723146
0.3537763341 1.0217875245 -0.0147326452
0.3537106600 1.0218174484 -0.0147450160
0.3537725126 1.0219410850 -0.0175595466
0.3537247688 1.0217430435 -0.0203588267
0.3536127115 1.0217206892 -0.0171874154
0.3536649601 1.0220466503 -0.0140546154
0.3537986036 1.0221969065 -0.0168885500
0.3536790717 1.0219722683 -0.0196683559
0.3462580990 1.0190410800 -0.0177310867
0.3463846263 1.0193969053 -0.0145841140
0.3465200553 1.0195500623 -0.0173885692
0.3464682550 1.0194552826 -0.0231664303
0.3464202058 1.0194593198 -0.0200136146
0.3464915268 1.0198459261 -0.0169067779
0.3466345075 1.0199995183 -0.0197097512
0.3465118993 1.0198344620 -0.0224939233
0.3464637839 1.0198385488 -0.0193412197
0.3466009599 1.0201951322 -0.0162220095
0.3466782355 1.0203786001 -0.0190372698
0.3466213413 1.0201837009 -0.0218090065
0.3465086950 1.0202187658 -0.0186986788
0.3466520381 1.0206338546 -0.015
"""

# Use uma expressão regular para extrair as coordenadas do objeto
coordenadas_objeto = [list(map(float, re.findall(r'-?\d+\.\d+', line))) for line in coordenadas_objeto.split('\n') if line.strip()]

# Converte as coordenadas do objeto em uma matriz NumPy
cc3d_objeto = np.array(coordenadas_objeto)

# Separe as coordenadas X, Y e Z dos pontos do objeto
x_objeto = cc3d_objeto[:, 0]
y_objeto = cc3d_objeto[:, 1]
z_objeto = cc3d_objeto[:, 2]

# Plota a trajetória do objeto
ax.plot(x_objeto, y_objeto, z_objeto, c='r', marker='o')

# Configurações adicionais do gráfico
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

plt.title('Trajetória do Objeto e Coordenadas 3D')

# Salvar o gráfico em um arquivo
plt.savefig('saida.png')

# Exibe o gráfico
plt.show()
