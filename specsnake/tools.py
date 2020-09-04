import datetime
import os

import pandas as pd
import numpy as np

from specsnake.sfg_spectrum import SfgSpectrum


def nparray_to_str(array):
    return ",".join(array.values.astype(str))


def extract_sfg_file(file) -> pd.DataFrame:
    """A function extracting the measurement data from a SFG spectral file """
    col_names = ['wavenumbers', 'sfg', 'ir', 'vis']
    return pd.read_csv(file, sep="\t", usecols=[0, 1, 3, 4], names=col_names, encoding='utf8', engine='c')

# todo: generic import function which can be configured from a scheme


def to_sfg(file) -> SfgSpectrum:
    """Load the input file and return it as an SfgSpectrum object."""
    df = extract_sfg_file(file)
    creation_time = datetime.datetime.fromtimestamp(os.path.getmtime(str(file)))
    dic = {"name": file.split(".sfg")[0], "measured_time": creation_time}
    return SfgSpectrum(df['wavenumbers'], df['intensity'], df['ir_intensity'], df['vis_intesity'], dic)