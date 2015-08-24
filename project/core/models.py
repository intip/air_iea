from django.core.files.base import ContentFile
from django.db import models

import iealib


class Processing(models.Model):
    air_file = models.FileField(upload_to="input/%Y/%m/%d/%H:%M")
    air_json_data = models.TextField()
    iea_file = models.FileField(blank=True, upload_to="output")
    iea_json_data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
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

    class Meta:
        verbose_name = "Processamento"
        verbose_name_plural = "Processamentos"

    def __unicode__(self):
        return self.air_file.path

    def reprocess(self):
        from .tasks import process_file
        return process_file(self.air_file.path, self)

    def generate_iea_file_contents(self):
        values = []
        for k, meta in iealib.KEYS:
            values.append(str(getattr(self, "iea_%s" % k)))
        raw = ';'.join(values) + '\r\n\r\n'
        return raw

    def write_iea_file(self):
        raw = self.generate_iea_file_contents()

        # if self.iea_file:
        #     self.iea_file.delete()

        self.iea_file.save(self.iea_file.name,
                           ContentFile(raw))
