# coding: utf-8

from django.core.files.base import ContentFile
from django.db import models
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
import iealib
import codecs
import os
from time import sleep
from django.conf import settings
path_regente_rj = settings.PATH_REGENTE_RJ
path_regente_sp = settings.PATH_REGENTE_SP
EMAIL_FROM = settings.EMAIL_FROM
EMAIL_TO = settings.EMAIL_TO
class Processing(models.Model):
    #air_file = models.FileField(upload_to="input/%Y/%m/%d/%H:%M")
    air_json_data = models.TextField()
    #iea_file = models.FileField(blank=True, upload_to="output")
    iea_json_data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    air_file = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="AIR FILE",
    )

    iea_file = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="IEA FILE",
    )

    air_BKAGT = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="BKAGT",
    )
    air_CURRCDE = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CURRCDE",
    )
    air_GUOPT = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="GUOPT",
    )
    air_HTLNME = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="HTLNME",
    )
    air_IDBKG = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="IDBKG",
    )
    air_INDTE = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="INDTE",
    )
    air_OUTDTE = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="OUTDTE",
    )
    air_PNRDTE = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRDTE",
    )
    air_PNRRMK_AutCli = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_AutCli",
    )
    air_PNRRMK_CcuPax = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_CcuPax",
    )
    air_PNRRMK_CodCli = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_CodCli",
    )
    air_PNRRMK_CodEt1 = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_CodEt1",
    )
    air_PNRRMK_CodEt2 = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_CodEt2",
    )
    air_PNRRMK_CodEt3 = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_CodEt3",
    )
    air_PNRRMK_CodSgl = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_CodSgl",
    )
    air_PNRRMK_DadCnf = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_DadCnf",
    )
    air_PNRRMK_FilCli = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_FilCli",
    )
    air_PNRRMK_ForRep = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_ForRep",
    )
    air_PNRRMK_MatFun = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_MatFun",
    )
    air_PNRRMK_NomSol = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_NomSol",
    )
    air_PNRRMK_RsvDir = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_RsvDir",
    )
    air_PNRRMK_VlrTch = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PNRRMK_VlrTch",
    )
    air_PSGRNME = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PSGRNME",
    )
    air_ROOMRTE = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="ROOMRTE",
    )
    air_SIPPRM = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="SIPPRM",
    )
    iea_AgtRsv = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="AgtRsv",
    )
    iea_AutCli = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="AutCli",
    )
    iea_CcuPax = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CcuPax",
    )
    iea_CcuVen = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CcuVen",
    )
    iea_CodAph = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodAph",
    )
    iea_CodCli = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodCli",
    )
    iea_CodEt1 = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodEt1",
    )
    iea_CodEt2 = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodEt2",
    )
    iea_CodEt3 = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodEt3",
    )
    iea_CodFop = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodFop",
    )
    iea_CodMoe = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodMoe",
    )
    iea_CodPah = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodPah",
    )
    iea_CodSgl = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodSgl",
    )
    iea_CodTar = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="CodTar",
    )
    iea_DadCnf = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DadCnf",
    )
    iea_DadPcv = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DadPcv",
    )
    iea_DatCnf = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DatCnf",
    )
    iea_DatFim = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DatFim",
    )
    iea_DatIni = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DatIni",
    )
    iea_DatSol = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DatSol",
    )
    iea_DesCcu = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="DesCcu",
    )
    iea_EmlFun = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="EmlFun",
    )
    iea_FilCli = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="FilCli",
    )
    iea_ForPdt = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="ForPdt",
    )
    iea_ForRep = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="ForRep",
    )
    iea_GerDoc = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="GerDoc",
    )
    iea_GerRet = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="GerRet",
    )
    iea_HorFim = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="HorFim",
    )
    iea_HorIni = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="HorIni",
    )
    iea_IdtArq = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="IdtArq",
    )
    iea_IdtDiv = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="IdtDiv",
    )
    iea_IdtEmp = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="IdtEmp",
    )
    iea_MatFun = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="MatFun",
    )
    iea_NomPes = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="NomPes",
    )
    iea_NomSol = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="NomSol",
    )
    iea_NumCcr = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="NumCcr",
    )
    iea_ObsRes = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="ObsRes",
    )
    iea_PrcApt = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="PrcApt",
    )
    iea_QtdApp = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="QtdApp",
    )
    iea_RsvDir = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="RsvDir",
    )
    iea_TaxFor = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="TaxFor",
    )
    iea_TipInf = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="TipInf",
    )
    iea_TipNac = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="TipNac",
    )
    iea_TipPcv = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="TipPcv",
    )
    iea_TipPdt = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="TipPdt",
    )
    iea_TipPho = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="TipPho",
    )
    iea_VlrPpa = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="VlrPpa",
    )
    iea_VlrTch = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="VlrTch",
    )
    status = models.TextField(
        blank=True,
        db_index=True,
        verbose_name="Status",
    )

    class Meta:
        verbose_name = "Processamento"
        verbose_name_plural = "Processamentos"

    def __unicode__(self):
        return self.air_file#.path

    def reprocess(self):
        from .tasks import process_file
        return process_file(self.air_file, self)

    def generate_iea_file_contents(self):
        values = []
        for k, meta in iealib.KEYS:
            values.append(str(getattr(self, "iea_%s" % k)))
        raw = ';'.join(values) + '\r\n\r\n'
        return raw

    def write_iea_file(self):
        if self.air_IDBKG.find('SAO') != -1:
           arquivo = path_regente_sp + '/' + self.iea_file
        else:
            arquivo = path_regente_rj + '/' + self.iea_file

        raw = self.generate_iea_file_contents()
        #ieafilepath = join(settings.MEDIA_ROOT, iea_file)
        ieafile = codecs.open(arquivo, "w", "utf-8")
        raw = raw.replace('RIOB2210V', 'RIOB2217N')
        raw = raw.replace('SAOB221BL', 'SAOB221CB')
        raw = raw.replace('SAOB2241C', 'SAOB221CB')
        print 'raw', raw
        ieafile.write(raw)

    def read_result_ieafile(self):
        """ le se integrou com sucesso ou se falhou 
        1- se esta no folder OK e sucesso
        2- se nao se esta no erro e erro
        """
        sleep(120)
        if self.air_IDBKG.find('SAO') != -1:
           arquivo = path_regente_sp
        else:
            arquivo = path_regente_rj
        # esta no ok?
        if os.path.isfile(arquivo + '/OK/' + self.iea_file.upper()):
            self.status = 'Integrou'
            self.save()
            #integracao correta
        else:
            #ve se integracao falhou
            file_erro = self.iea_file
            file_erro = file_erro.split('.')
            file_erro = file_erro[0] + '.ERR'
            if os.path.isfile(arquivo + '/ERR/' + file_erro):
                #integracao falhou
                self.status = 'Não integrou'
                self.save()
                file = codecs.open(arquivo + '/ERR/' + file_erro, 'r')
                mensagem = file.read()
                titulo = 'erro integracao iea-hotel'
                mail = EmailMultiAlternatives(titulo, mensagem, EMAIL_FROM, EMAIL_TO)
                mail.attach_alternative(mensagem, "text/html")
                mail.send()