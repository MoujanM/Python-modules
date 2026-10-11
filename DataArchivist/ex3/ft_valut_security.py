
def valut_security():
    header = "cyber archives - valut security system"
    print(f"=== {header.upper()} ===\n")

    print("Initializing secure valut access...")
    print("Vault connection established with failsafe protocols\n")
    with open("classified_data.txt") as ex_vault:
        print("SECURE EXTRACTION:")
        print(ex_vault.read())
    
    with open("security_protocols.txt") as pres_vault:
        print("\nSECURE PRESERVATION:")
        print(pres_vault.read())
        print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")

if __name__ == "__main__":
    valut_security()