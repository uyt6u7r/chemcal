from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Ensuring both GET and POST methods are allowed
def chemical_calculator():
    if request.method == 'POST':
        try:
            concentration = float(request.form['concentration'])  # Desired concentration in mol/L
            molar_mass = float(request.form['molar_mass'])  # Molar mass in g/mol
            volume = float(request.form['volume'])  # Desired volume in liters
            required_mass = concentration * molar_mass * volume  # mass = c * M * V

            advice = ""
            if required_mass < 0.01:  # Adjust this threshold as necessary
                stock_concentration = 1.0  # Assume stock solution concentration in mol/L
                stock_volume_needed = required_mass / (stock_concentration * molar_mass)
                stock_volume_needed_ml = stock_volume_needed * 1000  # Convert liters to milliliters

                advice = f"For precise measurement, dilute {stock_volume_needed_ml:.2f} mL of a 1 M stock solution into {volume * 1000:.0f} mL total volume."
            else:
                advice = "Weigh out the required mass directly."

            return render_template('result.html', required_mass=required_mass, advice=advice)
        except ValueError:
            return "Invalid input. Please enter valid numbers."
    else:
        return render_template('index.html')  # Make sure to handle GET requests by showing the form

if __name__ == '__main__':
    app.run(debug=True)
