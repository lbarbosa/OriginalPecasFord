# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""


def procFiles(arqusql, arquXml):
    print("procLineXml")
    count_sql = 0
    ncm_count = 0
    if arqusql != '' and arquXml != '':
        sql_len = len(arqusql)
        for sql in arqusql:
            if count_sql == 0:
                count_sql = count_sql + 1
                sql.append('NCM')
            else:
                for xml in arquXml:
                    if xml[0] in sql[1]:
                        sql.append(xml[0])
                        break
                    else:
                        ncm_count = ncm_count + 1
                        sql.append('NCM_' + str(ncm_count))
                        break

    return arqusql
