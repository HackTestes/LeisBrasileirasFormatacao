# Formatação de leis brasileiras

Foco é formatar leis brasileiras para leitores de texto.

## Como eliminar texto riscado

* Se a lei umsa uma tag `strike`, basta adicionar um estilo CSS no painel de Debug do Chrome (estilo: `Display: None`)
* Se a linha for um estilo em si, devemos salvar a página web (`CTRL + S`) e abrir em um editor de texto que possua a funcionalidade de "mudar todas as ocorrências" (VSCode). Em seguida, substitua todas os estilos de linha por `Display: None` e renderize o resultado final em um navegador web

    * `text-decoration:line-through` -> `display:none`
    * `<style>strike{display: none;};</style>`

## Encoding

* Algumas leis não usam UTF-8 e podem quebrar ao salvar como UTF-8 em um editor de texto. É necessário descobrir o encoding correto da página web e depois abrir com ele no editor. Muitas leis usam o: `windows-1252`

    * Mostrar o encoding no navegador: document.characterSet

## Mudanças nos textos ou interpretações

* Pesquisar por "ADI", "ADIN" ou "EMC".

## Comandos

* Formatar

``` powershell
python.exe .\format.py  D:\code_repo\LeisBrasileiras_Formatacao\Original\*.txt "D:\code_repo\LeisBrasileiras_Formatacao\Modificado\"
```

* Formatar tudo
``` powershell
$InputFiles = Get-Item D:\code_repo\LeisBrasileiras_Formatacao\Original\*.txt; $InputFiles | ForEach { python.exe .\src\format.py $_.FullName "D:\code_repo\LeisBrasileiras_Formatacao\Modificado\" }
```


* Copiar textos para VM
``` powershell
scp.exe D:\code_repo\LeisBrasileiras_Formatacao\Modificado\* caiohvm@$(arp -a | Select-String -Pattern "00-15-5d-00-5d-" | %{$_.Line.Split(" ")[2]}):/home/caiohvm/Dev/edge-tts/texts/
```


* Copiar os áudios para o host
``` powershell
scp.exe caiohvm@$(arp -a | Select-String -Pattern "00-15-5d-00-5d-" | %{$_.Line.Split(" ")[2]}):/home/caiohvm/Dev/edge-tts/texts/*.mp3 .\Documents\Leis\Audio\
```

* Gerar audio em português brasileiro
```bash
MAX_JOBS=4 && cd ~/texts && ls *.txt | sed 's/\..*//' | xargs -i --max-procs=$MAX_JOBS bash -c "echo 'Generating {}.mp3...' && edge-tts --voice pt-BR-FranciscaNeural --file {}.txt --write-media /tmp/{}.mp3 && mv /tmp/{}.mp3 ./ && echo 'Finished {}.mp3...'"
```

* Gerar audio em português brasileiro APENAS
```bash
MAX_JOBS=4 && cd ~/texts && ls *ptBR.txt | sed 's/\..*//' | xargs -i --max-procs=$MAX_JOBS bash -c "echo 'Generating {}.mp3...' && edge-tts --voice pt-BR-FranciscaNeural --file {}.txt --write-media /tmp/{}.mp3 && mv /tmp/{}.mp3 ./ && echo 'Finished {}.mp3...'"
```

* Gerar audio em inglês
```bash
MAX_JOBS=4 && cd ~/texts && ls *en.txt | sed 's/\..*//' | xargs -i --max-procs=$MAX_JOBS bash -c "echo 'Generating {}.mp3...' && edge-tts --voice en-US-AndrewNeural --file {}.txt --write-media /tmp/{}.mp3 && mv /tmp/{}.mp3 ./ && echo 'Finished {}.mp3...'"
```