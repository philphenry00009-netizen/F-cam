import os

print("Starting aggressive dollar-sign resource cleanup...")
count = 0

# Walk bottom-up (topdown=False) so we rename files before their parent directories if needed
for root, dirs, files in os.walk(".", topdown=False):
    for f in files:
        if "$" in f:
            old_path = os.path.join(root, f)
            new_file = f.replace("$", "s_")
            new_path = os.path.join(root, new_file)
            try:
                os.rename(old_path, new_path)
                print(f"RENAMED FILE: {old_path} -> {new_path}")
                count += 1
            except Exception as e:
                print(f"Error renaming {old_path}: {e}")

    for d in dirs:
        if "$" in d:
            old_path = os.path.join(root, d)
            new_dir = d.replace("$", "s_")
            new_path = os.path.join(root, new_dir)
            try:
                os.rename(old_path, new_path)
                print(f"RENAMED DIR: {old_path} -> {new_path}")
                count += 1
            except Exception as e:
                print(f"Error renaming dir {old_path}: {e}")

print(f"Aggressive cleanup complete. Total renamed: {count}")
