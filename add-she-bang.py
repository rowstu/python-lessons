import os

# add missing to shebangs to any scripts in the scripts directory

directory = os.path.expanduser('~/scripts')

for filename in os.listdir(directory):
    if filename.endswith(".sh"):
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as file:
            firstline = file.readline()

        if not firstline.startswith("#!"):
            print(f"Adding shebang to {filename}")
            with open(file_path, 'r') as original:
                lines = original.read()
            with open(file_path, 'w') as modified:
                modified.write("#!/bin/bash\n" + lines)
