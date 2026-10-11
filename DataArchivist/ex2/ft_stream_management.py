
import sys


def stream_manager():
    header = "=== cyber archives - communication system ==="
    sys.stdout.write(header.upper() + '\n\n')

    # input stream:
    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    # stream channels
    sys.stdout.write("\n[STANDARD] ")
    print(f"Archive status from {arch_id}: {status}", file=sys.stdout)
    sys.stderr.write("[ALERT] System diagnostic: ")
    print("Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete")

    print("\nThree-channel commuication test successful.")


if __name__ == "__main__":
    stream_manager()
