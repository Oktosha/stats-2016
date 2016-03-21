Домашнее задание по математической статистике
=============================================

Тут лежат мои решения домашней работы по курсу статистики ФИВТ ПМИ 2016.


Получение pdf
=============

Как получить pdf? В общем, jupiter генерирует почти правильный latex файл, просто не приспособленный к русским реалиям. Поэтому, чтобы получить pdf нужно сделать так:

'''
jupyter nbconvert --to latex your-file.ipynb
'''

Открыть сгенерированный tex файл your-file.tex и добавить в него 2 строчки

'''
\usepackage{cmap}
\usepackage[T2A]{fontenc}
'''

в самое начало, сразу после

'''
\documentclass{article}
'''

После этого оно нормально скомпилируется пдфлатехом.

'''
pdflatex your-file.tex
'''

Таки лень делать это руками, написала скрипт на python3, который делает это за меня. Да, надо было писать на bash, но что поделать.