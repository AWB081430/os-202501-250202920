def simulasi_fifo(pages, capacity):
    frames = []
    faults = 0
    
    print("=== SIMULASI FIFO (3 Frames) ===")
    print(f"{'Ref':<5} | {'Isi Frame':<15} | {'Status'}")
    print("-" * 35)
    
    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0) 
                frames.append(page)
            faults += 1
            status = "FAULT"
        else:
            status = "HIT"
        
        print(f"{page:<5} | {str(frames):<15} | {status}")
    
    print("-" * 35)
    print(f"Total Page Fault FIFO: {faults}")

dataset = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
simulasi_fifo(dataset, 3)