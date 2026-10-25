import os

print("Running pre-build resource cleanup to remove $ from filenames...")
count = 0
for root, dirs, files in os.walk("."):
    if ".git" in root or "build" in root or "dist" in root:
        continue
    for f in files:
        if "$" in f:
            old_path = os.path.join(root, f)
            new_file = f.replace("$", "s_")
            new_path = os.path.join(root, new_file)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
            count += 1

print(f"Cleanup complete. Total files fixed: {count}")
