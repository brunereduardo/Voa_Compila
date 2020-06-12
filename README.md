# Instrucoes para Compilar o Codigo-Fonte
 Para preparar o terreno para a compilacao, respeitando a linguagem utilizada, *python*, os  passos  essenciais dos codigos fonte dos analisadores sintatico- ***scriptySintatico.py*** - e léxico- ***LexicalAnalyzer.py*** -, sao basicamente ter a versao basica, python 3 ou superior, para que se possa ter acesso a um interpretador da linguagem utilizada e, assumindo que se tenha acesso a um terminal ou uma IDE para Python, basta rodar o codigo do compilador - compiler.py -para que o mesmo utilize os analisadores léxico e sintatico, na entrada do arquivo txt a ser analisado. Por fim o mesmo gera a saida - saida.txt  -com as analises feitas pelo lexico e sintatico, com o intuito de ser utilizado em futuras implementacoes. Abaixo temos um exemplo de execucao, no qual basta utilizar a linha de comando a baixo:
```
python3  compiler.py caminho/nome_do_arquivo_de_entrada.txt 
```
