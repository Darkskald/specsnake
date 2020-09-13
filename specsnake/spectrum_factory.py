from __future__ import annotations

import os
import datetime
from pathlib import Path

from .builtin_loaders import sfg_extractor, sfg_constructor, lt_extractor, lt_constructor
from .exceptions import SpectrumTypeNotAvailableError


class SpectrumFactoryProvider:
    """A class to generate SpectrumFactories. This is the generic way to introduce new types of spectra to
    the logic of this package. All builtin type of spectra are available at runtime due to an instance of this class
    and to add new types, the underlying config dictionary may be updated."""

    global_factory_config = {
        "sfg": {"extractor": sfg_extractor, "constructor": sfg_constructor},
        "lt": {"extractor": lt_extractor, "constructor": lt_constructor}
    }

    def provide_factory_by_name(self, name: str) -> CustomSpectrumFactory:
        try:
            return CustomSpectrumFactory(**self.global_factory_config[name])
        except KeyError:
            raise SpectrumTypeNotAvailableError(
                "The spectrum type you requested is not available in the current config!")

    def add_new_template(self, name, extractor, constructor, name_transformer=None):
        """Add a new template for SpectrumFactories to the configuration. This requires the name of the template,
        an extractor method, a constructor method and an optional name_transformer method."""
        self.global_factory_config[name] = {'extractor': extractor, 'constructor': constructor, 'name_transformer': name_transformer}


class CustomSpectrumFactory:
    # todo: add signatures for the callable parameters here
    def __init__(self, extractor, constructor, name_transformer=None):
        """Configure the factory to create spectrum objects from raw measurement data. The extractor is a function that extracts
        the data from the file, the constructor is responsible for the instantiation of the spectrum objects and the
        optional name transformer processes the file name to a representation suitable to appear in a plot legend."""
        self.extractor = extractor
        self.constructor = constructor
        self.name_transformer = name_transformer

    def build_from_file(self, file: Path):
        """The function that transforms the filepath to the spectrum object"""
        creation_time = datetime.datetime.fromtimestamp(os.path.getmtime(str(file)))
        data = self.extractor(file)

        if not self.name_transformer:
            name = file.stem
        else:
            name = self.name_transformer(file)

        return self.constructor(name, data, creation_time)

    def build_batch(self, directory: Path, file_ending='*'):
        """A convenience function to apply the builder to all spectra within the directoy and return a list of spectra.
        Can receive a pattern for the file ending to avoid the wrong files being imported."""
        return [self.build_from_file(p) for p in directory.rglob(file_ending)]
