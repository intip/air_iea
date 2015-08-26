# coding: utf-8

from __future__ import unicode_literals

from glob import glob
from os.path import join, isdir, isfile, exists

from django.conf import settings
from django.core.management.base import BaseCommand

from airlib import AIRBLK207NotFound, AirKeyError
from core.tasks import process_file, move_file, type_file
PATH_ARGOIT = settings.PATH_ARGOIT
PATH_REGENTE = settings.PATH_REGENTE
PATH_HOTEL = settings.PATH_HOTEL

class Command(BaseCommand):
    help = "Move os arquivos da pasta raiz para a pasta de integracao"
    """
    se for arquivo do argoit move para a pasta argoit
    se for amadeus move para a pasta amadeus
    arquivos amadeus sao processados pelo regente
    arquivos argoit sao tratados e convertidos para iea e movidos para serem
    processados novamente pelo regente
    """

    def handle_dir(self):

        paths = glob(join(PATH_ARGOIT, "*.*"))
        for path in paths:
            file_type = type_file(path)
            if file_type == 'hotel':
                print 'moveu para hotel %s' % path
                move_file(path, PATH_HOTEL)
            else:
                move_file(path, PATH_REGENTE)

    def handle(self, *args, **options):
        self.handle_dir()
        print 'processamento ok'