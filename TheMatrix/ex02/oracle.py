import os
from dotenv import load_dotenv, dotenv_values

def check_config() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    
    load_dotenv()
    mode = os.getenv('MATRIX_MODE', 'development')

    if mode == "development":
        database_status = "Connected to local instance"
        log_status = "DEBUG"
    else:
        database_status = "Connected to Zion Network"
        log_status = "ERROR"
    
    print(f"Mode: {mode}")
    print(f"Database: {database_status}")
    print(f"API Access: {'Authenticated' if os.getenv('API_KEY') else 'Key missing'}")
    print(f"Log Level: {log_status}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")


def check_security() -> None:
    print("Environment security check:")
    with open(__file__, 'r') as f:
        content = f.read()
        to_search = ("API" + "_KEY = '")
        if to_search in content:
            print("[WARNING] Some secrets are exposed")
        else:
            print("[OK] No hardcoded secrets detected")

    if os.path.exists("ex02/.env"):
        cloaked = False
        if os.path.exists("ex02/.gitignore"):
            with open("ex02/.gitignore", "r") as g:
                if ".env" in g:
                    cloaked = True
        if cloaked:
            print("[OK] .env file properly configured")
        else:
            print("[ERROR] .env file exists but not cloaked")
    else:
        print("[ERROR] .env file missing")

    config_file = dotenv_values("ex02/.env")
    current_mode = os.getenv("MATRIX_MODE")

    if current_mode != config_file.get("MATRIX_MODE"):
        print("[ERROR] Production override disabled")
    else:
        print("[OK] Production override available")

    
def main() -> None:
    check_config()
    print()
    check_security()
    print("\nThe Oracle sees all configurations.")

main()
