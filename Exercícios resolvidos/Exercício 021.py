# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

print('\nBem vindo ao programa que reproduz uma música!')

pygame.mixer.init()
pygame.mixer.music.load('Exercício 021.mp3')
pygame.mixer.music.play()

input('\nTocando a música Journey - Dont Stop Believin')
