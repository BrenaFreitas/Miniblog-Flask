# configurar arquivo com lint

import os
import sys
import subprocess

def run_lint():
    print("Running lint")
    subprocess.run(["pylint", "app.py"])
    subprocess.run(["pylint", "run.py"])
    subprocess.run(["pylint", "config.py"])
    subprocess.run(["pylint", "lint.py"])
    print("Lint done")

if __name__ == "__main__":
    run_lint()
    print("Running app")
    os.system("python run.py")
    print("App done")   
    run_lint()