# Formatação de leis brasileiras

Foco é formatar leis brasileiras para leitores de texto.

## Como eliminar texto riscado

* Se a lei umsa uma tag `strike`, basta adicionar um estilo CSS no painel de Debug do Chrome (estilo: `Display: None`)
* Se a linha for um estilo em si, devemos salvar a página web (`CTRL + S`) e abrir em um editor de texto que possua a funcionalidade de "mudar todas as ocorrências" (VSCode). Em seguida, substitua todas os estilos de linha por `Display: None` e renderize o resultado final em um navegador web

## Encoding

* Algumas leis não usam UTF-8 e podem quebrar ao salvar como UTF-8 em um editor de texto. É necessário descobrir o encoding correto da página web e depois abrir com ele no editor. Muitas leis usam o: `windows-1252`

    * Mostrar o encoding no navegador: document.characterSet

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