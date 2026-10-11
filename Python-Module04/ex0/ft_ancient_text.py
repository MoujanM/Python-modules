
def recovery_system() -> None:
    header = "cyber archives - data recovery system"
    print(f"=== {header.upper()} ===\n")
    vault = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {vault}")
    try:
        fragment = open(vault, mode='r')
        print("Connection Established...\n")
        print("RECOVERED DATA:")
        print(fragment.read())
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        fragment.close()


if __name__ == "__main__":
    recovery_system()
