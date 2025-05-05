from flask import Flask, render_template, request
from billing import generate_monthly_bill
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        items_json = request.form['items']
        target_month = request.form['month']
        try:
            item_list = json.loads(items_json)
            result = generate_monthly_bill(item_list, target_month)
        except Exception as e:
            result = {'error': str(e)}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
