# manipulação de arquivos
# exemplos: .txt e .csv

# w (write): abre um arquico no modo escrita mas
# substitui o conteudo que ja existe no arquivo

# a (append): tambem modo escrita, mas mantem

# r (read): abre o arquivo no modo leitura

arquivo = open("pessoas.txt", "a")
lista = ["frutas\n", "verduras\n", "legumes\n"]
arquivo.writelines(lista)

arquivo.close()