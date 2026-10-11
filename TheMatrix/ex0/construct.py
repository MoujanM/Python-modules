
import sys
import site
import os

def main():

    if (sys.prefix != sys.base_prefix):

        # prefix pointing to different directory means env detected
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.prefix}")
        print(f"Virtual Environment: {sys.prefix}")
        print(f"Environment Path: {sys.executable}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages withouut affecting the global system.\n")
    
        print(f"Package installation path:\n{site.getsitepackages()[0]}")
    else:
        
        # need instructions to the matrix
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.prefix}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate\t# On Windows")
        print("\nThen run this program again.")

main()
