# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from dis import _format_code_info
import math
from _ast import Return

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'
GRAVIDADE = 10  # m/s^2


class Ator():
    """
    Classe que representa um ator. Ele representa um ponto cartesiano na tela.
    """
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def __init__(self, x=0, y=0):
        """
        Método de inicialização da classe. Deve inicializar os parâmetros x, y, caracter e status

        :param x: Posição horizontal inicial do ator
        :param y: Posição vertical inicial do ator
        """
        self.y = y
        self.x = x
        self.status = ATIVO

    def caracter(self):
        return self._caracter_ativo if self.status == ATIVO else self._caracter_destruido


    def calcular_posicao(self, tempo):

        """
        Método que calcula a posição do ator em determinado tempo.
        Deve-se imaginar que o tempo começa em 0 e avança de 0,01 segundos

        :param tempo: o tempo do jogo
        :return: posição x, y do ator
        """
        return self.x, self.y

    def colidir(self, outro_ator, intervalo=1):
        if self.status==ATIVO and outro_ator.status==ATIVO:
            if outro_ator.x-intervalo<=self.x<=outro_ator.x+intervalo and outro_ator.y-intervalo<=self.y<=outro_ator.y+intervalo:
                self.status = DESTRUIDO
                self.caracter()
                outro_ator.status = DESTRUIDO
                outro_ator.caracter()
        ''' Método que executa lógica de colisão entre dois atores.
        Só deve haver colisão se os dois atores tiverem seus status ativos.
        Para colisão, é considerado um quadrado, com lado igual ao parâmetro intervalo, em volta do ponto onde se
        encontra o ator. Se os atores estiverem dentro desse mesmo quadrado, seus status devem ser alterados para
        destruido, seus caracteres para destruido também.

        :param outro_ator: Ator a ser considerado na colisão
        :param intervalo: Intervalo a ser considerado
        :return:
        '''




class Obstaculo(Ator):
    _caracter_ativo = 'O'



class Porco(Ator):
 _caracter_ativo = '@'
 _caracter_destruido = '+'


class Passaro(Ator):
    velocidade_escalar = 10


    def __init__(self, x=0, y=0):
        """
        Método de inicialização de pássaro.

        Deve chamar a inicialização de ator. Além disso, deve armazenar a posição inicial e incializar o tempo de
        lançamento e angulo de lançamento

        :param x:
        :param y:
        """
        super().__init__(x, y)
        self._x_inicial = x
        self._y_inicial = y
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None  # radianos

    def foi_lancado(self):
        if self._tempo_de_lancamento!=None:
            return True
        return False
        """
        Método que retorna verdadeira se o pássaro já foi lançado e falso caso contrário

        :return: booleano
        """


    def colidir_com_chao(self):
        """
        Método que executa lógica de colisão com o chão. Toda vez que y for menor ou igual a 0,
        o status dos Passaro deve ser alterado para destruido, bem como o seu caracter
        """
        if self.y<=0:
            self.status=DESTRUIDO
            self.caracter()


    def calcular_posicao(self, tempo):
        if self.foi_lancado() and self.status==ATIVO:
            delta_t=tempo-self._tempo_de_lancamento
            self.x=self._x_inicial+ self.velocidade_escalar*math.cos(self._angulo_de_lancamento)*delta_t
            self.y=self._y_inicial+ self.velocidade_escalar*math.sin(self._angulo_de_lancamento)*delta_t-(GRAVIDADE*delta_t**2)/2
        return self.x, self.y





    def lancar(self, angulo, tempo_de_lancamento):

        self._angulo_de_lancamento=math.radians(angulo)
        self._tempo_de_lancamento=tempo_de_lancamento






        """
        o self é o a variavel do atributo
        temm atributo de classe ou objeto e tem q descobrir de qual é.
        se ta dentro do init é de objeto
        se o self
        METODO LANÇAR: AQUI VAI A FORMULA DO DELTA T Q E O FINAL MENOS O INICIAL
        Lógica que lança o pássaro. Deve armazenar o ângulo e o tempo de lançamento para posteriores cálculo.
        O ângulo é passado em graus e deve ser transformado em radianos

        :param angulo:
        :param tempo_de_lancamento:
        :return:
        """



class PassaroAmarelo(Passaro):
    velocidade_escalar = 30
    _caracter_ativo = "A"
    _caracter_destruido = 'a'

class PassaroVermelho(Passaro):
    velocidade_escalar=20
    _caracter_ativo = "V"
    _caracter_destruido = 'v'




































    #self._tempo_de_lancamento=tempo_de_lancamento
    #self._tempo_de_lancamento=math.radians(angulo)