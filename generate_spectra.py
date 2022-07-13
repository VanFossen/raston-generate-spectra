import sys, math
from radis import calc_spectrum

# function presents error and usage to user, then quits
def __error(error_text):
  print(error_text)
  print("  usage: python3 generate_spectra.py <source (t or g)> <min-wavenumber (cm^-1)>  <max-wavenumber (cm^-1)>")
  quit()

# convert wavenumber (cm^-1) to wavelength (nm) (10000000 / wavenumber)
def __convert_wavenum_wavelen(min_wavenum, max_wavenum):
  min_wavelen = math.floor(10000000 / max_wavenum)
  max_wavelen = math.ceil(10000000 / min_wavenum)
  return min_wavelen, max_wavelen

# check number of args
if len(sys.argv) < 4:
  __error("  not enought command line arguments")

# create variables from args
source = sys.argv[1]
min_wavenum = int(sys.argv[2])
max_wavenum = int(sys.argv[3])

# check if source is correct (t or g)
if (source != 't') and (source != 'g'):
  __error("  source needs to be <t> or <g>. provided source: %s"%(source))

# set source_temp based on source input
if source == 'g':
  source_temp = 1700
elif source == 't':
  source_temp = 3100
else:
  __error("  source needs to be <t> or <g>. provided source: %s"%(source))

# check if wavenumbers are correct
if min_wavenum < 400:
  __error("  min wavenumber is out of range (400 - 12500). provided min: %s"%(min_wavenum))
elif min_wavenum > 12500:
  __error("  max wavenumber is out of range (400 - 12500). provided max: %s"%(max_wavenum))
elif min_wavenum > max_wavenum:
  __error("  min wavenumber is greater than max wavenumber. provided min: %s  provided max: %s"%(min_wavenum, max_wavenum))
elif min_wavenum == max_wavenum:
  __error("  min wavenumber is equivalent to max wavenumber. provided min: %s  provided max: %s"%(min_wavenum, max_wavenum))

# convert wavenumbers to wavelengths (cm^-1 --> nm)
min_wavelen, max_wavelen = __convert_wavenum_wavelen(min_wavenum, max_wavenum)

# check if wavelengths are correct
if min_wavelen < 800:
  __error("  min wavelength is out of range (800 - 25000). provided min %s"%(min_wavelen))
elif max_wavelen > 25000:
  __error("  max wavelength is out of range (800 - 25000). provided max %s"%(max_wavelen))
elif min_wavelen > max_wavelen:
  __error("  min wavelength is greater than max wavelength. provided min: %s  provided max: %s"%(min_wavelen, max_wavelen))
elif min_wavelen == max_wavelen:
  __error("  min wavelength is equivalent to max wavelength. provided min: %s  provided max: %s"%(min_wavelen, max_wavelen))

# output verified params to console as self-check before calc_spectrum()
print("source: %s   source_temp: %s   min_wavelen: %s   max_wavelen: %s"%(source, source_temp, min_wavelen, max_wavelen))

# ----- a -----
# ideal transmittance 
# https://radis.readthedocs.io/en/latest/source/radis.lbl.calc.html#radis.lbl.calc.calc_spectrum
s = calc_spectrum(min_wavelen,   # wmin minimum wavelength (nm - 800)
                  max_wavelen,   # wmax maximum wavelength (nm - 250000)
                  wunit='nm',
                  molecule='CO',
                  isotope='1,2,3',
                  pressure=0.0001,   # Bar
                  Tgas=294.15,       # K
                  path_length=10,    # cm
                  wstep=0.5,         # cm^-1
                  verbose=False,     # hides HITRAN output
                  databank='hitran',
                  warnings={'AccuracyError':'ignore'},
                )

# save
# https://radis.readthedocs.io/en/latest/spectrum/spectrum.html#label-spectrum-store
s.savetxt('calc_spectrum-%s-%s.csv'%(min_wavelen, max_wavelen), 'transmittance_noslit', wunit='nm')

# ----- b -----

# ----- c -----

# ----- d -----
