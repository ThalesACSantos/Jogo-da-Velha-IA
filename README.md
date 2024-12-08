# Jogo da Velha com IA, Python e Pygame
![Jogo_da_Velha_IA](Jogo_da_Velha_IA.ico)

## Este é um jogo da velha implementado em Python utilizando a biblioteca Pygame.

## O jogo permite que você jogue contra a Inteligência Artificial (IA).

## Como Jogar:

### Execute o script do jogo.
### Clique em uma célula vazia no tabuleiro para colocar o seu X.
### A IA fará sua jogada automaticamente.

## O jogo termina quando:
### Você preencher três Xs em uma linha, coluna ou diagonal (vitória do jogador).
### A IA preencher três Os em uma linha, coluna ou diagonal (vitória da IA).
### Todas as células estiverem preenchidas (empate).
### Clique no botão "Reiniciar" para iniciar uma nova partida.
![Botão de Reiniciar](reiniciar.ico)
## Instruções de Uso:

Para baixar a biblioteca pygame, execute no terminal o comando:

```
pip install pygame
```

Para executar o jogo, salve o código em um arquivo Python (por exemplo, jogo_da_velha.py) e execute-o no terminal usando o comando:

```
python jogo_da_velha.py
```
Para gerar os requirements do jogo, execute o seguinte comando no terminal:

```
pip freeze > requirements.txt
```

Para instalar o pyinstaller para gerar um arquivo executável (.exe), execute o seguinte comando no terminal:

```
pip install pyinstaller
```
Após a instalação do pyinstaller execute o seguinte comando para gerar o arquivo executável, com icone que deve estar na mesma pasta: 

```
pyinstaller Jogo_da_Velha_IA.py
```

Para criar um único arquivo executável sem a janela do console e com um ícone personalizado, use:

```
pyinstaller --onefile --windowed --icon=Jogo_da_Velha_IA.ico Jogo_da_Velha_IA.py
```

Use o código com cuidado.

## Recursos:

Pygame: https://www.pygame.org/
Minimax: https://en.wikipedia.org/wiki/Minimax

## Licença:

Este jogo é fornecido sem nenhuma garantia. Você pode usá-lo e modificá-lo livremente, desde que mantenha os créditos dos autores originais.

## Contribua:

Se você tiver sugestões de melhoria ou quiser contribuir para o código, sinta-se à vontade para fazer um fork do repositório (se houver) ou enviar um pull request.

## Autor:

[Thales Augusto Cardoso dos Santos / ThalesACSantos]

## Contato:

[E-mail: mecatecbots@gmail.com]

## Site:

https://sites.google.com/view/roboticamarte

ou
https://bit.ly/robmarte

## Agradecimentos:

[Agradeço a Deus, toda a honra e toda a Glória]