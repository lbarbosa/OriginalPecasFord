# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""

from collections import OrderedDict
import xml.etree.ElementTree as etXml
import os


# Open the file and create a Python list
def getFileXml(filename, Encoding):
    #print("openFileXml")
    Encoding = Encoding

    for dir, sub, arqu in os.walk(filename):
        # Open File
        return dir, sub, arqu


def procLineXml(dirXml, subXml, arquXml):
   # print("procLineXml")
    resultantList = []
    nfeList = []
    vl_cProd = ""
    vl_xProd = ""
    vl_NCM = ""
    if arquXml != "" and dirXml != "":
        for arqu in arquXml:

            tree = etXml.parse(dirXml + "/" + arqu)
            root = tree.getroot()
            filtro = "*"
            for child in root.iter(filtro):
                vl_child = child.tag.replace("{http://www.portalfiscal.inf.br/nfe}", "")
                if vl_child == "cProd":
                   vl_cProd = child.text

                if vl_child == "xProd":
                   vl_xProd = child.text

                if vl_child == "NCM":
                   vl_NCM = child.text

                if vl_cProd != "" and vl_xProd != "" and vl_NCM != "":
                    nfe = [vl_cProd, vl_xProd, vl_NCM]
                    if vl_cProd not in nfeList:
                        nfeList.append(nfe)
                        vl_cProd = vl_xProd = vl_NCM = ""


        return nfeList