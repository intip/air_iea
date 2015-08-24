# TODO


[ ] Corrigir nome do arquivo gerado

[x] Questionar caso for enviado novamente o arquivo AIR

[x] Gerar o arquivo IEA baseado nos valores do Painel de Admin

[x] CodFop caso seja G-FAT retornar FAT, se não CC e preencher NumCcr com o número de cartão, exemplo:

    G-CCAX376433680911004EXP0220 vai para AX376433680911004 NumCcr

[x] PNRRMK_AutCli não processou o campo inteiro, veio apenas uma palavra (DIRETORIA, faltou restante)

[x] PNRRMK_CcuPax não leu conteúdo todo da linha

[x]

    [10:11:38] Leonardo Pimentel: 30 -{{ Missing:TaxFor }}; tem q pegar o valor total e diminuir pela qtde de diarias x qtde de diarias
    03SEP+02+128.0 é a quantidade de diárias
    o valor total é TTL-BRL268.80
    O caculo entao da taxa é = - TTL-BRL268.80 = 128x2  = 12,80

[x] TTL- não foi carregado para o TaxFor (É o resultado da conta)

[x]

    [10:16:26] Leonardo Pimentel: Código da taxa com 3 posições, seguido pelo valor da taxa em Reais para o segmento. As taxas devem ser separadas por uma barra normal. Ex.:TX115400/XT 1500/ISS325/
    Onde:
      "TX1", "XT " e "ISS": códigos das taxas
      "15400", "1500" e "325": valor de cada taxa, igual a 154,00, 15,00 e 3,25 respectivamente.
    Exemplo com uma taxa: TX 15400/.
    Tem que finalizar com uma barra.

[/] Linha 47. È o campo que deve ser calculado baseado nos campos de taxa do arquivo AIR original.
    iea: PrcApt
    airkey: ROOMRTE
    quantidade: RATEPER

    (USAR DIFERENÇA DE DATAS OUTDTE - INDTE, QtdApp)

[x] CodFop precisa ser desenvolvido (Verificar se está sendo retornado, os arquivos existentes possuem apenas X ou em Branco)

[!] BKAGT usar o valor para retornar do SQL o código (Aplicar trim)

[!] Select UsuIea V099UTU where UsuAma = LRAS

[!] HTLNME usar o valor para retornar o SQL (Aplicar trim)

[!] SELECT codfor FROM e095for WHERE apefor = 'nome do hotel'

[x] Quebra de linha no fim do arquivo

[x] RM*PR.99270331 / CMNET (ForRep)

    [x] caso for CMNET (PNRRMK_ForRep) possui código específico, repetir código do hotel (IEA: ForPDt / Senior: HTLNME, consultar na Database e retornar o código do Hotel)

    [x] caso for TREND (PNRRMK_ForRep) possui código específico, colocar código 5363

    [?] caso office ID seja SAO colocar instrução MUC1A

[ ] Verificar como vai ser a questão de consultar o regente para saber quais arquivos IEA foram integrados com sucesso ou não (VER DEPOIS)


# Email do  Diff


[?] Linha 26. Campo pode ser branco ou 0;
    [?] CodPah não vem de local algum
        """
        25
        CodPah
        Código do plano alimentar
        X(05)
        Não
        Se não for informado, assume “CM”(Café da manhã)
        Deixar em Branco para assumir CM
        """
    [?] VlrPpa não vem de local algum
        """
        26
        VlrPpa
        Valor do plano alimentar
        ZZZ.ZZZ.ZZ9,99
        Não
        Pode ser zerado
        Deixar em Branco
        """


# Acessos

gustavo
[10/14/14 3:53:51 PM] Josiete Costa: remoto.abctur.com.br
[10/14/14 3:56:51 PM] Josiete Costa: abctur-rj\gustavo
tenta acesssar la
tem esse email aqui tb

Utilizar o remote Desktop

remoto.abctur.com.br
Login: gustavo
Senha: gustavo@14
