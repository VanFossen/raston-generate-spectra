from radis import calc_spectrum, sPlanck

# Radis Lab Online
# https://radis.github.io/radis-lab/

# ideal transmittance (in wavenumbers (cm^-1))
s = calc_spectrum(400,           # wmin (minimum wavenumber (cm^-1))
                  12500,         # wmax (maximum wavenumber (cm^-1))
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
s.apply_slit(0.5, 'nm')
s.plot("transmittance_noslit")

# ideal transmittance (in wavelengths (nm))
s = calc_spectrum(800,           # wmin (minimum wavelength (nm))
                  25000,         # wmax (maximum wavelength (nm))
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
s.apply_slit(0.5, 'nm')
s.plot("transmittance_noslit")

# blackbody spectrum for Globar (in wavenumbers (cm^-1))
s = sPlanck(wavenum_min=400,
            wavenum_max=12500,
            T=1700,            # blackbody temperature (K)
            eps=1,             # grey-body emissivity
            medium='air')
s.plot()

# blackbody spectrum for Tungsten (in wavenumbers (cm^-1))
s = sPlanck(wavenum_min=400,
            wavenum_max=12500,
            T=3100,            # blackbody temperature (K)
            eps=1,             # grey-body emissivity
            medium='air'
        )
s.plot()

# blackbody spectrum for Globar (in wavelengths (nm))
s = sPlanck(wavelength_min=800,
            wavelength_max=25000,
            T=1700,            # blackbody temperature (K)
            eps=1,             # grey-body emissivity
            medium='air')
s.plot()

# blackbody spectrum for Tungsten (in wavelengths (nm))
s = sPlanck(wavelength_min=800,
            wavelength_max=25000,
            T=3100,            # blackbody temperature (K)
            eps=1,             # grey-body emissivity
            medium='air'
        )
s.plot()
