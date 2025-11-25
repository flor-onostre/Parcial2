import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def buscar(request):
    query = request.GET.get("q", "")
    resultados = []
    error = None
    if query:
        try:
            url = f"https://es.wikipedia.org/wiki/{query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
            }
            resp = requests.get(url, timeout=5, headers=headers)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            titulo = soup.find("h1").get_text(strip=True)
            parrafos = soup.select("p")
            snippets = [p.get_text(strip=True) for p in parrafos[:3] if p.get_text(strip=True)]
            resultados.append({"titulo": titulo, "snippets": snippets, "url": url})
        except Exception as exc:  # pragma: no cover - muestra errores en UI
            error = f"Error al obtener la pagina: {exc}"
    return render(
        request, "scraper/buscar.html", {"query": query, "resultados": resultados, "error": error}
    )

# Create your views here.
