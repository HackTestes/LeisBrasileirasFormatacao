# Funpresp-JUD

## Estatuto Social da Funpresp-Jud

* URL
```bash
wget https://www.funprespjud.com.br/wp-content/uploads/2023/04/estatuto-social-funprespjud.pdf -P /tmp/
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 810 -f 1 -nopgbrk /tmp/estatuto-social-funprespjud.pdf - | less
```

* Final
```bash
echo "Estatuto Social da Funpresp-Jud" > ./EstatutoSocialFunprespJud.txt &&
pdftotext -y 0 -W 1000 -H 810 -f 2 -nopgbrk /tmp/estatuto-social-funprespjud.pdf - >> ./EstatutoSocialFunprespJud.txt
```


## Regulamento do plano de benefícios da Funpresp‐Jud: Plano JusMP-Prev

* URL
```bash
wget https://www.funprespjud.com.br/wp-content/uploads/2021/09/Plano-de-Beneficios-FunprespJud_2018.pdf -P /tmp/
```

* Debug
```bash
pdftotext -y 50 -W 1000 -H 1000 -f 4 -l 11 -nopgbrk /tmp/Plano-de-Beneficios-FunprespJud_2018.pdf - | less
```

* Debug
```bash
echo "Regulamento do plano de benefícios da Funpresp‐Jud: Plano JusMP-Prev" > ./RegulamentoPlanoDeBeneficiosFunprespJud.txt &&
pdftotext -y 50 -W 1000 -H 1000 -f 4 -l 11 -nopgbrk /tmp/Plano-de-Beneficios-FunprespJud_2018.pdf - >> ./RegulamentoPlanoDeBeneficiosFunprespJud.txt &&
pdftotext -y 50 -W 1000 -H 350 -f 12 -l 12 -nopgbrk /tmp/Plano-de-Beneficios-FunprespJud_2018.pdf - >> ./RegulamentoPlanoDeBeneficiosFunprespJud.txt
```


## RESOLUÇÃO PREVIC 23/2023

* URL
```bash
wget https://www.gov.br/previc/pt-br/acesso-a-informacao-1/institucional/normas/resolucoes/resolucoes-previc/2023/resolucao-previc-23-2023-consolidada-ate-a-resolucao-25-de-16-10-2024/@@download/file -O /tmp/RESOLUÇÃO_PREVIC_23-2023.pdf
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 1000 -f 1 -l 3 -nopgbrk /tmp/RESOLUÇÃO_PREVIC_23-2023.pdf - | less
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 810 -f 1 -l 2 -nopgbrk /tmp/RESOLUÇÃO_PREVIC_23-2023.pdf - > ./FunprespJudResolucaoPrevic2023.txt &&
pdftotext -y 0 -W 1000 -H 560 -f 3 -l 3 -nopgbrk /tmp/RESOLUÇÃO_PREVIC_23-2023.pdf - >> ./FunprespJudResolucaoPrevic2023.txt
```