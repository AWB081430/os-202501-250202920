import csv
import os


filename = 'deadlock_data.csv'
data_content = [
    ['Proses', 'Allocation', 'Request'],
    ['P1', 'R1', 'R2'],
    ['P2', 'R2', 'R3'],
    ['P3', 'R3', 'R4'],
    ['P4', 'R4', 'R5'],
    ['P5', 'R5', 'R1']
]

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_content)

print(f"File {filename} berhasil dibuat.\n")


def solve_deadlock():
    allocation = {}  
    request = {}     
    semua_proses = []

    
    with open(filename, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = row['Proses'].strip()
            alloc = row['Allocation'].strip()
            req = row['Request'].strip()
            
            semua_proses.append(p)
            allocation[alloc] = p
            request[p] = req

    
    graph = {}
    for p in semua_proses:
        resource_yang_dicari = request[p]
        if resource_yang_dicari in allocation:
            
            graph[p] = allocation[resource_yang_dicari]

    
    def find_cycle():
        deadlocked = set()
        for p in semua_proses:
            visited = []
            curr = p
            while curr in graph and curr not in visited:
                visited.append(curr)
                curr = graph[curr]
                if curr == p: 
                    deadlocked.update(visited)
                    break
        return deadlocked

    terjebak_deadlock = find_cycle()

    
    print("="*40)
    print(f"{'Proses':<10} | {'Status':<15}")
    print("-" * 40)
    
    for p in semua_proses:
        status = "DEADLOCK" if p in terjebak_deadlock else "AMAN"
        print(f"{p:<10} | {status:<15}")
    
    print("-" * 40)
    if terjebak_deadlock:
        print(f"KESIMPULAN: Sistem Deadlock pada: {sorted(list(terjebak_deadlock))}")
    else:
        print("KESIMPULAN: Sistem Aman.")


if __name__ == "__main__":
    solve_deadlock()