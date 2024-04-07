Pokud se objeví Error prosím zobrazit jej v příkazové řádce

Jako například tento 
{
    "error": {
        "message": "Incorrect API key provided: x. You can find your API key at https://platform.openai.com/account/api-keys.",
        "type": "invalid_request_error",
        "param": null,
        "code": "invalid_api_key"
    }
}

# Můj zdroják
#!/bin/bash

# Načtení konfiguračních proměnných
source "$(dirname "$0")/config"

# Ověření, že byl zadán parametr
if [ -z "$1" ]; then
    echo "Chyba: Nebyl zadán název služby jako parametr."
    exit 1
fi

service_name="$1"
output_file="$OUTPUT_DIR/$service_name.md"
response_file="$RESPONSE_DIR/$service_name.md"
start_file="$TEMPLATE_DIR/$service_name.md"

# Kontrola existence startovního souboru
if [ ! -f "$start_file" ]; then
    echo "Chyba: Startovní soubor '$start_file' neexistuje."
    exit 1
fi

# Příprava výstupního souboru
mkdir -p "$(dirname "$output_file")"
echo "" > "$output_file"

# Kopírování startovního obsahu
cat "$start_file" >> "$output_file"

# Přidání adresářové struktury
echo "## Adresářová struktura složky '$APP_DIR'\n" >> "$output_file"
if tree $APP_DIR >> "$output_file" 2>/dev/null; then
    echo "Používám 'tree' pro výpis struktury."
else
    find $APP_DIR -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g' >> "$output_file"
fi
echo '\n' >> "$output_file"

# Funkce pro přidání obsahu souboru
add_file_content() {
    local file_path="$1"
    local relative_path="${file_path#$APP_DIR/}"
    echo -e "# $relative_path\n" >> "$output_file"
    echo '```' >> "$output_file"
    cat "$file_path" >> "$output_file"
    echo -e '\n```\n' >> "$output_file"
}

# Export proměnných a funkcí pro jejich použití v podprocesech
export -f add_file_content
export output_file
export APP_DIR

# Zpracování souborů v aplikaci
find "$APP_DIR" -type f -exec bash -c 'add_file_content "$0"' {} \;

# Po dokončení vytvoření output file, pokud je OpenAI API klíč nastaven, pošlete obsah do ChatGPT API
if [ ! -z "$OPENAI_API_KEY" ]; then
    input_text=$(cat "$output_file")

    # Použití curl pro odeslání požadavku na ChatGPT API
    response=$(curl -s -X POST -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -d "{\"model\": \"gpt-3.5-turbo\", \"prompt\": \"$input_text\", \"temperature\": 0.7, \"max_tokens\": 2048}" \
        "https://api.openai.com/v1/completions")

    # Uložení odpovědi API do souboru
    echo "$response" > "$response_file"

    echo "Odpověď od ChatGPT API je uložena v souboru $response_file"
else
    echo "OpenAI API klíč není nastaven. Volání ChatGPT nebude provedeno."
fi

echo "Sloučení dokončeno. Výsledek je v souboru $output_file"
