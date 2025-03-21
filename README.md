# winterdarktempcorr
To implement a thermal correction for dark images for the WINTER telescope




In this repository is the code I have been working on. The two csv files are darks from the whole history of WINTER (WINTER_temp_data.csv) with data pulled out about temperature and median counts calculates, and darks from the whole night of 3/19 (WINTER_temp_correction_data.csv). The scripts used to create these files are temps.py and the first block of the night_of_darks_analysis.ipynb notebook. The notebooks also have a bunch of plots. At the bottom of scrath.ipynb I had started fitting coeffs for the temperature curves using the median, but this actually must be done pixel-wise. My plan was to pick a few (10-50) representaive darks along each temperature curve and fit a temperature curve for each pixel which would then be used to apply a correction to each image. If someone else wants to try this today they should feel free but I can also work on it next week. 
