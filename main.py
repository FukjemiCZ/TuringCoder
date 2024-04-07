from pathlib import Path
import sys
from config import *
from lib.preparation import prepare_output_file
from lib.structure import add_directory_structure
from lib.file_content import process_files
from lib.openai_integration import send_to_chatgpt

# Ověření, že byl zadán parametr
if len(sys.argv) < 2:
    print("Chyba: Nebyl zadán název služby jako parametr.")
    exit(1)

service_name = sys.argv[1]
output_file = Path(OUTPUT_DIR) / f"{service_name}.md"
response_file = Path(RESPONSE_DIR) / f"{service_name}.md"
start_file = Path(TEMPLATE_DIR) / f"{service_name}.md"

print (APP_DIR)
# Kontrola existence startovního souboru
if not start_file.exists():
    print(f"Chyba: Startovní soubor '{start_file}' neexistuje.")
    exit(1)

prepare_output_file(output_file, start_file)
add_directory_structure(APP_DIR, output_file)
process_files(APP_DIR, output_file)
send_to_chatgpt(OPENAI_API_KEY, OPENAI_MODEL, output_file, response_file)

print(f"Sloučení dokončeno. Výsledek je v souboru {output_file}")
