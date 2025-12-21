
proses = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3)
]

waktu = 0

print("Proses | Arrival | Burst | Waiting | Turnaround")
print("-" * 50)

for p in proses:
    nama = p[0]
    arrival = p[1]
    burst = p[2]

    if waktu < arrival:
        waktu = arrival

    waiting = waktu - arrival
    turnaround = waiting + burst

    waktu = waktu + burst

    print(f"{nama:>5} | {arrival:>7} | {burst:>5} | {waiting:>7} | {turnaround:>10}")
