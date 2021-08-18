from pygame import mixer
import os
from random import shuffle


class musica:
    def __init__(self):
        self.list_reproducao = []
        self.num_reproducao = 0
        self.rodando = False
        mixer.init()

    def incerir_musicas(self, list_reprod, arquivo):
        nome, extecao = os.path.splitext(arquivo)  # separa a extecão do arquivo
        if extecao == '.ogg' or extecao == '.wav':  # verifica sé o arquivo é copativel
            self.list_reproducao.append(list_reprod)
            self.list_reproducao = sorted(self.list_reproducao)  # ordena em ordem alfabetica
            mixer.music.load(self.list_reproducao[0])
            mixer.music.play()
            mixer.music.pause()

    def limpar_reproducao(self):
        self.num_reproducao = 0
        self.list_reproducao = []

    def play(self):  # pausa ou continua o som
        if len(self.list_reproducao) > 0:

            if mixer.music.get_busy():
                mixer.music.pause()
                self.rodando = False
            elif not mixer.music.get_busy():
                mixer.music.unpause()
                self.rodando = True

            return self.list_reproducao[self.num_reproducao]
        else:
            return 'Nenhuma musica selecionada'

    def prox_music(self, direcao):
        if len(self.list_reproducao) > 0:  # verifica sé o contem arquivos de audio na lista

            if direcao:
                self.num_reproducao += 1
            else:
                self.num_reproducao -= 1

            if self.num_reproducao >= len(self.list_reproducao) or self.num_reproducao < 0:  # verifica se o numero de reprodução é maior que o total de musicas ou sé é menor que 0
                self.num_reproducao = 0

            mixer.music.load(self.list_reproducao[self.num_reproducao])
            mixer.music.play()
            return str(self.list_reproducao[self.num_reproducao])
        else:
            return 'Nenhuma musica selecionada'

    @staticmethod
    def volume(vol):  # altera o volue
        vol = vol / 100
        mixer.music.set_volume(vol)

    def parado(self):  # Começa a proxima musica quando a atual acabar
        if self.rodando and not mixer.music.get_busy():
            if not mixer.music.get_busy():
                return True
            else:
                return False
        return False

    def aleatorio(self):
        if self.list_reproducao != sorted(self.list_reproducao):
            self.list_reproducao = sorted(self.list_reproducao)
            return False
        else:
            shuffle(self.list_reproducao)
            return True
