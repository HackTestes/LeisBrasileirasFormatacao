# International Organization of Supreme Audit Institutions (INTOSAI) - Normas Brasileiras de Auditoria do Setor Público (NBASP)

## ISSAI 100

* URL
```bash
wget https://s3-nbasp.irbcontas.org.br/nbasp/jet-form-builder/78f1893678afbeaa90b1fa01b9cfb860/2025/12/NBASP-100-%E2%80%93-PRINCIPIOS-FUNDAMENTAIS-DE-AUDITORIA-DO-SETOR-PUBLICO.pdf -O /tmp/NBASP_ISSAI_100.pdf
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 4 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - | less
```

* Final
```bash
printf "Normas Brasileiras de Auditoria do Setor Público (NBASP) - ISSAI 100 - Princípios Fundamentais de Auditoria do Setor Público \n\n" > ./NBASP_ISSAI_100.txt &&
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 4 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 6 -l 12 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 0 -W 1000 -H 165 -f 13 -l 13 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 500 -W 1000 -H 50 -f 13 -l 13 -nopgbrk /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 165 -W 1000 -H 415 -f 13 -l 13 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 14 -l 19 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 0 -W 1000 -H 275 -f 20 -l 20 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 21 -l 31 -nopgbrk -layout /tmp/NBASP_ISSAI_100.pdf - >> ./NBASP_ISSAI_100.txt &&
sed -i 's/efetividade1/efetividade/g' ./NBASP_ISSAI_100.txt
```

### Notas
Pag. 13 -> Nota de tradução/rodapé ("efetividade")

Pag. 20 -> Imagem



## ISSAI 200

* URL
```bash
wget https://s3-nbasp.irbcontas.org.br/nbasp/jet-form-builder/78f1893678afbeaa90b1fa01b9cfb860/2025/12/NBASP-200-%E2%80%93-PRINCIPIOS-DE-AUDITORIA-FINANCEIRA.pdf -O /tmp/NBASP_ISSAI_200.pdf
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 4 -nopgbrk -layout /tmp/NBASP_ISSAI_200.pdf - | less
```

* Final
```bash
printf "Normas Brasileiras de Auditoria do Setor Público (NBASP) - ISSAI 200 - Princípios de auditoria financeira\n\n" > ./NBASP_ISSAI_200.txt &&
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 4 -nopgbrk -layout /tmp/NBASP_ISSAI_200.pdf - >> ./NBASP_ISSAI_200.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 7 -l 15 -nopgbrk -layout /tmp/NBASP_ISSAI_200.pdf - >> ./NBASP_ISSAI_200.txt &&
pdftotext -y 0 -W 1000 -H 530 -f 16 -l 16 -nopgbrk -layout /tmp/NBASP_ISSAI_200.pdf - >> ./NBASP_ISSAI_200.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 17 -l 26 -nopgbrk -layout /tmp/NBASP_ISSAI_200.pdf - >> ./NBASP_ISSAI_200.txt &&
sed -i 's/NBASP 1001/NBASP 100 (parágrafos 34 a 43)/g' ./NBASP_ISSAI_200.txt
```

### Notas
Pag. 16 -> Nota de rodapé



## ISSAI 300

* URL
```bash
wget https://s3-nbasp.irbcontas.org.br/nbasp/jet-form-builder/78f1893678afbeaa90b1fa01b9cfb860/2025/12/NBASP-300-%E2%80%93-PRINCIPIOS-DE-AUDITORIA-OPERACIONAL-1.pdf -O /tmp/NBASP_ISSAI_300.pdf
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 5 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - | less
```

* Final
```bash
printf "Normas Brasileiras de Auditoria do Setor Público (NBASP) - ISSAI 300 - Princípios de auditoria operacional\n\n" > ./NBASP_ISSAI_300.txt &&
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 5 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 7 -l 9 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 0 -W 1000 -H 300 -f 10 -l 10 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 500 -W 1000 -H 50 -f 10 -l 10 -nopgbrk /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 300 -W 1000 -H 200 -f 10 -l 10 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 11 -l 22 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 0 -W 1000 -H 535 -f 23 -l 23 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 24 -l 33 -nopgbrk -layout /tmp/NBASP_ISSAI_300.pdf - >> ./NBASP_ISSAI_300.txt &&
sed -i 's/efetividade11/efetividade/g; s/aplication material2/aplication material/g' ./NBASP_ISSAI_300.txt
```

### Notas
Pag. 10 -> Nota de tradução/rodapé ("efetividade")

Pag. 23 -> Nota de rodapé estranha ("O que é aplication material?")

## ISSAI 400

* URL
```bash
wget https://s3-nbasp.irbcontas.org.br/nbasp/jet-form-builder/78f1893678afbeaa90b1fa01b9cfb860/2025/12/NBASP-400-%E2%80%93-PRINCIPIOS-DE-AUDITORIA-DE-CONFORMIDADE.pdf -O /tmp/NBASP_ISSAI_400.pdf
```

* Debug
```bash
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 5 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - | less
```

* Final
```bash
printf "Normas Brasileiras de Auditoria do Setor Público (NBASP) - ISSAI 400 - Princípios de auditoria de conformidade\n\n" > ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 575 -f 3 -l 5 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 7 -l 7 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 535 -f 8 -l 8 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 9 -l 10 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 490 -f 11 -l 11 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 535 -f 12 -l 12 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 13 -l 13 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 535 -f 14 -l 14 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 15 -l 28 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 500 -f 29 -l 29 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
pdftotext -y 0 -W 1000 -H 565 -f 30 -l 31 -nopgbrk -layout /tmp/NBASP_ISSAI_400.pdf - >> ./NBASP_ISSAI_400.txt &&
sed -i 's/conformidade1/conformidade/g; 
s/normas2/normas (Ver parágrafos 28-29 sobre o conceito de “normas”)/g; 
s/legalidade3/legalidade (Nota de tradução do IRB: tradução adotada para “regularity”)/g; s/legitimidade4/legitimidade ( tradução adotada para o termo “propriety”, no sentido do que é apropriado com base em princípios superiores do direito, da boa gestão e da ética, não necessariamente codificados em lei, e que atende ao interesse público, o bem comum.)/g; 
s/legitimidade5/legitimidade (Ver parágrafo 32)/g; 
s/financeiras6/financeiras (Ver ISSAI 2250)/g;
s/efetividade7/efetividade (Ver ISSAI 2250)/g;
s/contraditório8/contraditório (Nota de tradução do IRB: a obtenção de comentários e esclarecimentos durante a auditoria não representa abertura do contraditório e, portanto, não significa exercício de direito de defesa, o qual, se necessário, poderá ser exercido nas etapas processuais posteriores - Ver “NBASP 50 - Princípios das Atividades Jurisdicionais dos Tribunais de Contas”)/g' ./NBASP_ISSAI_400.txt
```

### Notas
Pag. 8 -> Nota de rodapé (desnecessária)

Pag. 11 -> Várias notas de rodapé

Pag. 12 -> Nota de rodapé (desnecessária)

Pag. 14 -> Nota de rodapé

Pag. 15 -> Nota de rodapé (não atrapalha o texto e está na ordem certa)

Pag. 29 -> Nota de rodapé