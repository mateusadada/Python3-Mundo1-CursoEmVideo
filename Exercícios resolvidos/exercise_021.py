# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

print('\nBem-vindo ao programa que reproduz uma música!')

pygame.init()
pygame.mixer.music.load('exercise_021.mp3')
pygame.mixer.music.play()

input('\nTocando a música \033[33mJourney - Dont Stop Believin\033[m')
