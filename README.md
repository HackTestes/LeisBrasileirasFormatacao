# Formatação de leis brasileiras

Foco é formatar leis brasileiras para leitores de texto.

## Comandos

* Formatar

```
python.exe .\format.py  D:\code_repo\LeisBrasileiras_Formatacao\Original\*.txt "D:\code_repo\LeisBrasileiras_Formatacao\Modificado\"
```

* Formatar tudo
```
$InputFiles = Get-Item D:\code_repo\LeisBrasileiras_Formatacao\Original\*.txt; $InputFiles | ForEach { python.exe .\format.py $_.FullName "D:\code_repo\LeisBrasileiras_Formatacao\Modificado\" }
```


* Copiar textos para VM
```
scp.exe D:\code_repo\LeisBrasileiras_Formatacao\Modificado\* caioh_edgetts@$(arp -a | Select-String -Pattern "00-15-5d-00-5d-" | %{$_.Line.Split(" ")[2]}):/home/caioh_edgetts/Dev/edge-tts/texts/
```


* Copiar os áudios para o host
```
scp.exe caioh_edgetts@$(arp -a | Select-String -Pattern "00-15-5d-00-5d-" | %{$_.Line.Split(" ")[2]}):/home/caioh_edgetts/Dev/edge-tts/texts/*_altered.mp3 .\Documents\Leis\Audio\
```