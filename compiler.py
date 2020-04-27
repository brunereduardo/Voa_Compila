import sys
from pprint import pprint

from LexicalAnalyzer import LexicalAnalyzer

def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('ERRO: Caminho para arquivo codigo fonte nao digitado.')

        lexAnalyzer = LexicalAnalyzer(sys.argv[1])

        with open('saida.txt', 'w') as fp:
            for item in lexAnalyzer.get_token_table():
                fp.write(item + '\n')
    except FileNotFoundError:
        print('ERRO: Arquivo nao existe.')
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()