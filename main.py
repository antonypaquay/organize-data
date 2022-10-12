file_path = "/Users/antonypaquay/Dev/organize-data/prenoms.txt"

with open(file_path, "r") as f:
    lines = f.read().splitlines()

names = []
for line in lines:
    names.extend(line.split())

cleaned_names = [name.strip(",. ") for name in names]

with open(file_path, "w") as f:
    f.write("\n".join(sorted(cleaned_names)))
