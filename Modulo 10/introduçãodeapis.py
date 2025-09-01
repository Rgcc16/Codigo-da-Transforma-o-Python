# ==============================================================
# AVISO: Este código foi desenvolvido com auxílio de Inteligência Artificial
# ==============================================================
import requests

# Previsão do tempo
def previsao_tempo():
    cidade = input("Digite a cidade: ")
    api_key = "SUA_CHAVE_API"  # substitua pela sua chave do OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        dados = r.json()
        print("Temperatura:", dados["main"]["temp"], "°C")
        print("Clima:", dados["weather"][0]["description"])
    except Exception as e:
        print("Erro ao buscar clima:", e)

# Buscar filmes
def buscar_filme():
    nome = input("\nDigite o nome do filme: ")
    api_key = "SUA_CHAVE_TMDB"  # substitua pela sua chave do TMDB
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome}&language=pt-BR"

    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        dados = r.json()
        if dados["results"]:
            filme = dados["results"][0]
            print("Título:", filme["title"])
            print("Sinopse:", filme["overview"])
            print("Lançamento:", filme["release_date"])
        else:
            print("Nenhum filme encontrado.")
    except Exception as e:
        print("Erro ao buscar filme:", e)

# Execução
if __name__ == "__main__":
    previsao_tempo()
    buscar_filme()