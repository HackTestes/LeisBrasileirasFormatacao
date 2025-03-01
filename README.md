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