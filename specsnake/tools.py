import datetime
import os
from functools import partial
from pathlib import Path

import pandas as pd
import numpy as np

from specsnake.base_spectrum import BaseSpectrum
from specsnake.sfg_spectrum import SfgSpectrum


# todo: generic import function which can be configured from a scheme
# todo: generic import funcion must take another function (loader) as argument

def to_spectrum(file, extractor, constructor) -> BaseSpectrum:
    """Generic extraction function to convert a given input file into a base spectrum. The parameter extractor is a
    function that is called on the file to extract the data, the constructor a function that returns the actual
    spectrum object"""
    data = extractor(file)
    creation_time = datetime.datetime.fromtimestamp(os.path.getmtime(str(file)))
    meta = {"name": Path(file).stem, "measured_time": creation_time}
    return constructor(data, meta)


def sfg_extractor(file) -> pd.DataFrame:
    """A function extracting the measurement data from a SFG spectral file """
    col_names = ['wavenumbers', 'sfg', 'ir', 'vis']
    return pd.read_csv(file, sep="\t", usecols=[0, 1, 3, 4], names=col_names, encoding='utf8', engine='c')


def sfg_constructor(data, meta) -> SfgSpectrum:
    """Constructor function for the actual SFG object"""
    return SfgSpectrum(data['wavenumbers'], data['sfg'], data['ir'], data['vis'], meta)


def load_sfg():
    return partial(to_spectrum, extractor=sfg_extractor, constructor=sfg_constructor)
