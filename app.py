from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/")
def home():
    return render_template_string(get_html())

@app.route("/analyze", methods=["POST"])
def analyze():
    user_input = request.form.get("text_data", "")
    word_count = len(user_input.split())
    char_count = len(user_input)
    
    result_msg = f"تم التحليل! عدد الكلمات: {word_count} | عدد الحروف: {char_count}"
    html_content = get_html().replace("<!-- RESULT -->", f"<div class='result'>{result_msg}</div>")
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)