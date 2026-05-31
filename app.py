import gradio as gr
import numpy as np
import joblib

rf = joblib.load("model_random_forest.pkl")

def predict_risk(latitude, longitude, bright_ti4, bright_ti5,
                 scan, track, acq_time, day_of_year, is_day, confidence):
    
    confidence_map = {"baixa (l)": 0, "nominal (n)": 1, "alta (h)": 2}
    input_data = np.array([[latitude, longitude, bright_ti4, bright_ti5,
                            scan, track, acq_time, day_of_year,
                            int(is_day), confidence_map[confidence]]])
    
    proba = rf.predict_proba(input_data)[0][1]
    risco = "🔴 ALTO RISCO" if proba >= 0.5 else "🟢 BAIXO RISCO"
    return f"{risco}\nProbabilidade: {proba:.1%}"

app = gr.Interface(
    fn=predict_risk,
    inputs=[
        gr.Number(label="Latitude", value=-8.87),
        gr.Number(label="Longitude", value=-46.93),
        gr.Number(label="Bright TI4 (K)", value=320.0),
        gr.Number(label="Bright TI5 (K)", value=295.0),
        gr.Number(label="Scan", value=0.4),
        gr.Number(label="Track", value=0.4),
        gr.Number(label="Horário (acq_time)", value=1400),
        gr.Number(label="Dia do ano", value=150),
        gr.Checkbox(label="É diurno?", value=True),
        gr.Dropdown(["baixa (l)", "nominal (n)", "alta (h)"], label="Confiança", value="nominal (n)"),
    ],
    outputs=gr.Textbox(label="Resultado"),
    title="OrbitWatch — Predição de Risco de Queimada",
    description="Insira os dados do satélite VIIRS para classificar o nível de risco do foco."
)

app.launch(server_name="0.0.0.0", server_port=8000)