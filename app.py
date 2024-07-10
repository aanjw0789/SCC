from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Function to calculate values
def calculate_values(biomass, density, coverage):
    # Perform calculations based on your formula
    abg_result = np.where(
        (biomass == 0) & (density == 0) & (coverage == 0), 0,
        np.where((biomass > 0) & (density == 0) & (coverage == 0), 12.63086 + 0.061001 * biomass,
        np.where((biomass > 0) & (density == 0) & (coverage > 0), 14.26965 + 0.062445 * biomass - 0.044118 * coverage,
        np.where((biomass > 0) & (density > 0) & (coverage == 0), 12.63086 + 0.061001 * biomass,
        np.where((biomass == 0) & (density == 0) & (coverage > 0), 21.33781 + 0.13514 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage > 0), 21.33781 + 0.13514 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage == 0), 29.609031 - 0.001435 * density,
        14.26965 + 0.062445 * biomass - 0.044118 * coverage)))))))

    bgc_result = np.where(
        (biomass == 0) & (density == 0) & (coverage == 0), 0,
        np.where((biomass > 0) & (density == 0) & (coverage == 0), 6.00388 + 0.214211 * biomass,
        np.where((biomass > 0) & (density == 0) & (coverage > 0), -4.365552 + 0.21622 * biomass + 0.218579 * coverage,
        np.where((biomass > 0) & (density > 0) & (coverage == 0), 0.451447 + 0.216752 * biomass + 0.006902 * density,
        np.where((biomass == 0) & (density == 0) & (coverage > 0), 53.2301 + 0.3055 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage > 0), 53.2301 + 0.3055 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage == 0), 65.28627 + 0.00201 * density,
        -3.942647 + 0.21748 * biomass + 0.006119 * density + 0.108165 * coverage)))))))

    tc_result = np.where(
        (biomass == 0) & (density == 0) & (coverage == 0), 0,
        np.where((biomass > 0) & (density == 0) & (coverage == 0), 10.232724 + 0.297451 * biomass,
        np.where((biomass > 0) & (density == 0) & (coverage > 0), 6.862504 + 0.295653 * biomass + 0.080054 * coverage,
        np.where((biomass > 0) & (density > 0) & (coverage == 0), 7.426061 + 0.298152 * biomass + 0.003718 * density,
        np.where((biomass == 0) & (density == 0) & (coverage > 0), 78.7965 + 0.4117 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage > 0), 78.7965 + 0.4117 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage == 0), 96.56068 + 0.001082 * density,
        6.874866 + 0.297085 * biomass + 0.003865 * density + 0.010671 * coverage)))))))

    cs_result = np.where(
        (biomass == 0) & (density == 0) & (coverage == 0), 0,
        np.where((biomass > 0) & (density == 0) & (coverage == 0), 6.813338 + 0.001579 * biomass,
        np.where((biomass > 0) & (density == 0) & (coverage > 0), 1.74315 + 0.08654 * coverage,
        np.where((biomass > 0) & (density > 0) & (coverage == 0), 6.813338 + 0.001579 * biomass,
        np.where((biomass == 0) & (density == 0) & (coverage > 0), 1.74315 + 0.08654 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage > 0), 1.74315 + 0.08654 * coverage,
        np.where((biomass == 0) & (density > 0) & (coverage == 0), 6.659196 + 0.002178 * density,
        1.74315 + 0.08654 * coverage)))))))

    tc_conv_result = tc_result / 100

    return abg_result, bgc_result, tc_result, cs_result, tc_conv_result

# Route to render the index.html template
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        biomass = float(request.form['biomass'])
        density = float(request.form['density'])
        coverage = float(request.form['coverage'])

        abg_result, bgc_result, tc_result, cs_result, tc_conv_result = calculate_values(biomass, density, coverage)

        return render_template('result.html', 
                               abg=abg_result, 
                               bgc=bgc_result, 
                               tc=tc_result, 
                               cs=cs_result, 
                               tc_conv=tc_conv_result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
