
def crisis_response():
    header = "cyber archives - crisis response system"
    print(f"=== {header.upper()} ===\n")

    archives = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"]

    for archive in archives:
        if archive == "standard_archive.txt":
            print("ROUTINE ACCESS:", end=" ")
        else:
            print("CRISIS ALERT:", end=" ")
        print(f"Attempting access to '{archive}'...")

        try:
            with open(archive) as f:
                content = f.read()
                print(f"SUCCESS: Archive recovered - ''{content}''")
                print("STATUS: Normal operations resumed\n")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except Exception:
            print("RESPONSE: Unknown error detected")
            print("STATUS: Crisis handled, security maintained\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()

