from django.contrib.admin import site, ModelAdmin
from django.db import models
from django import forms

from .models import Processing


AIR_FIELDS = [
    'air_BKAGT',
    'air_CURRCDE',
    'air_GUOPT',
    'air_HTLNME',
    'air_IDBKG',
    'air_INDTE',
    'air_OUTDTE',
    'air_PNRDTE',
    'air_PNRRMK_AutCli',
    'air_PNRRMK_CcuPax',
    'air_PNRRMK_CodCli',
    'air_PNRRMK_CodEt1',
    'air_PNRRMK_CodEt2',
    'air_PNRRMK_CodEt3',
    'air_PNRRMK_CodSgl',
    'air_PNRRMK_DadCnf',
    'air_PNRRMK_FilCli',
    'air_PNRRMK_ForRep',
    'air_PNRRMK_MatFun',
    'air_PNRRMK_NomSol',
    'air_PNRRMK_RsvDir',
    'air_PNRRMK_VlrTch',
    'air_PSGRNME',
    'air_ROOMRTE',
    'air_SIPPRM',
]


class ProcessingAdmin(ModelAdmin):
    list_display = ['air_file', 'status']
    fieldsets = \
        ((None, {'classes': ('wide', 'extrapretty'),
                 'fields': ('air_file', 'iea_file','status')}),
         ('AIR',
          {'classes': ('wide', 'extrapretty collapse'),
           'fields': AIR_FIELDS}),
         ('IEA',
          {'classes': ('wide', 'extrapretty'),
           'fields': ['iea_AgtRsv',
                      'iea_AutCli',
                      'iea_CcuPax',
                      'iea_CcuVen',
                      'iea_CodAph',
                      'iea_CodCli',
                      'iea_CodEt1',
                      'iea_CodEt2',
                      'iea_CodEt3',
                      'iea_CodFop',
                      'iea_CodMoe',
                      'iea_CodPah',
                      'iea_CodSgl',
                      'iea_CodTar',
                      'iea_DadCnf',
                      'iea_DadPcv',
                      'iea_DatCnf',
                      'iea_DatFim',
                      'iea_DatIni',
                      'iea_DatSol',
                      'iea_DesCcu',
                      'iea_EmlFun',
                      'iea_FilCli',
                      'iea_ForPdt',
                      'iea_ForRep',
                      'iea_GerDoc',
                      'iea_GerRet',
                      'iea_HorFim',
                      'iea_HorIni',
                      'iea_IdtArq',
                      'iea_IdtDiv',
                      'iea_IdtEmp',
                      'iea_MatFun',
                      'iea_NomPes',
                      'iea_NomSol',
                      'iea_NumCcr',
                      'iea_ObsRes',
                      'iea_PrcApt',
                      'iea_QtdApp',
                      'iea_RsvDir',
                      'iea_TaxFor',
                      'iea_TipInf',
                      'iea_TipNac',
                      'iea_TipPcv',
                      'iea_TipPdt',
                      'iea_TipPho',
                      'iea_VlrPpa',
                      'iea_VlrTch']}))
    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput},
    }
    readonly_fields = AIR_FIELDS
    save_on_top = True

    class Media:
        js = ('admin/core/processing_change.js', )

    def save_model(self, request, obj, form, change):
        obj.save()

        if 'air_file' in request.FILES:
            obj.reprocess()
        else:
            obj.write_iea_file()


site.register(Processing, ProcessingAdmin)
