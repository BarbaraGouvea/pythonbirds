# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO, Ator

VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
        """
        Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

    def adicionar_obstaculo(self, *obstaculos):
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        self._passaros.extend(passaros)

    def status(self):
        birds = 0
        pigs = 0
        for pas in self._passaros:
            if pas.status == ATIVO:
                birds += 1

        for por in self._porcos:
            if por.status == ATIVO:
                pigs += 1

        if birds == 0 and pigs!=0:
            return DERROTA
        elif pigs == 0:  # len(self._passaros)==0 and len(self._porcos)!=0:
            return VITORIA
        else:
            return EM_ANDAMENTO
        """
        Método que indica com mensagem o status do jogo

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo), retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa mensagem

        :return:
        """

    def lancar(self, angulo, tempo):

        for b in self._passaros:
            if b.status == ATIVO and not b.foi_lancado():
                b.lancar(angulo, tempo)
                break

        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento"""

    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela.
        Cada ator deve ser transformado em um Ponto.
        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        pontos=[]

        for pa in self._passaros:
            pa.calcular_posicao(tempo)
            for ator in self._porcos + self._obstaculos:
                if(pa.status == ATIVO):
                    pa.colidir(ator, self.intervalo_de_colisao)
                    pa.colidir_com_chao()

            pontos.append(self._transformar_em_ponto(pa))
        for ator in self._porcos + self._obstaculos:
            pontos.append(self._transformar_em_ponto(ator))

        return pontos




    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())
