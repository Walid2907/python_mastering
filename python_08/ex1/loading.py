import sys
import importlib


RESET_CODE = "\033[0m"
RED_CODE = "\033[91m"
GREEN_CODE = "\033[32m"
BLUE_CODE = "\033[34m"
YELLOW_CODE = "\033[33m" 

REQUIRED_PACKAGES = ["pandas", "requests", "matplotlib"]


def check_dependencies():
    missing = []
    installed = {}

    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
            version = module.__version__
            print(f"{GREEN_CODE}[OK]{RESET_CODE} {package} ({version}) - {YELLOW_CODE}Ready{RESET_CODE}")
            installed[package] = version
        except ImportError:
            print(f"{RED_CODE}[MISSING]{RESET_CODE} {package} - {YELLOW_CODE}Not installed{RESET_CODE}")
            missing.append(package)

    return missing, installed

def install_instructions() -> None:
    print("\nto install missing dependencies ")
    print(BLUE_CODE + "using pip: " + RESET_CODE)
    print(GREEN_CODE + "pip install -r requirements.txt" + RESET_CODE)
    print(BLUE_CODE + "using poetry (Suggested): " + RESET_CODE)
    print(GREEN_CODE + "run : poetry install" + RESET_CODE)

def run_analysis():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    # Simulate Matrix data
    np.random.seed(42)
    numbers = np.random.randint(1, 101, size=1000)
    data = pd.DataFrame({"value": numbers})

    print(f"Processing {len(data)} data points...")
    print("Generating visualization...")

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(1, 21)

    ax.plot(x, numbers[:20], color='steelblue', marker='o', linewidth=2, markersize=6, label='Matrix Signal')
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.grid(True)
    ax.legend()

    output = "matrix_analysis.png"
    plt.savefig(output)
    plt.close()

    print(f"\nAnalysis complete!")
    print(f"Results saved to: {output}")

print("LOADING STATUS: Loading programs...\n")
print("Checking dependencies:")


# pandas check
missing, installed = check_dependencies()

if missing:
    install_instructions()
    sys.exit(1)

run_analysis()

