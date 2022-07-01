# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""


def procFiles(arqusql, arquXml):
    print("procLineXml")
    if arqusql != '' and arquXml != '':
        for sql in arqusql:
            print(sql[1])


        for xml in arquXml:
            print(xml[0])