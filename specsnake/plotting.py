import os
import pathlib
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from .base_spectrum import BaseSpectrum

# todo add support for plot file

class Plotter:

    # todo: custom title, label

    def __init__(self, specs: List[BaseSpectrum], title="default"):
        self.specs = specs
        self.title = title

    def plot(self, show_label=True):
        for s in self.specs:
            label = s.name if show_label else None
            plt.plot(s.x, s.y, label=label)
        plt.xlabel(self.specs[0].x_unit)
        plt.ylabel(self.specs[0].y_unit)
        plt.legend()

    def show(self):
        self.plot()
        plt.show()

    def save(self):
        self.plot()
        plt.savefig(f'{self.title}.png')