# Universidad del Valle de Guatemala
# Cifrado de Información
# Laboratorio 4
#
# Andrei Portales 19825
# Jose Javier Hurtarte 19707
# Christian Pérez 19710

#Obtenidas de https://github.com/GINARTeam/NIST-statistical-test
#Adaptadas para aceptar cadenas de bit en formato de string como unico parametro
from StatTests.monobit_test import monobit
from StatTests.longest_run_ones_in_a_block import longestRunOnesInABlock
from StatTests.frequency_within_block_test import frecuency
from StatTests.random_excursion_test import randomEx
from StatTests.runs_test import runs
from StatTests.non_overlapping_template_matching_test import nonOverlapping

#Obtenidas de https://github.com/dj-on-github/sp800_22_tests
#Adaptadas para aceptar cadenas de bit en formato de string como unico parametro
from StatTests.sp800_22_maurers_universal_test import maurers_universal_test
from StatTests.sp800_22_cumulative_sums_test import cumulative_sums_test
from StatTests.sp800_22_dft_test import dft_test
from StatTests.sp800_22_binary_matrix_rank_test import binary_matrix_rank_test

#Para graficar el histograma
import matplotlib.pyplot as plt

#Librería de tests aleatorios utilizada en laboratorio 3
import pseudo_random_bits as pseudo;



#Graficos de barras
def plot(data, title):
    plt.style.use('ggplot')
    plt.figure(title)
    plt.title(title)
    plt.ylabel("Frecuencia")
    plt.bar(data.keys(), data.values(), align='center', width=0.8)
    plt.show()

#Histograma en base a una lista de valores
def plotHist(data, title):
    plt.figure(title)
    plt.title(title)
    plt.hist(data)
    plt.show()


#Función de batería de tests para probar cadenas pseudoaleatorias
def batteryTests(bits, tail = 0.01):
    verifier = lambda p: "Success" if p > tail else "Fail"
    results = [
("Monobit test",monobit(bits)[3]),
("Maurers universal test",maurers_universal_test(bits)[1]),
("Frecuency between blocks test",frecuency(bits)[1]),
("Random excursion test",randomEx(bits)[4]),
("Runs test", runs(bits)[4]),
("Non overlapping test", nonOverlapping(bits)[3]),
("Cumulative sums test", (cumulative_sums_test(bits)[2][1])),
("DFT test", dft_test(bits)[1]),
("Binary matrix rank test", binary_matrix_rank_test(bits)[7]),
("Longest run ones in a block test", longestRunOnesInABlock(bits)[1])
    ]
    return [(n[0],n[1], verifier(n[1])) for n in results]


#Para las cadenas aleatorias del laboratorio pasado

#Con generador de congruencia lineal
print("Ejemplo correcto Generador Lineal:")
for n in batteryTests(pseudo.linearGenerator(31111, 1111111, 31, 100, int(387848/8))):
    print(n)


print("\nEjemplo Con Errores Generador Lineal:")
for n in batteryTests(pseudo.linearGenerator(68, 300, 31, 100, int(387848/8))):
    print(n)


#Con generador Wichman-Hill
print("\n\nEjemplo correcto Wichman-Hill:")
for n in batteryTests(pseudo.wichmanGenerator([111, 711, 313],  int(387848/8))):
    print(n)


print("\nEjemplo Con Errores Wichman-Hill:")
for n in batteryTests(pseudo.wichmanGenerator([1, 1, 1], int(387848/8),m1=100,m2=200,m3=300 )):
    print(n)


#Con generador LSFR
print("\n\nEjemplo correcto LSFR:")
for n in batteryTests(pseudo.lfsr(369112786, 387848, positions =[1,6,7,13,14,18,21,27], step=3)):
    print(n)


print("\nEjemplo Con Errores LSFR:")
for n in batteryTests(pseudo.lfsr(2002, 387848, positions =[1,2], step=1)):
    print(n)



print("\n\nGraficas de errores en bateria de tests con 1000 iteraciones:")
print("\nDebido a la complejidad en tiempo de los tests y de los generadores, puede tomar hasta media hora por gráfica")
print("por lo que se recomienda ver los resultados en el PDF adjunto\n")


# Para LSFR
fallosLSFR = []
for x in range(1000):
    pseudoLSFR = pseudo.lfsr(2097152 + 123*x, 387848, positions =[1,6,7,13,14,18,21], step=1)
    
    fallosLSFR.append(len([n for n in batteryTests(pseudoLSFR) if n[2]=='Fail']))

plotHist(fallosLSFR, "Tests fallados en cadenas LSFR")



# Para Wichman-Hill
fallosWichman = []
for x in range(1000):
    pseudoWichman = pseudo.wichmanGenerator([111 +123*x, 711+389*x, 313+ 631*x],  int(387848/8))
    
    fallosWichman.append(len([n for n in batteryTests(pseudoWichman) if n[2]=='Fail']))

plotHist(fallosWichman, "Tests fallados en cadenas Wichman-Hill")

# Para generador de Congruencia lineal
fallosLineal = []
for x in range(1000):
    pseudoLineal = pseudo.linearGenerator(31111, 1111111, 31, 100, int(387848/8))
    
    fallosLineal.append(len([n for n in batteryTests(pseudoLineal) if n[2]=='Fail']))

plotHist(fallosLineal, "Tests fallados en cadenas de Congruencia lineal")





