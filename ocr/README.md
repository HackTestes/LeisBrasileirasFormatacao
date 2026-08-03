# Instruções para OCR

## Programas principais

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [Image Magick](https://github.com/imagemagick/imagemagick)

## Exemplos


* Debug (faz a transformação e rotaciona uma imagem, mas não cria arquivos)
```
magick ./screenshot_01.jpeg -rotate 90 - | tesseract - - -l por+eng | less
```

* Cria um txt final
```
magick ./screenshot_01.jpeg -rotate 90 - | tesseract - - -l por+eng > test.txt
```