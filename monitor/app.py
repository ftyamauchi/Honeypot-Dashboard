import json
import subprocess
from pathlib import Path

from flask import Flask

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FILE = BASE_DIR / "services" / "cowrie" / "var" / "log" / "cowrie" / "cowrie.json"
COWRIE_DIR = BASE_DIR / "services" / "cowrie"
COWRIE_CMD = COWRIE_DIR / "cowrie-env" / "bin" / "cowrie"


def verificar_cowrie():
    try:
        resultado = subprocess.run(
            [str(COWRIE_CMD), "status"],
            cwd=str(COWRIE_DIR),
            capture_output=True,
            text=True
        )

        if "is running" in resultado.stdout.lower():
            return "🟢 Online"

    except Exception:
        pass

    return "🔴 Offline"


def formatar_lista(lista):
    if not lista:
        return "Nenhum registro"

    return ", ".join(sorted(lista))


def formatar_comandos(comandos):
    if not comandos:
        return "<p>Nenhum comando registrado.</p>"

    html = "<ul>"

    for comando in comandos:
        html += f"<li>{comando}</li>"

    html += "</ul>"

    return html


def ler_dados():
    total_eventos = 0
    dados_por_ip = {}

    if not LOG_FILE.exists():
        return total_eventos, dados_por_ip

    with open(LOG_FILE, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                evento = json.loads(linha)
            except json.JSONDecodeError:
                continue

            total_eventos += 1

            ip = evento.get("src_ip")

            if not ip:
                continue

            if ip not in dados_por_ip:
                dados_por_ip[ip] = {
                    "eventos": 0,
                    "usuarios": set(),
                    "senhas": set(),
                    "comandos": [],
                    "ultima_atividade": ""
                }

            dados_por_ip[ip]["eventos"] += 1

            if "username" in evento:
                dados_por_ip[ip]["usuarios"].add(evento["username"])

            if "password" in evento:
                dados_por_ip[ip]["senhas"].add(evento["password"])

            if "input" in evento:
                dados_por_ip[ip]["comandos"].append(evento["input"])

            if "timestamp" in evento:
                dados_por_ip[ip]["ultima_atividade"] = evento["timestamp"]

    return total_eventos, dados_por_ip


@app.route("/")
def index():
    status = verificar_cowrie()
    total_eventos, dados = ler_dados()

    conteudo = f"""
    <h1>Honeypot Dashboard</h1>

    <p><b>Status do Cowrie:</b> {status}</p>

    <p><b>Total de eventos:</b> {total_eventos}</p>

    <p><b>IPs encontrados:</b> {len(dados)}</p>

    <hr>
    """

    for ip, info in dados.items():
        conteudo += f"""
        <h2>IP: {ip}</h2>

        <p><b>Eventos:</b> {info["eventos"]}</p>

        <p><b>Usuários:</b> {formatar_lista(info["usuarios"])}</p>

        <p><b>Senhas:</b> {formatar_lista(info["senhas"])}</p>

        <p><b>Comandos:</b></p>

        {formatar_comandos(info["comandos"])}

        <p><b>Última atividade:</b> {info["ultima_atividade"]}</p>

        <hr>
        """

    return f"""
    <html>
    <head>
        <title>Honeypot Dashboard</title>
        <meta http-equiv="refresh" content="3">
    </head>
    <body>
        {conteudo}
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
