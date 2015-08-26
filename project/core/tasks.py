# coding: utf-8

from __future__ import unicode_literals
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings

from decimal import Decimal
from json import dumps
from os.path import join
import codecs
import shutil

from airlib import process_air
import database

from .models import Processing

EMAIL_FROM = settings.EMAIL_FROM
EMAIL_TO = settings.EMAIL_TO
PATH_AIR_BKP = settings.PATH_AIR_BKP


def load_file(filepath):
    fobj = open(filepath)
    print Processing.objects.get_or_create(air_file=fobj)


def move_file(filepath, filepath2):
   """
   move file da raiz para a folder de processamento
   """
   shutil.move(filepath, filepath2)

def type_file(filepath):
    """ le o arquivo e define o tipo dele """
    try:
        fobj = open(filepath)
        line = fobj.readline()
        if line:
            type_file = line.split(';')[0]
            if type_file == 'AIR-BLK207':
                return 'hotel'
    except:
        pass
    return 


def process_file(filepath, processing=None):
    """
    """
    enviar_email = False

    airdata, ieadata, ieafilename, airfilename = process_air(filepath)
    filial = 'RJ'
    if airdata['IDFIRST'].find('SAO') != -1:
        filial = 'SAO'

    print 'Processing', filepath
    print ieafilename
    print filepath
    #filepath = filepath.replace("%s/" % settings.MEDIA_ROOT, "")
    print filepath
    if processing is None:
        processing, nil = Processing.objects.get_or_create(air_file=airfilename, iea_file=ieafilename)
    processing.air_json_data = dumps(airdata)

    update_fields = ['air_json_data']
    for k, v in airdata.items():
        k = "air_%s" % k
        setattr(processing, k, v)
        update_fields.append(k)

    for k, v in ieadata.items():
        if k == 'CodFop' and v.startswith("CC"):
            v = "CC"

        elif k == 'NumCcr' and airdata['GUOPT'] != "FAT":
            v = ieadata['CodFop'][2:19]

        elif k == "TaxFor":
            total = Decimal(airdata['TOTRT_Number'])
            roomrte = Decimal(airdata['ROOMRTE'])
            days = int(airdata['RATEPER'])
            taxfor = total - (roomrte * days)
            v = ("TX%.2f/" % taxfor).replace(".", "")

        elif k == 'ForRep':
            if 'PNRRMK_ForRep' in airdata:
                print 'v', v
                if v == 'CMNET':
                    v = database.get_hotel_code(airdata['HTLNME'], filial)

                elif v == 'TREND':
                    if airdata['IDFIRST'].find('SAO') != -1:
                        v = 1005
                    else:
                        v = 5363
                elif v == 'EHTL':
                    if airdata['IDFIRST'].find('SAO') != -1:
                        v = 0
                    else:
                        v = 12682
                elif v == 'HOTELDO':
                    if airdata['IDFIRST'].find('SAO') != -1:
                        v = 0
                    else:
                        v = 14784
                else:
                    v = database.get_hotel_code(airdata['HTLNME'], filial)
        if v == 0 or v == '':
            enviar_email = True

        if k == 'AgtRsv':
            bkagt = v.strip()
            v = database.get_regente_code(bkagt, filial)

        k = "iea_%s" % k
        setattr(processing, k, v)
        update_fields.append(k)
    processing.save()  # update_fields=update_fields)

    if enviar_email:
        titulo = 'checar cadastro do hotel'
        mensagem = processing.generate_iea_file_contents()
        mail = EmailMultiAlternatives(titulo, mensagem, EMAIL_FROM, EMAIL_TO)
        mail.attach_alternative(mensagem, "text/html")
        mail.send()
    else:    
        print processing.generate_iea_file_contents()
        print processing.pk,
        print processing,
        print ieafilename
        processing.save(update_fields=['iea_file'])
        processing.write_iea_file()
        move_file(filepath,PATH_AIR_BKP)
        
