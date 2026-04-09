import zipfile
import os

def create_zip(files, session_id):
    zip_path = f"outputs/{session_id}/all_reports.zip"

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file)

    return zip_path