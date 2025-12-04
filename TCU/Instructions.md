# PDFs TCU

Instruções para lidar com pdfs ISSAI.

```bash
wget <URL>
```

```bash
ls *.pdf | xargs -i bash -c "pdftotext -y 50 -W 1000 -H 735 -f 4 -layout ./'{}'"
```

## Regimento interno TCU

* Debug
```bash
pdftotext -y 50 -W 1000 -H 615 -f 11 -l 11 -layout -nopgbrk ./RITCU.pdf - | less
```

* Gerar arquivo final com as páginas selecionadas
```bash
printf "Regimento Interno do TCU\n\n" > RITCU.txt &&
WIDTH=1000 && HEIGHT=615 && Y=50 &&
H_WITH_TITLE=635 && Y_WITH_TITLE=30 &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 10 -l 10 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 11 -l 16 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 20 -l 20 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H 150 -f 96 -l 96 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 102 -l 102 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 109 -l 110 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 120 -l 120 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 121 -l 153 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 158 -l 158 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 159 -l 161 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 168 -l 168 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 169 -l 176 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H 225 -f 184 -l 184 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt
```

Explicação

* printf: reseta o arquivo e coloca o nome do documento
* Variáveis: facililita a configuração
* Páginas únicas: é para pegar também o título no início da página
* Páginas:
    * Pg. 10 - 16: TÍTULO I – NATUREZA, COMPETÊNCIA E JURISDIÇÃO (ARTS. 1º AO 5º)
    * Pg 20: TÍTULO II CAPÍTULO I – SEDE E COMPOSIÇÃO (ARTS. 6º AO 10)
    * Pg 96: TÍTULO V – CAPÍTULO III – DISTRIBUIÇÃO (ART. 147*)
    * Pg 102: TÍTULO V – CAPÍTULO VI – PROVAS (ART. 162)
    * Pg. 109 - 110: TÍTULO V – CAPÍTULO X – NULIDADES (ARTS. 171 AO 178)
    * Pg. 120 - 153: TÍTULO VI – ATIVIDADE DE CONTROLE EXTERNO (ARTS. 188 A AO 263*)
    * Pg. 158 - 161: TÍTULO VII – SANÇÕES (ARTS. 266 AO 272)
    * Pg. 168 - 176: TÍTULO IX – RECURSOS (ARTS. 277 AO 289)
    * Pg. 184: TÍTULO XI – DISPOSIÇÕES GERAIS (ART. 293*)
