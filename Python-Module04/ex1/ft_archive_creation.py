
def create_archive():
    header = "cyber archives - preservation system"
    print(f"=== {header.upper()} ===\n")
    name = "new_discovery.txt"
    data = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
        ]
    print(f"Initializing new storage unit: {name}")
    
    # check if file already exists if so, abort
    try:
        checking = open(name, mode='r')
        checking.close()
        print(f"ERROR: storage unit named '{name}' already exists.")
        print("Initializing new storage unit aborted.")
        return
    except FileNotFoundError:
        pass


    try:
        new = open(name, mode='w')
        print("Storage unit created successfully...\n")
        for datum in data:
            new.write(datum + "\n")
            print(datum)
        new.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{name}' ready for long-term preservation.")
    except FileExistsError:
        print(f"ERROR: storage unit named '{name}' already exists.")


if __name__ == "__main__":
    create_archive()