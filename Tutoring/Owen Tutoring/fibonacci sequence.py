# fibonacci sequence

seq = [0]
x = 1

for i in range(10):
    seq.append(x)
    x = seq[-1] + seq[-2]

print(seq)

seqSum = []
j = 0
sum = 0
for i in range(len(seq)):
    while j <= i:
        sum += seq[j]
        j += 1
    seqSum.append(sum)
    sum = 0
    j = 0

print(seqSum)