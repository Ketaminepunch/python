# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/17 17:27:24 by vsack           #+#    #+#               #
#  Updated: 2026/05/30 19:49:21 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import importlib.metadata as md

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


REQUIRED: list[tuple[str, str]] = [
    ("numpy", "Numerical computation ready"),
    ("pandas", "Data manipulation ready"),
    ("matplotlib", "Visualization ready"),
]


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_ok = True
    for name, desc in REQUIRED:
        try:
            version = md.version(name)
            print(f"[OK] {name} ({version}) - {desc}")
        except md.PackageNotFoundError:
            print(f"[MISSING] {name} - install with: pip install {name}"
                  f" or install with poetry add {name}")
            all_ok = False
    return all_ok


def analyser() -> None:
    print("\nAnalyzing Matrix Data...")
    print("Processing 1000 data points...")
    data = np.random.randint(0, 5000, size=1000)
    df = pd.DataFrame(data, columns=["value"])
    print(df.describe().round(2))
    print("Generating visualization...")
    plt.plot(df)
    plt.savefig('matrix_analysis.png')
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    if not check_dependencies():
        print("\nMissing dependencies. Aborting.")
        sys.exit(1)
    analyser()
