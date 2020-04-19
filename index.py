# -*- coding: utf-8 -*-

"""
    Autor: Jhennifer Matias
    Projeto: jogo da forca multiplayer
"""

import string
import os
import sys

letras_certas = []
letras_erradas = []
palavra_lista = []
resposta = [] #resposta atual
vidas = 0

def letra(palavra, vidas):
    """
    A função lê as letras
    e verifica se as mesmas pertencem
    a palavra ou não
    """

    letra = input("\n \n Digite uma letra: ")
    e = palavra.find(letra)
    if e == -1:
        letras_erradas.append(letra)
        vidas = vidas -1
    elif letra == palavra:
        print("parabens você ganhou!")
        sys.exit()
    else:
        letras_certas.append(letra)
    return vidas


def inicio(palavra):
    """
    Esta função inicializa o jogo
    com a quantidade de caractere
    e com a quantidade de vidas
    """

    cont = 0
    vidas = 6
    print("Vidas: "+ str(vidas))
    while cont < len(palavra):
        print(" _ ", end="")
        cont = cont + 1

def palavra():
    """
    Esta função serve para um jogador
    escolher a palavra secreta
    """
    palavra = input("Digite a palavra a ser descoberta: ")
    return palavra, list(palavra)

def mostra(palavra, vidas):
    """
    Função para mostrar a palavra
    quantidade de vidas atuais
    letras utilizadas
    """
    tamanho = len(palavra)
    resposta = "_" *tamanho
    print("Vidas atuais: "+str(vidas))
    print("Letras erradas: "+str(letras_erradas))
    palavra_lista = list(palavra)
    for i in range(tamanho):
        if palavra_lista[i] in letras_certas:
            resposta = resposta[:i] + palavra_lista[i] + resposta[i + 1:]
    return resposta

def verifica(palavra, resposta,vidas):
    if palavra == resposta:
        print("Parabéns você ganhou!")
        return -1
    elif vidas == 0:
        print("Você perdeu!")
        print("A palavra era: "+palavra)
        sys.exit()
    return 1


def imprimeComEspacos(palavra):
    for letra in palavra:
        print(letra, end=' ')
    print()

def novoJogo():
    print("================= JOGO DA FORCA ===================")
    print("O jogo consiste em um jogo de no mínimo 2 jogadores")
    pala, palavra_lista = palavra()
    os.system('clear')
    inicio(pala)
    vidas = 6
    while 1:
        vidas = letra(pala, vidas)
        resposta = mostra(pala, vidas)
        imprimeComEspacos(resposta)
        if verifica(pala, resposta,vidas) == -1:
            sys.exit()

novoJogo()
