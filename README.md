# Quebra-cabeça Deslizante (n-Puzzle)

Este relatório descreve o trabalho 1 da disciplina de Fundamentos de Inteligência Artificial cursada no Programa de Pós-Graduação em Computação da Universidade Federal de Pelotas cursada  em 2019/1. Como trabalho, foram implementados algoritmos para a resolução do problema Sliding Puzzle (Quebra-cabeça Delizante). Os algoritmos desenvolvidos foram a busca em largura, busca em profundidade, busca em profundidade iterativa e o algoritmo A* com duas heurísticas de menor caminho (Manhattan Distance e Chessboard Distance).

## Autores
Este trabalho foi desenvolvido em conjunto pelo seguintes autores
* [Douglas Corrêa](https://github.com/douglasscorrea)
* [Iago Storch](https://github.com/iagostorch)
* [Paulo Gonçalves](https://github.com/pHgon)
* [Thiago Bubolz](https://github.com/thiagobubolz)

## Como utilizar

As instruções a seguir descreverão como utilizar o projeto, desde os pré-requisitos necessários até a execução dos algoritmos.

### Pré-requisitos

É necessário possuir as bibliotecas numpy e pygame disponíveis para a linguagem de programação Python

Para instalar os pré-requisitos utilizar os seguinte comando no terminal do seu computador
```
pip install pygame
pip install numpy
```

### Como executar os algoritmos

Os algoritmos podem ser rodados individualmente ou utilizando a interface gráfica desenvolvida para ajudar na visualização do problema

#### Escolhendo o tamanho do tabuleiro para a interface gráfica
O tabuleiro pode possuir tamanhos 3x3, 4x4 e 5x5. Para escolher o tamanho e a imagem utilizada na interface ver tutoriais abaixo é necessário modificar o código ao final do arquivo **main.py** como os códigos apresentados abaixo

![Interface gráfica desenvolvida para tabuleiro 3x3](https://github.com/pHgon/8Puzzle-FIA/blob/master/Interface/images/3x3.png)


#####  Tamanho 3x3
O tamanho 3x3 pode possui 3 imagens diferentes que podem ser utilizadas. Para escolher qual imagem utilizar na interface utilizar 1 dos trechos mostrados abaixo ao final do arquivo **main.py**
```python
# Imagem 1 
game = Game_Interface(3, c.FILENAME_MAT)
#game = Game_Interface(3, c.FILENAME_JAC)
#game = Game_Interface(3, c.FILENAME_STD)
#game = Game_Interface(4, c.FILENAME_STD)
#game = Game_Interface(5, c.FILENAME_STD)
```
```python
# Imagem 2
#game = Game_Interface(3, c.FILENAME_MAT)
game = Game_Interface(3, c.FILENAME_JAC)
#game = Game_Interface(3, c.FILENAME_STD)
#game = Game_Interface(4, c.FILENAME_STD)
#game = Game_Interface(5, c.FILENAME_STD)
```
```python
# Imagem 3
#game = Game_Interface(3, c.FILENAME_MAT)
#game = Game_Interface(3, c.FILENAME_JAC)
game = Game_Interface(3, c.FILENAME_STD)
#game = Game_Interface(4, c.FILENAME_STD)
#game = Game_Interface(5, c.FILENAME_STD)
```

#####  Tamanho 4x4
O tamanho 4x4 possui somente uma imagem disponível. Para utilizar o tamanho 4x4, utilizar o seguinte trecho de código ao final do arquivo **main.py**

```python
# Imagem 3
#game = Game_Interface(3, c.FILENAME_MAT)
#game = Game_Interface(3, c.FILENAME_JAC)
#game = Game_Interface(3, c.FILENAME_STD)
game = Game_Interface(4, c.FILENAME_STD)
#game = Game_Interface(5, c.FILENAME_STD)
```

#####  Tamanho 5x5
O tamanho 5x5 possui somente uma imagem disponível. Para utilizar o tamanho 4x4, utilizar o seguinte trecho de código ao final do arquivo **main.py**

```python
# Imagem 3
#game = Game_Interface(3, c.FILENAME_MAT)
#game = Game_Interface(3, c.FILENAME_JAC)
#game = Game_Interface(3, c.FILENAME_STD)
#game = Game_Interface(4, c.FILENAME_STD)
game = Game_Interface(5, c.FILENAME_STD)
```

#### Sem interface gráfica

Para executar os algoritmos sem interface gráfica é necessário gerar um tabuleiro. Para isso, pode-se utilizar a função para gerar tabuleiros aleatoriamente presente no arquivo **shuffle.py**

##### Gerando tabuleiros aleatoriamente
```python
# board_size é o tamanho do tabuleiro
# 3 = 3x3, 4 = 4x4, 5 = 5x5
shuffler = shuffle.Shuffle(board_size)
# shuffle_number é o número de embaralhamentos
shuffler.shuffle_algorithm(shuffle_number) 
```

##### Rodando os algoritmos sem interface gráfica
##### Busca em Largura
```python
bfs_alg = bfs.BFS(shuffler.get_matrix(), board_size)
bfs_alg.BFS_algorithm()
```
##### Busca em Profundidade
```python
dfs_alg = dfs.DFS(shuffler.get_matrix(), board_size)
dfs_alg.DFS_algorithm()
```
##### Busca em Profundidade Iterativa
```python
idfs_alg = idfs.IT_DFS(shuffler.get_matrix(), board_size)
idfs_alg.IT_DFS_algorithm()
```
##### A*
Para o algoritmo A* é necessário especificar a heurística de menor caminho utilizada. Três heurísticas estão disponíveis no arquivo **utils.py**

* diff_heuristic: Peças fora do lugar correto
* chessboard_heuristic: Calcula menor caminho com _Chessboard Distance_
* manhattan_heuristic: Calcula menor caminho com _Manhattan Distance_

```python
a_star_alg = a_star.A_STAR(shuffler.get_matrix(), board_size)
# Para trocar heurística substituir o nome pelos especificados acima
a_star_alg.a_star_algorithm(utils.manhattan_heuristic)
```



