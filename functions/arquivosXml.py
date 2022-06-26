# -*- coding: utf-8 -*-
"""
Graphical User Interface for file processing
Autor: Lourenço Madruga Barbosa

Funcionalidades da versão: 1.0.0
"""
import xml.etree.ElementTree as etXml
import os


# Open the file and create a Python list
def getFileXml(filename, Encoding):
    print("openFileXml")
    Encoding = Encoding

    for dir, sub, arqu in os.walk(filename):
        # Open File
        return dir, sub, arqu


def procLineXml(dirXml, subXml, arquXml):
    print("procLineXml")
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
                #print(child.tag.replace("{http://www.portalfiscal.inf.br/nfe}", ""), child.text)
                if vl_child == "cProd":
                   vl_cProd = child.text

                if vl_child == "xProd":
                   vl_xProd = child.text

                if vl_child == "NCM":
                   vl_NCM = child.text

                if vl_cProd != "" and vl_xProd != "" and vl_NCM != "":
                    print(vl_cProd, vl_xProd, vl_NCM)
                    vl_cProd = vl_xProd = vl_NCM = ""
    # process the file to validate where the product lines start and end

    # process the product line
