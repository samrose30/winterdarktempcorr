import glob
import numpy as np
from astropy.io import fits
import pandas as pd


all_night_dir = '/data/loki/raw_data/winter/'
sam_dir = '/data/srose/'
nights = glob.glob(all_night_dir + '2025*')

t_data = []
i=0
for night in nights:
    print(night)
    i=i+1
    raw_files = glob.glob(night+'/raw/*.fits')
    for file in raw_files:
        hdul = fits.open(file)
        hdr0 = hdul[0].header
        for board in range(1,len(hdul)):
            img_type = hdr0['OBSTYPE']
            time_taken = hdr0['OBSMJD']
            tempture = hdr0['TEMPTURE'] #Outside air temperature (C)
            tempm1 = hdr0['TEMPM1'] # telescope temp M1, C
            tempm2 = hdr0['TEMPM2'] # telescope temp M2, C
            tempm3 = hdr0['TEMPM3'] # telescope temp M3, C 
            tempamb = hdr0['TEMPAMB'] # telescope temp ambient, C
            tobstar = hdr0['TOBSTAR'] #  Optics Box Temp - Starboard (C)
            tobport = hdr0['TOBPORT'] # Optics Box Temp - Port (C)
            tempFPA = hdul[board].header['T_FPA'] # FPA Temp (C)
            tempROIC = hdul[board].header['T_ROIC'] # ROIC Temp (C)
            boardid = hdul[board].header['BOARD_ID'] #sensor id
            exptime = hdr0['EXPTIME'] #exposure time in seconds
            nightid = i

            if img_type == 'DARK':
                img_data = hdul[board].data
                median_counts = np.median(img_data)

            else:
                median_counts = np.NaN

            t_data.append((img_type, time_taken, tempture, tempm1, tempm2, tempm3, tempamb, tobstar, tobport,
                      tempFPA, tempROIC, boardid, median_counts, exptime, nightid))
temp_frame = pd.DataFrame(t_data, columns=['img_type', 'UTC', 'air_temp', 'M1', 'M2', 'M3', 'AMB', 'OBStar',
                                              'OBPort', 'FPA', 'ROIC','boardid', 'med_counts', 'exptime', 'nightid'])
            
temp_frame.to_csv(sam_dir + 'WINTER_temp_data.csv', index=False)