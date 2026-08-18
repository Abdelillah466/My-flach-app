from flask import Flask, render_template, request

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# مسار استقبال البيانات والتحليل
@app.route('/analyze', methods=['POST', 'GET'])
def analyze():
    if request.method == 'POST':
        # هنا يمكنك استقبال البيانات من الفورم
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
