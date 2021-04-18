#!/usr/bin/env python
# _*_ coding: utf8 _*_

import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-b", '--buscar', help="Información a buscar")
parser = parser.parse_args()


def main():
    if parser.buscar:
        bus = mechanize.Browser()
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0')]
        bus.open("https://www.google.com")
        '''
        Para obtener el textcontrol
        for n in bus.forms():
            print(n)
        '''
        # nr es la posición que recibe los datos
        bus.select_form(nr=0)
        # q en este caso es el nombre de la etiqueta html que recibe los datos
        bus["q"] = parser.buscar
        bus.submit()
        # html5lib es la librería que va a utilizar
        p = BeautifulSoup(bus.response().read(), 'html5lib')
        for link in p.find_all('a'):
            u = link.get('href')
            u = u.replace('/url?q=', '')
            print(u)

    else:
        print("Introducir palabra a buscar")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Programa interrumpido")
        exit()
