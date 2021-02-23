# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos - Python 
# Projeto da Data Science Academy
# Livia Amaral

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.guessedLetters = []
		self.missedLetters = []
		
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word and letter not in self.guessedLetters:
			self.guessedLetters.append(letter)
		elif letter not in self.guessedLetters and letter not in self.missedLetters:
			self.missedLetters.append(letter)
		
	
	# Método para verificar se o jogo terminou
	# Jogador vence ou erra 6 letras
	def hangman_over(self):
		return self.hangman_won() or (len(self.missedLetters) == 6)
		
	
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return '-' not in self.hide_word() 		

	# Método para não mostrar a letra no board
	def hide_word(self):
		auxWord = ''
		for i in self.word:
			if i in self.guessedLetters:
				auxWord += i
			else:
				auxWord += '-'
		return auxWord

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.missedLetters)])

		print('\nPalavra: ', self.hide_word())
		print('\nLetras erradas: ', *self.missedLetters)
		print('\nLetras corretas: ', *self.guessedLetters)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	#print(game.word)

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while (game.hangman_over()==False):
		game.print_game_status()

		attempt = input('\nDigite uma letra: ')

		game.guess(attempt)

		# Verifica o status do jogo
		game.print_game_status()	

		# De acordo com o status, imprime mensagem na tela para o usuário
		if game.hangman_won():
			print ('\nParabéns! Você venceu!!')
		elif (len(game.missedLetters) == 6):
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + game.word)
	
	print ('\nFoi bom jogar com você!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
