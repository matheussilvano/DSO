# Escreva um programa em Python que receba como entrada uma sequência de números inteiros e imprima os valores recebidos em ordem crescente.

# Siga o exemplo anexo e complete com o seu código.

# Utilize exatamente os mesmos nomes de classe e das operações.

# Gere a String de saída EXATAMENTE como no exemplo.

# Exemplos:

# Vetor de entrada: 4 3 2 1 5
# Saída: "1,2,3,4,5"
# Vetor de entrada: 9 0 5 2 10
# Saída: "0,2,5,9,10"
# IMPORTANTE: Não utilize funções prontas como: array.sort(). Implemente o seu próprio algoritmo de ordenação.

# """
# Universidade Federal de Santa Catarina.
#    CTC - Centro Tecnologico - http://ctc.ufsc.br
#    INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
# """

class Ordenacao:

    def ordena(self, array_para_ordenar):
        """Realiza a ordenação do conteúdo do array recebido como parâmetro"""
        n = len(array_para_ordenar)
        for i in range(n):
            for j in range(0, n-i-1):
                if array_para_ordenar[j] > array_para_ordenar[j+1]:
                    array_para_ordenar[j], array_para_ordenar[j+1] = array_para_ordenar[j+1], array_para_ordenar[j]
        return array_para_ordenar

    def to_string(self, array_ordenado):
        """Converte o conteúdo do array em String formatado
           Exemplo: 
           Para o conteúdo do array: [1, 2, 3, 4, 5]
           Retorna: "1,2,3,4,5"
           @return String com o conteúdo do array formatado
        """
        return ",".join(map(str, array_ordenado))

if __name__ == "__main__":
    input_array = list(map(int, input("Vetor de entrada: ").split()))
    ordenacao = Ordenacao()
    array_ordenado = ordenacao.ordena(input_array)
    print(ordenacao.to_string(array_ordenado))


