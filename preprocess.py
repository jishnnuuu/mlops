import sys
import os

with open(os.path.join("dataset", "data.txt"), "r") as f:
    data = f.read()

processed_data = data.upper()

with open(os.path.join("dataset", "processed_data.txt"), "w") as f:
    f.write(processed_data)
