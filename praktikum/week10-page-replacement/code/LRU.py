def simulasi_lru(pages, capacity):
    frames = []
    history = [] 
    faults = 0
    
    print("=== SIMULASI LRU (3 Frames) ===")
    print(f"{'Ref':<5} | {'Isi Frame':<15} | {'Status'}")
    print("-" * 35)
    
    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
                history.append(page)
            else:
                
                lru_page = history.pop(0)
                frames.remove(lru_page)
                frames.append(page)
                history.append(page)
            faults += 1
            status = "FAULT"
        else:
            
            history.remove(page)
            history.append(page)
            status = "HIT"
        
        print(f"{page:<5} | {str(frames):<15} | {status}")
    
    print("-" * 35)
    print(f"Total Page Fault LRU: {faults}")

dataset = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
simulasi_lru(dataset, 3)