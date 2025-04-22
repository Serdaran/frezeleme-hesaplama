from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hesaplama():
    sonuc_n = None
    sonuc_vf = None
    if request.method == "POST":
        try:
            vc = float(request.form["vc"])
            d = float(request.form["d"])
            fz = float(request.form["fz"])
            z = int(request.form["z"])

            pi = 3.14159
            n = (1000 * vc) / (pi * d)
            vf = n * fz * z

            sonuc_n = round(n, 2)
            sonuc_vf = round(vf, 2)
        except:
            sonuc_n = "Hesaplanamadı"
            sonuc_vf = "Hesaplanamadı"

    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Frezeleme Teknik Hesaplama</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Frezeleme Devir ve Tabla İlerlemesi Hesaplama</h2>
            <form method="post">
                <label>Vc - Kesme Hızı (m/dk):</label><br>
                <input type="number" step="any" name="vc" required><br><br>

                <label>D - Takım Çapı (mm):</label><br>
                <input type="number" step="any" name="d" required><br><br>

                <label>fz - Diş Başı İlerleme (mm):</label><br>
                <input type="number" step="any" name="fz" required><br><br>

                <label>z - Diş Sayısı:</label><br>
                <input type="number" step="1" name="z" required><br><br>

                <button type="submit">Hesapla</button>
            </form>
            {% if sonuc_n is not none and sonuc_vf is not none %}
                <h3>Hesaplama Sonuçları</h3>
                <p><strong>n (Devir):</strong> {{ sonuc_n }} devir/dk</p>
                <p><strong>Vf (Tabla İlerlemesi):</strong> {{ sonuc_vf }} mm/dk</p>
            {% endif %}
        </body>
        </html>
    """, sonuc_n=sonuc_n, sonuc_vf=sonuc_vf)

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
