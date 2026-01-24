import bz2

file_path = "data/raw/lanl-auth-dataset-1-00.bz2"

with bz2.open(file_path, "rt") as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i == 5:
            break
