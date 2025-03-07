from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Carregar modelo e vetorizador treinados
modelo = joblib.load("modelo.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    sentimento = None
    texto = ""

    if request.method == "POST":
        texto = request.form["texto"]
        texto_vetorizado = vectorizer.transform([texto])
        previsao = modelo.predict(texto_vetorizado)[0]

        # Mapear resultado
        sentimentos = {-1: "Negativo 😔", 0: "Neutro 😐", 1: "Positivo 😊"}
        resultado = sentimentos[previsao]

        return render_template("index.html", resultado=resultado, texto=texto)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="", port=)
