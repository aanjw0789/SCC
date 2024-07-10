----------------------------------
# Seagrass Carbon Calculator (SCC)
----------------------------------

_The graphical user interface (GUI) and all codes are developed by A. J. Wahyudi with contributions and input from IMBeR Group members and OpenAI ChatGPT 3.5_
_The last update: 10 July 2024_

PLEASE read the [CC-BY-4.0 license](https://github.com/aanjw0789/SCC/?tab=CC-BY-4.0-1-ov-file) of this app code.

The SCC app is developed based on the following source: 

Wahyudi, A. J., Rahmawati, S., Irawan, A., Hadiyanto, H., Prayudha, B., Hafizt, M., Afdal, A., Adi, N. S., Rustam, A., Hernawan, U. E., Rahayu, Y. P., Iswari, M. Y., Supriyadi, I. H., Solihudin, T., Ati, R. N. A., Kepel, T. L., Kusumaningtyas, M. A., Daulat, A., Salim, H. L., … Kiswara, W. (2020). Assessing Carbon Stock and Sequestration of the Tropical Seagrass Meadows in Indonesia. Ocean Science Journal, 55(1), 85–97. https://doi.org/10.1007/s12601-020-0003-0

----------------------------------
## Installation Guide
----------------------------------
Run the Seagrass Carbon Calculator (SCC) Application Locally
1. Clone the GitHub Repository:
   ```sh
   git clone https://github.com/aanjw0789/SCC.git
   cd SCC
   ```
   or manually download and save `app.py` `requirements.txt` and the `templates` folder in your project directory.
3. Ensure you have Python 3 installed on your machine. You can download it from python.org.
4. Open a terminal or command prompt, navigate to your project directory, and create a virtual environment:
   ```sh
   python3 -m venv venv

5. Activate the virtual environment:

   a. On MacOS and Linux:
   ```sh
   source venv/bin/activate
   ```
   b. On Windows:
   ```sh
   venv\Scripts\activate
   ```
6. Install the dependencies using the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```
7. Run the SCC flask application:
   ```sh
   python3 app.py
   ```
8. Your SCC app will start locally, and you can access it in your web browser at `http://127.0.0.1:5000`
9. You can start calculating the seagrass carbon stock and carbon sequestration/assimilation based on the value of biomass, density, and/or coverage percentage of seagrass


Note:

You may use one or a combination of biomass, density, and/or coverage percentages based on the available data you have. Put zero (0) if there is no data.

You will get the results:

  * ABG = above-ground carbon stock in gC/m2
  * BGC = below-ground carbon stock in gC/m2
  * TC = total carbon stock in gC/m2; it does not always ABG+BGC, but a direct calculation based on the model from the source: Wahyudi et al., (2020)
  * CS = carbon sequestration or assimilation rate, i.e., carbon dioxide that assimilated to the biomass in tC/ha/yr
  * TC-conversion = total carbon stock in tC/ha

---------------------------------
## Alternative
---------------------------------
You can use `SCC-GUI-Python-code-standalone.ipynb` and run it directly on platforms like Jupyter Notebook or Google Colab.

---------------------------------
## Batch Calculation
---------------------------------
You can use `batch calculation-SCC.ipynb` for large data calculations (i.e., Excel file dataset). Run the Python code directly on platforms like Jupyter Notebook or Google Colab. Example of dataset format may refer to `batch file test.xlsx`
