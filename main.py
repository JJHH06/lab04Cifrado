from monobit_test import monobit
from sp800_22_maurers_universal_test import maurers_universal_test
from frequency_within_block_test import frecuency
from random_excursion_test import randomEx
from runs_test import runs
from non_overlapping_template_matching_test import nonOverlapping
from sp800_22_cumulative_sums_test import cumulative_sums_test
from sp800_22_dft_test import dft_test
from sp800_22_binary_matrix_rank_test import binary_matrix_rank_test
from sp800_22_linear_complexity_test import linear_complexity_test
from longest_run_ones_in_a_block import longestRunOnesInABlock



import matplotlib.pyplot as plt


import pseudo_random_bits as pseudo;
pseudoLSFR = pseudo.lfsr(369112786, 387840, positions =[1,6,7,13,14,18,21,27], step=3)

pseudoWich = pseudo.wichmanGenerator([111, 711, 313],  int(387840/8))


def plot(data, title):
    
    plt.style.use('ggplot')
    plt.ylabel("Frecuencia")
    plt.bar(data.keys(), data.values(), align='center', width=0.8)
    plt.show()

def plotHist(data, title):
    plt.figure(title)
    plt.title(title)
    plt.hist(data)
    plt.show()


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

print("Inicio")
###Para LSFR
fallosLSFR = []
for x in range(1000):
    pseudoLSFR = pseudo.lfsr(2097152 + 123*x, 387840, positions =[1,6,7,13,14,18,21], step=1)
    
    fallosLSFR.append(len([n for n in batteryTests(pseudoLSFR) if n[2]=='Fail']))

plotHist(fallosLSFR, "Tests fallados en cadenas LSFR")
print("Final")












print('Deja a las ratas fluir')
