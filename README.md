# SCC
## Seagrass Carbon Calculator
==================================
The app is developed by A. J. Wahyudi

PLEASE read the [CC-BY-4.0 license](https://github.com/aanjw0789/SCC/?tab=CC-BY-4.0-1-ov-file) of this app code.

The SCC app is developed based on the following source: 

Wahyudi, A. J., Rahmawati, S., Irawan, A., Hadiyanto, H., Prayudha, B., Hafizt, M., Afdal, A., Adi, N. S., Rustam, A., Hernawan, U. E., Rahayu, Y. P., Iswari, M. Y., Supriyadi, I. H., Solihudin, T., Ati, R. N. A., Kepel, T. L., Kusumaningtyas, M. A., Daulat, A., Salim, H. L., … Kiswara, W. (2020). Assessing Carbon Stock and Sequestration of the Tropical Seagrass Meadows in Indonesia. Ocean Science Journal, 55(1), 85–97. https://doi.org/10.1007/s12601-020-0003-0

----------------------------------
## Installation Guide
----------------------------------
Run the Seagrass Carbon Calculator (SCC) Application Locally
1. Install [Python 3](https://gist.github.com/MichaelCurrin/57caae30bd7b0991098e9804a9494c23) and the main dependencies: 'numpy' and 'pandas'
3. Save 'app.py' file and the 'templates' folder in your project directory.
4. Open a terminal or command prompt, navigate to your project directory, and install 'Flask' e.g., using the following code: "!pip install flask"
5. Run the Flask application using the following command:
   "python app.py"
6. Your SCC app will start locally, and you can access it in your web browser at http://127.0.0.1:5000
7. You can start calculating the seagrass carbon stock and carbon sequestration/assimilation based on the value of biomass, density, and/or coverage percentage of seagrass

Note:
You may use one or a combination of biomass, density, and/or coverage percentages based on the available data you have. Put zero (0) if there is no data.
ABG = above-ground carbon stock in gC/m2
BGC = below-ground carbon stock in gC/m2
TC = total carbon stock in gC/m2; it does not always ABG+BGC, but a direct calculation based on model from the source (Wahyudi et al., 2020)
CS = carbon sequestration or assimilation rate, i.e., carbon dioxide that assimilated to the biomass in tC/ha/yr
TC-conversion = total carbon stock in tC/ha
