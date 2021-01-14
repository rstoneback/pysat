#!/usr/bin/env python
# Full license can be found in License.md
# Full author list can be found in .zenodo.json file
# DOI:10.5281/zenodo.1199703
# ----------------------------------------------------------------------------
""" Created as part of a Spring 2018 UTDesign project.
"""

import importlib


class Constellation(object):
    """Manage and analyze data from multiple pysat Instruments.

    Parameters
    ----------
    constellation_module : string
        Name of a pysat constellation module
    instruments : list-like
        A list of pysat Instruments to include in the Constellation

    Attributes
    ----------
    instruments : list
        A list of pysat Instruments that make up the Constellation
    bounds : (datetime/filename/None, datetime/filename/None)
        bounds for loading data, supply array_like for a season with gaps.
        Users may provide as a tuple or tuple of lists, but the attribute is
        stored as a tuple of lists for consistency

    """

    # -----------------------------------------------------------------------
    # Define the magic methods

    def __init__(self, constellation_module=None, instruments=None):
        """
        Constructs a Constellation given a list of instruments or the name of
        a file with a pre-defined constellation.

        Parameters
        ----------
        constellation_module : string
            Name of a pysat constellation module
        instruments : list-like

        Note
        ----
        Omit `instruments` and `name` to create an empty constellation.

        """

        # Load Instruments from the constellation module, if it exists
        if constellation_module is not None:
            const = importlib.import_module(constellation_module)
            self.instruments = const.instruments
        else:
            self.instruments = []
        
        if instruments is not None:
            if hasattr(instruments, '__getitem__'):
                raise ValueError('instruments must be iterable')

            self.instruments.extend(list(instruments))

        return

    def __getitem__(self, *args, **kwargs):
        """
        Look up a member Instrument by index.

        """

        return self.instruments.__getitem__(*args, **kwargs)

    def __repr__(self):
        """ Print the basic Constellation properties

        """

        out_str = "Constellation(instruments={:}) -> {:d} Instruments".format(
            self.instruments, len(self.instruments))
        return out_str

    def __str__(self):
        """ Print names of instruments within constellation

        """

        output_str = 'pysat Constellation object:\n'
        output_str += '---------------------------\n'

        ninst = len(self.instruments)

        if ninst > 0:
            output_str += "\nIndex Platform Name Tag Inst_ID\n"
            output_str += "-------------------------------\n"
            for i, inst in enumerate(self.instruments):
                output_str += "{:d} '{:s}' '{:s}' '{:s}' '{:s}'\n".format(
                    i, inst.platform, inst.name, inst.tag, inst.inst_id)
        else:
            output_str += "No loaded Instruments\n"

        return output_str

    # -----------------------------------------------------------------------
    # Define the public methods and properties

    @property
    def bounds(self):
        return self.instruments[0].bounds

    @bounds.setter
    def bounds(self, value=None):
        """ Sets boundaries for all Instruments in Constellation

        Parameters
        ----------
        value : tuple or NoneType
            Tuple containing starting time and ending time for Instrument
            bounds attribute or None (default=None)

        """

        for instrument in self.instruments:
            instrument.bounds = value

        return

    def custom_attach(self, *args, **kwargs):
        """Register a function to modify data of member Instruments.

        Parameters
        ----------
        *args : list reference
            References a list of input arguments
        **kwargs : dict reference
            References a dict of input keyword arguments

        Note
        ----
        Wraps Instrument.custom_attach; see Instrument.custom_attach for more
        information.

        """

        for instrument in self.instruments:
            instrument.custom_attach(*args, **kwargs)

        return

    def load(self, *args, **kwargs):
        """ Load instrument data into Instrument object.data

        Parameters
        ----------
        *args : list reference
            References a list of input arguments
        **kwargs : dict reference
            References a dict of input keyword arguments

        Note
        ----
        Wraps pysat.Instrument.load; see Instrument.load for more information.

        """

        for instrument in self.instruments:
            instrument.load(*args, **kwargs)

        return
