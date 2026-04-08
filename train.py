import sys
import os

with open(os.path.join("dataset", "processed_data.txt"), "r") as f:
    data = f.read()

model = f"Model trained on data: {data}"

with open("model.txt", "w") as f:
    f.write(model)
