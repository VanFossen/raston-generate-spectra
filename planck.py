import sys
from radis import sPlanck

# function presents error and usage to user, then quits
def __error(error_text):
  print(error_text) 
  print("  python3 planck.py <source> <min-wavelength (nm)> <max-wavelength (nm)>")
  quit()

# check number of args
if len(sys.argv) < 4:
  __error("  not enought command line arguments")

# create variables from args
source_temp = int(sys.argv[1])
min_wavelen = int(sys.argv[2])
max_wavelen = int(sys.argv[3])

# check if wavelengths are correct
if min_wavelen < 800:
  __error("  min wavelength is out of range (800 - 25000). provided min %s"%(min_wavelen))
elif max_wavelen > 25000:
  __error("  max wavelength is out of range (800 - 25000). provided max %s"%(max_wavelen))
elif min_wavelen > max_wavelen:
  __error("  min wavelength is greater than max wavelength. provided min: %s  provided max: %s"%(min_wavelen, max_wavelen))
elif min_wavelen == max_wavelen:
  __error("  min wavelength is equivalent to max wavelength. provided min: %s  provided max: %s"%(min_wavelen, max_wavelen))

# output verified params to console as self-check before sPlanck()
print("source_temp: %s   min_wavelen: %s   max_wavelen: %s"%(source_temp, min_wavelen, max_wavelen))

# https://radis.readthedocs.io/en/latest/source/radis.phys.blackbody.html#radis.phys.blackbody.sPlanck
s = sPlanck(wavelength_min=min_wavelen,  # minimum wavelength (nm - 800)
            wavelength_max=max_wavelen,  # maximum wavelength (nm - 25000)
            T=source_temp,               # blackbody temperature (K) - Globar (1700), Tungsten (3100)
            eps=1,                       # grey-body emissivity
            medium='air'
        )

# save
# https://radis.readthedocs.io/en/latest/spectrum/spectrum.html#label-spectrum-store
s.savetxt('planck-%s-%s.csv'%(min_wavelen, max_wavelen), "radiance_noslit")
