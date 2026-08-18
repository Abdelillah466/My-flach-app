from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/analyze', methods=['GET', 'POST'])
def home():
    result = None
    original_text = ""
    
    if request.method == 'POST':
        # جلب النص المدخل من الفورم
        original_text = request.form.get('text', '')
        
        if original_text:
            # حساب الأرقام والإحصائيات
            words_count = len(original_text.split())
            chars_count = len(original_text)
            
            result = {
                'words': words_count,
                'chars': chars_count
            }

    return render_template('index.html', result=result, original_text=original_text)

if __name__ == '__main__':
    app.run()
