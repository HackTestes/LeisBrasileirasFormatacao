# ISO

## ISO 27001 (ABNT NBR)

* URL
```bash
wget ??? -P /tmp/
```

* Debug
```bash
pdftotext -y 100 -x 50 -W 1000 -H 700 -f 7 -l 7 -nopgbrk /tmp/'abnt_iso_27001 2022.pdf' - | less
```

* Final
```bash
echo "ABNT NBR ISO/IEC 27001 de 2022" > ./ISO_ABNT_27001_2022_pt-BR.txt &&
pdftotext -y 100 -x 50 -W 1000 -H 700 -f 7 -l 28 -nopgbrk /tmp/'abnt_iso_27001 2022.pdf' - >> ./ISO_ABNT_27001_2022_pt-BR.txt
```

## ISO 27002

* URL
```bash
wget ??? -P /tmp/
```

* Debug
```bash
pdftotext -y 50 -x 0 -W 1000 -H 760 -f 11 -l 15 -nopgbrk -raw /tmp/'iso_27002_2022 english.pdf' - | less
```

* Final
```bash
echo "ISO/IEC 27002 2022" > ./ISO_27002_2022_en-US.txt &&
pdftotext -y 50 -x 0 -W 1000 -H 760 -f 7 -l 152 -nopgbrk -raw /tmp/'iso_27002_2022 english.pdf' - >> ./ISO_27002_2022_en-US.txt
```

## ISO 27005

* URL
```bash
wget ??? -P /tmp/
```

* Debug
```bash
pdftotext -y 45 -x 0 -W 1000 -H 765 -f 47 -l 47 -nopgbrk /tmp/'ISO IEC 27005-2018 English.pdf' - | less
```

* Final
```bash
echo "ISO/IEC 27005 2018" > ./ISO_27005_2018_en-US.txt &&
pdftotext -y 45 -x 0 -W 1000 -H 765 -f 5 -l 58 -nopgbrk /tmp/'ISO IEC 27005-2018 English.pdf' - >> ./ISO_27005_2018_en-US.txt
```