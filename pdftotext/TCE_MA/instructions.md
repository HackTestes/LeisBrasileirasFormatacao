# Tribunal de Contas do Estado do Maranhão (TCE MA) 

## Constituição do Estado do Maranhão

* URL
```bash
wget https://arquivos.al.ma.leg.br:8443/ged/codigos_juridicos/CE89_EC101_2025 -O /tmp/Constituicao_MA_2025.pdf
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 810 -f 15 -l 15 -nopgbrk /tmp/Constituicao_MA_2025.pdf - | less
```

* Final
```bash
pdftotext -y 0 -W 1000 -H 8100 -f 5 -l 5 -nopgbrk /tmp/Constituicao_MA_2025.pdf - > ./Constituicao_MA_2025.txt &&
pdftotext -y 0 -W 1000 -H 600 -f 15 -l 186 -nopgbrk /tmp/Constituicao_MA_2025.pdf - >> ./Constituicao_MA_2025.txt &&
pdftotext -y 0 -W 1000 -H 230 -f 187 -l 187 -nopgbrk /tmp/Constituicao_MA_2025.pdf - >> ./Constituicao_MA_2025.txt
```