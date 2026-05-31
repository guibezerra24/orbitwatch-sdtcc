from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>OrbitWatch</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:'Segoe UI',sans-serif; background:#0a0e1a; color:#fff; }
        header { background:#0d1b2a; padding:20px 40px; border-bottom:1px solid #1e3a5f; }
        header h1 { color:#4fc3f7; font-size:24px; }
        header p { color:#90a4ae; font-size:13px; margin-top:4px; }
        .hero { text-align:center; padding:80px 20px 40px; }
        .hero h2 { font-size:42px; }
        .hero h2 span { color:#ff6b35; }
        .hero p { color:#90a4ae; font-size:18px; margin-top:16px; max-width:600px; margin-inline:auto; }
        .btn { display:inline-block; margin-top:32px; padding:14px 32px; background:#ff6b35; color:#fff; border-radius:8px; text-decoration:none; font-weight:700; font-size:16px; }
        .badges { display:flex; justify-content:center; gap:20px; margin-top:40px; flex-wrap:wrap; }
        .badge { background:#0d1b2a; border:1px solid #1e3a5f; border-radius:12px; padding:20px 28px; text-align:center; }
        .badge .value { font-size:28px; font-weight:700; color:#4fc3f7; }
        .badge .label { font-size:13px; color:#90a4ae; margin-top:4px; }
        .cards { display:flex; justify-content:center; gap:24px; padding:60px 40px; flex-wrap:wrap; }
        .card { background:#0d1b2a; border:1px solid #1e3a5f; border-radius:16px; padding:28px; max-width:280px; }
        .card h3 { color:#4fc3f7; margin-bottom:10px; }
        .card p { color:#90a4ae; font-size:14px; line-height:1.6; }
        footer { text-align:center; padding:20px; color:#546e7a; font-size:13px; border-top:1px solid #1e3a5f; }
    </style>
</head>
<body>
    <header>
        <h1>🛰️ OrbitWatch</h1>
        <p>Monitoramento de Queimadas via Dados Satelitais — FIAP Global Solution 2026</p>
    </header>
    <div class="hero">
        <h2>O espaço protegendo <span>a Terra</span></h2>
        <p>Plataforma integrada de detecção e alerta de queimadas usando dados orbitais da NASA em tempo quase real.</p>
        <a class="btn" href="https://huggingface.co/spaces/Gui24/orbitwatch" target="_blank">🔥 Acessar Demo — Predição de Queimadas</a>
        <div class="badges">
            <div class="badge"><div class="value">98%</div><div class="label">Acurácia CNN</div></div>
            <div class="badge"><div class="value">0.90</div><div class="label">AUC-ROC ML</div></div>
            <div class="badge"><div class="value">6.900+</div><div class="label">Focos analisados</div></div>
            <div class="badge"><div class="value">&lt;3h</div><div class="label">Tempo de alerta</div></div>
        </div>
    </div>
    <div class="cards">
        <div class="card"><h3>🔥 Detecção de Focos</h3><p>Coleta dados do satélite VIIRS (NASA FIRMS) e classifica focos de calor em alto ou baixo risco usando Machine Learning.</p></div>
        <div class="card"><h3>🖼️ Visão Computacional</h3><p>CNN treinada do zero classifica imagens satelitais com 98% de acurácia em floresta, vegetação, área residencial ou água.</p></div>
        <div class="card"><h3>🚨 Alertas Automáticos</h3><p>Bot RPA monitora continuamente e dispara notificações por e-mail quando novos focos de alto risco são detectados.</p></div>
        <div class="card"><h3>📊 Pipeline de Dados</h3><p>Apache Airflow orquestra a ingestão, transformação e carga dos dados orbitais para análise contínua.</p></div>
    </div>
    <footer>OrbitWatch · FIAP Global Solution 2026 · Engenharia de Software 4º Ano</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run()