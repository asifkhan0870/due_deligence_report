import zipfile
import os

def create_zip(files, session_id):
    zip_dir = f"outputs/{session_id}"
    zip_path = f"{zip_dir}/all_reports.zip"

    # Ensure directory exists
    os.makedirs(zip_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))

    return zip_path