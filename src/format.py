import sys

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

    destination_file_path = open(destination_path + source_path.split("\\")[-1].replace(".txt", "_altered.txt"), "w", encoding='utf-8')

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

    # Às vezes os números perdem o "º" na cópia a viram a graus "°"
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

    # IA - evita interpretar a letra "I" como um numeral
    formatted_text = formatted_text.replace("I.A.", "IA")

    # Parágrafo
    formatted_text = formatted_text.replace("§§", "Parágrafos ")
    formatted_text = formatted_text.replace("§ ", "Parágrafo ")
    formatted_text = formatted_text.replace("§", "Parágrafo ")

    # Retirar
    formatted_text = formatted_text.replace("(Vigência)", "")

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

    destination_file_path.write(formatted_text)

if __name__ == '__main__':
    main()