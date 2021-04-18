#!/usr/bin/env python
# _*_ coding: utf8 _*_

import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t', '--target', help="Objetivo")
parser = parser.parse_args()


def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            # convertir en diccionario
            cabeceras = dict(url.headers)
            for i in cabeceras:
                print(i + " : " + cabeceras[i])
        except:
            print("Error al conectar")
    else:
        print("No hay objetivo")


if __name__ == '__main__':
    main()
