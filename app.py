from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chemical_calculator():
    if request.method == 'POST':
        try:
            concentration = float(request.form['concentration'])
            molar_mass = float(request.form['molar_mass'])
            volume = float(request.form['volume'])  # Volume in liters
            required_mass = concentration * molar_mass * volume  # mass = c * M * V

            advice = ""
            if required_mass < 0.01:
                advice = "Consider diluting a higher concentration stock solution."
            else:
                advice = "Weigh out the required mass directly."
                
            return render_template('result.html', required_mass=required_mass, advice=advice)
        except ValueError:
            return "Invalid input. Please enter valid numbers."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
