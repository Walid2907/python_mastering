import sys
import os
import site


python_path = sys.executable
# sys.prefix: The prefix of the Python installation used to run the script.
# sys.base_prefix: The prefix of the "base" Python installation
prefix = sys.prefix
base_prefix = sys.base_prefix
in_venv = prefix != base_prefix

# If we are in a virtual environment, 'prefix' (current env) will be different
# from 'base_prefix' (system python). If they are the same, we are in the global scope.
if in_venv:
    print("MATRIX STATUS: Welcome to the construct\n")
else:
    print("MATRIX STATUS: You're still plugged in\n")
print(f"Current Python: {python_path}")

if in_venv:
    print(f"Virtual Environment: {os.path.basename(prefix)}")
    print(f"Environment Path: {prefix}")
    print("\nSUCCESS: You're in an isolated environment!"
          " Safe to install packages without affecting"
          " the global system.\n")
    # Get the site-packages directory where libraries are installed
    site_packages = site.getsitepackages()[0]
    print(f"\nPackage installation path:\n{site_packages}")
else:
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python3 -m virtualenv matrix_env")
    print("source myenv/bin/activate# On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows\n")
    print("Then run this program again.")
