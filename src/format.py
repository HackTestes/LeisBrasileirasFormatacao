import sys
import re
from datetime import date

class InsufficientArgs(Exception):
    pass

class DstPathNotADirectory(Exception):
    pass

separator = "========================================"

def print_help():
    print("format.py <SRC FILE PATH> <DST DIRECTORY PATH> OR format.py [-h|--help]")

# https://www.geeksforgeeks.org/python-program-to-convert-integer-to-roman/
def int_to_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = len(num) - 1
    result = ""
    
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
            result += sym[i]
            div -= 1
        i -= 1

    return result

def main():
    # No args
    if len(sys.argv) <= 1:
        raise InsufficientArgs("There aren't any arguments")

    # Help
    if len(sys.argv) >= 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print_help()
        return

    # Normal flow
    source_path = sys.argv[1]
    source_file_content = open(source_path, "r", encoding='utf-8').read()

    destination_path = sys.argv[2]

    if destination_path[-1] != "\\":
        raise DstPathNotADirectory("Destination path is not a directory")

    # Also append the date, so we can differentiate newer files
    destination_file_path = open(destination_path + source_path.split("\\")[-1].replace(".txt", f"_altered_{date.today().strftime("%d-%m-%Y")}.txt"), "w", encoding='utf-8')

    print(separator)
    print(f"Source path: {source_path}")
    print(f"Destination path {destination_path}")
    print(f"Destination file: {destination_file_path}")
    print(separator)

    # Text fromatting
    formatted_text = source_file_content

    # Artigo
    formatted_text = formatted_text.replace("Art.", "Artigo")
    formatted_text = formatted_text.replace("Arts.", "Artigos")
    formatted_text = formatted_text.replace("art.", "artigo")
    formatted_text = formatted_text.replace("arts.", "artigos")
    formatted_text = formatted_text.replace("ART.", "Artigo")
    formatted_text = formatted_text.replace("ARTS.", "Artigos")

    # Numeração
    # Às vezes os números perdem o "º" na cópia a viram a letra "o"
    formatted_text = formatted_text.replace("1o ", "1º ")
    formatted_text = formatted_text.replace("2o ", "2º ")
    formatted_text = formatted_text.replace("3o ", "3º ")
    formatted_text = formatted_text.replace("4o ", "4º ") 
    formatted_text = formatted_text.replace("5o ", "5º ")
    formatted_text = formatted_text.replace("6o ", "6º ")
    formatted_text = formatted_text.replace("7o ", "7º ")
    formatted_text = formatted_text.replace("8o ", "8º ")
    formatted_text = formatted_text.replace("9o ", "9º ")

    # Às vezes os números perdem o "º" na cópia a viram graus "°"
    #formatted_text = formatted_text.replace("1° ", "1º ")
    #formatted_text = formatted_text.replace("2° ", "2º ")
    #formatted_text = formatted_text.replace("3° ", "3º ")
    #formatted_text = formatted_text.replace("4° ", "4º ") 
    #formatted_text = formatted_text.replace("5° ", "5º ")
    #formatted_text = formatted_text.replace("6° ", "6º ")
    #formatted_text = formatted_text.replace("7° ", "7º ")
    #formatted_text = formatted_text.replace("8° ", "8º ")
    #formatted_text = formatted_text.replace("9° ", "9º ")

    formatted_text = formatted_text.replace("1°", "1º")
    formatted_text = formatted_text.replace("2°", "2º")
    formatted_text = formatted_text.replace("3°", "3º")
    formatted_text = formatted_text.replace("4°", "4º") 
    formatted_text = formatted_text.replace("5°", "5º")
    formatted_text = formatted_text.replace("6°", "6º")
    formatted_text = formatted_text.replace("7°", "7º")
    formatted_text = formatted_text.replace("8°", "8º")
    formatted_text = formatted_text.replace("9°", "9º")

    formatted_text = formatted_text.replace(" n° ", " número ")
    formatted_text = formatted_text.replace(" N° ", " número ")
    formatted_text = formatted_text.replace(" nº ", " número ")
    formatted_text = formatted_text.replace(" Nº ", " número ")
    formatted_text = formatted_text.replace(" n. ", " número ")
    formatted_text = formatted_text.replace(" N. ", " número ")

    # Algumas leis possuem erros no "número" (adicionam um espaço extra), então vou corrigí-lo
    formatted_text = formatted_text.replace(" n ° ", " número ")
    formatted_text = formatted_text.replace(" N ° ", " número ")
    formatted_text = formatted_text.replace(" n º ", " número ")
    formatted_text = formatted_text.replace(" N º ", " número ")

    # Plural
    formatted_text = formatted_text.replace(" n°s ", " números ")
    formatted_text = formatted_text.replace(" N°s ", " números ")
    formatted_text = formatted_text.replace(" nºs ", " números ")
    formatted_text = formatted_text.replace(" Nºs ", " números ")
    formatted_text = formatted_text.replace(" n.s ", " números ")
    formatted_text = formatted_text.replace(" N.s ", " números ")

    # IA - evita interpretar a letra "I" como um numeral
    formatted_text = formatted_text.replace("I.A.", "IA")

    # Parágrafo
    formatted_text = formatted_text.replace("§§", "Parágrafos ")
    formatted_text = formatted_text.replace("§ ", "Parágrafo ")
    formatted_text = formatted_text.replace("§", "Parágrafo ")

    # Retirar
    formatted_text = formatted_text.replace("(Promulgação partes vetadas)", "")
    formatted_text = formatted_text.replace("(Vigência)", "")
    formatted_text = formatted_text.replace("Vigência \n", "")
    formatted_text = formatted_text.replace("(Regulamento)", "")

    # \( ou \) : são os parêntes literais já que é uma caracter especial
    # [\n\)] : representa uma bquebra de linha OU o fechamento de parênteses
    # ^ : negação (faz match com o oposto)
    # [^\n\)]* : faz match com 0 ou mais caracteres que não são uma quebra de linha OU fechamento de parênteses (isso permmite subtituir todo o texto dentro)
    # A ideia é substituir todo o texto dentro do parêntes e se ele não estiver fechado, parar na quebra de linha
    formatted_text = re.sub(r'\(Incluído pel[^\n\)]*[\n\)]', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\(Redação dada pel[^\n\)]*[\n\)]', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\(Vide [^\n\)]*[\n\)]', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\(Regulamento Dec. [^\n\)]*[\n\)]', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\(Revogad[oa] pel[^\n\)]*[\n\)]', "Revogado", formatted_text, flags=re.IGNORECASE)

    # Regras específicas para o Regimento Interno da Câmara dos Deputados
    formatted_text = re.sub(r'\(“Caput” do artigo com redação dada[^\)]*\)', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\(Parágrafo único acrescido [^\)]*\)', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\(Revogado em decorrência [^\)]*\)', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\((Artigo|Inciso|Parágrafo|Alínea|Capítulo|Seção) acrescido [^\)]*\)', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\((Artigo|Inciso|Parágrafo|Alínea|Capítulo|Seção) com redação dada [^\)]*\)', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\((Artigo|Inciso|Parágrafo|Alínea|Capítulo|Seção) com redação adaptada [^\)]*\)', "", formatted_text, flags=re.IGNORECASE)
    formatted_text = re.sub(r'\((Artigo|Inciso|Parágrafo|Alínea|Capítulo|Seção) adaptado [^\)]*\)', "", formatted_text, flags=re.IGNORECASE)

    # Números romanos
    for i in range(1, 150):
        # Incisos
        # Alguns leitores veem apenas as letras do inciso ao invés de numeração (inciso "i" ao invés de inciso um)
        formatted_text = formatted_text.replace(f"\n{int_to_roman(i)} - ", f"\nInciso {i} - ")
        #formatted_text = formatted_text.replace(f"\n{int_to_roman(i)} – ", f"\nInciso {i} – ")
        #formatted_text = formatted_text.replace(f"\n{int_to_roman(i)}–", f"\nInciso {i} –")
        formatted_text = formatted_text.replace(f"\n{int_to_roman(i)}-", f"\nInciso {i} -")

        # Substituir em referências aos incisos
        formatted_text = formatted_text.replace(f" {int_to_roman(i)} ", f" {i} ")
        formatted_text = formatted_text.replace(f" {int_to_roman(i)}\n", f" {i}\n")
        formatted_text = formatted_text.replace(f"\n{int_to_roman(i)} ", f"\n{i} ")
        formatted_text = formatted_text.replace(f" {int_to_roman(i)},", f" {i},")
        #formatted_text = formatted_text.replace(f" {int_to_roman(i)}.", f" {i}.")
        formatted_text = formatted_text.replace(f" {int_to_roman(i)}-", f" {i} -")
        formatted_text = formatted_text.replace(f"\n{int_to_roman(i)} – ", f"\n{i} – ")

    # Corrigir
    # Raios X - acaba virando raios 10
    formatted_text = formatted_text.replace("Raios 10", "Raios X")

    destination_file_path.write(formatted_text)

if __name__ == '__main__':
    main()