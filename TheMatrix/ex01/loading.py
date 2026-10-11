

from importlib import import_module, metadata


def check_dependencies() -> bool:
    req_flag: bool = True
    my_mods = {'pandas': 'Data manipulation',
               'numpy': 'Numerical computation',
               'matplotlib': 'Visualization',
               'requests': "Network access"}

    print("Checking dependencies:")
    for mod in my_mods:
        str_suff = my_mods.get(mod)
        try:
            import_module(mod)
            print(f"[OK] {mod} ({metadata.version(mod)}) - {str_suff} ready")

        except (metadata.PackageNotFoundError, ModuleNotFoundError):
            req_flag = False
            print(f"{mod} dependency missing")

    return (req_flag)


def do_analysis() -> None:
    import requests
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
    try:
        response = requests.get(url)
        raw_data = response.json()['data']['stations']
        data_points = [s['capacity'] for s in raw_data[:1000]]
    except Exception:
        data_points = np.random.rand(1000)

    print(f"Processing {len(data_points)} data points...")

    df = pd.DataFrame({'signal': data_points})
    df['processed'] = df['signal'] * np.sin(df['signal'])

    print("Generating Visualization...\n")
    plt.figure(figsize=(10, 6))
    plt.plot(df['processed'])
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print("\nInstall dependencies before running program:")
        print("[1] pip install -r requirements.txt\npython3 [program]")
        print("[2] poetry install\npoetry run python [program]")
        return
    else:
        print("\nAnalyzing Matrix data...")
        do_analysis()


main()
