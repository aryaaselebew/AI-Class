#Quiz
#Arya Nanda Putra_F55123087
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
x = 5

kemunculan = A.count(x)

indeks_kemunculan = [i for i, nilai in enumerate(A) if nilai == x]

print("Kemunculan x:", kemunculan)
print("Indeks kemunculan x:", indeks_kemunculan)