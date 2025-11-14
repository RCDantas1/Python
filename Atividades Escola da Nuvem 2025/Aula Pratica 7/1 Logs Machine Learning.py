'''Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes.'''

import re
import numpy as np

def extract_times(filename):
   
    pattern = re.compile(r'Execution time: ([\\d\\.]+)s')
    times = []
    with open(filename, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                times.append(float(match.group(1)))
    return times

times = extract_times('SEU_ARQUIVO_LOG.txt')
if times:
    moyenne = np.mean(times)
    ecart_type = np.std(times)
    print(f"Média: {moyenne:.3f} segundos")
    print(f"Desvio padrão: {ecart_type:.3f} segundos")
else:
    print("Nenhum tempo de execução encontrado no log.")
