import os 
import requests
from dotenv import load_dotenv

# cargar variables de entorno 
load_dotenv()

#constantes
API_KEY = os.getenv("API_KEY_SARCH_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
SEARCH_QUERY = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
LANGUAGE_RESTRICTION = "lang_es"
START_PAGE = 1
API_URL = "https://cse.google.com/cse?cx=211650725cc1e4563"

def build_search_url(api_key: str, search_engine_id: str, query: str, start: int, lang: str) -> str:
    """Construye la URL para la API de búsqueda personalizada de Google."""
    return (
        f"{API_URL}?key={api_key}&cx={search_engine_id}&q={query}&start={start}&lr={lang}"
    )

def perform_search(url: str) -> dict:
    """Realiza una solicitud GET a la URL especificada y retorna la respuesta como JSON."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"Error al realizar la solicitud: {error}")
        return {}

def display_search_results(items: list) -> None:
    """Imprime los resultados de búsqueda de forma legible."""
    if not items:
        print("No se encontraron resultados.")
        return

    for item in items:
        title = item.get("title", "Sin título")
        link = item.get("link", "Sin enlace")
        snippet = item.get("snippet", "Sin descripción")

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 80)

def main():
    """Función principal para ejecutar la búsqueda."""
    if not API_KEY or not SEARCH_ENGINE_ID:
        print("Faltan las variables de entorno necesarias (API_KEY o SEARCH_ENGINE_ID).")
        return

    search_url = build_search_url(API_KEY, SEARCH_ENGINE_ID, SEARCH_QUERY, START_PAGE, LANGUAGE_RESTRICTION)
    data = perform_search(search_url)
    search_results = data.get("items", [])
    display_search_results(search_results)

if __name__ == "__main__":
    main()