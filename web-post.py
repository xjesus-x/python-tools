#!/usr/bin/env python
# _*_ coding: utf8 _*_

import requests
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="Archivo a subir")
parser = parser.parse_args()


def main():
    if parser.file:
        if path.exists(parser.file):
            # rb abre en formato binario
            archivo = open(parser.file, 'rb')
            headers = {'User-agent': 'Firefox'}
            # Key: name del input en el HTML
            # Url: dirección del input
            peticion = requests.post(url="https://ps.uci.edu/~franklin/doc/file_upload.html", files={'key': archivo}, headers=headers)
            # comprobación por nombre de archivo en respuesta
            if parser.file in peticion.text:
                # comprobación por código 200
                # if(parser.file[2:] in peticion.text):
                print(peticion.text)
                print("Archivo subido con éxito")

            else:
                print("Error al subir el archivo")
        else:
            print("No existe el archivo")
    else:
        print("Indica el archivo para subir")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Programa interrumpido")
