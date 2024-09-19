#!/usr/bin/env python3

import json
import os
from pathlib import Path
import subprocess

import pycyphal

project_root = Path(os.getenv("PROJECT_ROOT"))

std_packages = ["external/public_regulated_data_types/uavcan", "external/public_regulated_data_types/reg"]
if env_dsdl_packages := os.getenv("DSDL_PACKAGES"):
    custom_packages = json.loads(env_dsdl_packages)
else:
    custom_packages = [project_root / "cyphal-types" / "voltbro"]
packages = [*std_packages, *custom_packages]

output = os.getenv("DSDL_OUTPUT")
print(f"Compiling output to {output}")

print("Compiling all python types...", end='')
pycyphal.dsdl.compile_all(packages, output_directory=output)
print(" Done")

for pkg in packages:
    print(f"Compiling C/C++ types for {pkg}...", end='')
    subprocess.call([
        "nnvg",
        "--target-language",
        "c",
        "--target-endianness=little",
        pkg,
        "--lookup-dir",
        "external/public_regulated_data_types/uavcan",
        "--outdir",
        "common"
    ])
    print(" Done")
