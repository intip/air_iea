# coding: utf-8

from __future__ import unicode_literals

from glob import glob
from os.path import join, isdir, isfile, exists

from django.conf import settings
from django.core.management.base import BaseCommand

from airlib import AIRBLK207NotFound, AirKeyError
from core.tasks import process_file
from project.local_settings import path_argoit

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
        paths = glob(join(path_argoit, "*"))
        import pdb;pdb.set_trace()
        self.handle_paths(paths)

    def handle_file(self, filepath):
        try:
            process_file(filepath)

        except AIRBLK207NotFound, exc:
            print exc
            pass

        except AirKeyError, exc:
            print exc
            pass

    def handle(self, *args, **options):
        self.handle_dir()
        print 'processamento ok'