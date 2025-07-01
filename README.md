# file_integrity_tool
project 
🔐 File Integrity Checker using Python (GUI)
This tool monitors changes in files inside a selected folder by calculating and comparing SHA-256 hash values. It's useful for detecting file tampering, ensuring data integrity, and basic cybersecurity audits.

📌 Features
🧮 Calculates SHA-256 hash for every file

🔄 Detects:

✅ No changes

⚠️ Modified files

➕ Newly added files

❌ Deleted files

🖥️ Simple GUI with Tkinter

📂 Folder selection dialog

🔁 Supports one-time or auto monitoring (every 10 seconds)

💾 Stores hash data in file_hashes.json

📁 Project Structure
bash
Copy
Edit
📁 FileIntegrityMonitor/
├── file_hashes.json       # Auto-generated file storing hash records
├── file_integrity_monitor.py  # Main Python script
🚀 How It Works (Step by Step)
User selects a folder through the GUI.

The tool scans all files inside the selected folder.

It calculates a SHA-256 hash for each file.

It compares current hashes with saved hashes in file_hashes.json.

It shows in the GUI:

Which files are added, modified, or deleted

Or no changes

It updates file_hashes.json with the latest hashes after each scan.

You can choose:

📌 Run Once (manual check)

🔁 Auto Monitor (checks every 10 seconds)

🛠️ Requirements
Python 3.6+

Tkinter (comes pre-installed with Python)

✅ How to Run
Clone this repository

bash
Copy
Edit
git clone https://github.com/your-username/FileIntegrityMonitor.git
cd FileIntegrityMonitor
Run the script

bash
Copy
Edit
python file_integrity_monitor.py
📷 GUI Preview
(Optional: Add screenshots of your app here)

📜 License
This project is open-source and free to use.
