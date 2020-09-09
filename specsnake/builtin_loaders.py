import pandas as pd

from specsnake.langmuir_isotherm import LtIsotherm
from specsnake.sfg_spectrum import SfgSpectrum


# SFG
def sfg_extractor(file) -> pd.DataFrame:
    """A function extracting the measurement data from a SFG spectral file """
    col_names = ['wavenumbers', 'sfg', 'ir', 'vis']
    return pd.read_csv(file, sep="\t", usecols=[0, 1, 3, 4], names=col_names, encoding='utf8', engine='c')


def sfg_constructor(name, data, creation_time) -> SfgSpectrum:
    """Constructor function for the actual SFG object"""
    meta = {"name": name, "creation_time": creation_time}
    return SfgSpectrum(data['wavenumbers'], data['sfg'], data['ir'], data['vis'], meta)


# LT
def lt_extractor(file) -> pd.DataFrame:
    col_names = ["time", "area", "apm", "surface_pressure"]
    return pd.read_csv(file, comment="#", sep='\t', usecols=[1, 2, 3, 4], names=col_names, engine="c")


def lt_constructor(name, data, creation_time) -> LtIsotherm:
    return LtIsotherm(name, creation_time, data["time"], data["area"], data["apm"], data["surface_pressure"])

