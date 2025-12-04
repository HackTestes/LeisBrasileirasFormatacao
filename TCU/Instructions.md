# PDFs TCU

Instruções para lidar com pdfs ISSAI.

```bash
wget <ULR>
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
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 11 -l 11 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 12 -l 17 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 21 -l 21 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H 150 -f 95 -l 95 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 101 -l 101 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 108 -l 109 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 119 -l 119 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 120 -l 152 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 157 -l 157 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 158 -l 160 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H $H_WITH_TITLE -f 167 -l 167 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y -W $WIDTH -H $HEIGHT -f 168 -l 175 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt &&
pdftotext -y $Y_WITH_TITLE -W $WIDTH -H 225 -f 183 -l 183 -layout -nopgbrk ./RITCU.pdf - >> RITCU.txt
```

Explicação

* printf: reseta o arquivo e coloca o nome do documento
* Variáveis: facililita a configuração
* Páginas únicas: é para pegar também o título no início da página
* Páginas:
    * Pg. 11 - 17: TÍTULO I – NATUREZA, COMPETÊNCIA E JURISDIÇÃO (ARTS. 1º AO 5º)
    * Pg 21: TÍTULO II CAPÍTULO I – SEDE E COMPOSIÇÃO (ARTS. 6º AO 10)
    * Pg 95: TÍTULO V – CAPÍTULO III – DISTRIBUIÇÃO (ART. 147*)
    * Pg 101: TÍTULO V – CAPÍTULO VI – PROVAS (ART. 162)
    * Pg. 108 - 109: TÍTULO V – CAPÍTULO X – NULIDADES (ARTS. 171 AO 178)
    * Pg. 119 - 152: TÍTULO VI – ATIVIDADE DE CONTROLE EXTERNO (ARTS. 188 A AO 263*)
    * Pg. 157 - 160: TÍTULO VII – SANÇÕES (ARTS. 266 AO 272)
    * Pg. 167 - 175: TÍTULO IX – RECURSOS (ARTS. 277 AO 289)
    * Pg. 183: TÍTULO XI – DISPOSIÇÕES GERAIS (ART. 293*)
