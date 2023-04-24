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
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (temp * 1.8) + 32
        elif to_unit == 'Kelvin':
            return temp + 273.15
        else:
            return temp
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (temp - 32) / 1.8
        elif to_unit == 'Kelvin':
            return (temp + 459.67) * 5 / 9
        else:
            return temp
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return temp - 273.15
        elif to_unit == 'Fahrenheit':
            return (temp * 9 / 5) - 459.67
        else:
            return temp
    else:
        return temp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)