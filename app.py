from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        temp = float(request.form['temp'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert(temp, from_unit, to_unit)
        return render_template('index.html', result=result, temp=temp, from_unit=from_unit, to_unit=to_unit)
    return render_template('index.html')

def convert(temp, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return round((temp * 9/5) + 32, 2)
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return round((temp - 32) * 5/9, 2)
    else:
        return temp

if __name__ == '__main__':
    app.run(debug=True)