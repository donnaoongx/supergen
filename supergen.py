import os
import subprocess
import shutil
import psutil
from pathlib import Path

def get_unused_files(directory, days_unused=30):
    unused_files = []
    current_time = os.path.getmtime('.')
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_age_days = (current_time - os.path.getmtime(file_path)) / (3600 * 24)
            if file_age_days > days_unused:
                unused_files.append(file_path)
    return unused_files

def clear_unused_files(files):
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def get_unused_applications(days_unused=30):
    unused_apps = []
    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            app_age_days = (psutil.boot_time() - proc.info['create_time']) / (3600 * 24)
            if app_age_days > days_unused:
                unused_apps.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return unused_apps

def clear_unused_applications(applications):
    for app in applications:
        try:
            subprocess.call(['taskkill', '/F', '/IM', app])
            print(f"Closed: {app}")
        except Exception as e:
            print(f"Error closing {app}: {e}")

def main():
    # Define the directory to search for unused files (e.g., Downloads folder)
    directory_to_clean = str(Path.home() / "Downloads")

    print(f"Scanning for unused files in {directory_to_clean}...")
    unused_files = get_unused_files(directory_to_clean)
    clear_unused_files(unused_files)

    print("Scanning for unused applications...")
    unused_apps = get_unused_applications()
    clear_unused_applications(unused_apps)

    print("Cleanup completed.")

if __name__ == "__main__":
    main()