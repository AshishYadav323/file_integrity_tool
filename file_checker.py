import os
import hashlib
import json
from pathlib import Path

HASH_RECORD_FILE = "file_hashes.json"

def calculate_hash(file_path):
    """Calculate SHA-256 hash of the file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def load_hashes():
    """Load stored hash values."""
    if Path(HASH_RECORD_FILE).exists():
        with open(HASH_RECORD_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    """Save updated hash values."""
    with open(HASH_RECORD_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

def scan_directory(directory):
    """Scan directory and compute file hashes."""
    current_hashes = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)
            if file_hash:
                current_hashes[file_path] = file_hash
    return current_hashes

def monitor_changes(directory):
    """Monitor and report changes."""
    print(f"Scanning directory: {directory}")
    old_hashes = load_hashes()
    new_hashes = scan_directory(directory)

    modified = []
    added = []
    deleted = []

    # Check for modified and deleted files
    for path, old_hash in old_hashes.items():
        new_hash = new_hashes.get(path)
        if new_hash is None:
            deleted.append(path)
        elif new_hash != old_hash:
            modified.append(path)

    # Check for newly added files
    for path in new_hashes:
        if path not in old_hashes:
            added.append(path)

    # Show results
    print("\n🛠️  File Change Summary:")
    if modified:
        print(f"⚠️  Modified files:\n" + "\n".join(modified))
    if added:
        print(f"➕ Added files:\n" + "\n".join(added))
    if deleted:
        print(f"❌ Deleted files:\n" + "\n".join(deleted))
    if not (modified or added or deleted):
        print("✅ No changes detected.")

    # Update hash records
    save_hashes(new_hashes)

# === MAIN EXECUTION ===
if __name__ == "__main__":
    folder_to_monitor = input("Enter the directory to monitor: ").strip()
    if not os.path.isdir(folder_to_monitor):
        print("❗Invalid directory.")
    else:
        monitor_changes(folder_to_monitor)
