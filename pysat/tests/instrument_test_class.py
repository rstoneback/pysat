"""
Standardized class and functions to test instruments for pysat libraries.  Not
directly called by pytest, but imported as part of test_instruments.py.  Can
be imported directly for external instrument libraries of pysat instruments.
"""
import datetime as dt
from importlib import import_module
import warnings

import pytest

import pysat


def initialize_test_inst_and_date(inst_dict):
    """Initializes the instrument object to test and date

    Paramters
    ---------
    inst_dict : dict
        Dictionary containing specific instrument info, generated by
        generate_instrument_list

    Returns
    -------
    test_inst : pysat.Instrument
        instrument object to be tested
    date : dt.datetime
        test date from module

    """

    test_inst = pysat.Instrument(inst_module=inst_dict['inst_module'],
                                 tag=inst_dict['tag'],
                                 inst_id=inst_dict['inst_id'],
                                 temporary_file_list=True,
                                 update_files=True)
    test_dates = inst_dict['inst_module']._test_dates
    date = test_dates[inst_dict['inst_id']][inst_dict['tag']]
    return test_inst, date


class InstTestClass():
    """Provides standardized tests for pysat instrument libraries.

    Note: Not diretly run by pytest, but inherited through test_instruments.py
    """
    module_attrs = ['platform', 'name', 'tags', 'inst_ids',
                    'load', 'list_files', 'download']
    inst_attrs = ['tag', 'inst_id', 'acknowledgements', 'references']
    inst_callable = ['load', 'list_files', 'download', 'clean', 'default']
    attr_types = {'platform': str, 'name': str, 'tags': dict,
                  'inst_ids': dict, 'tag': str, 'inst_id': str,
                  'acknowledgements': str, 'references': str}

    def assert_hasattr(self, obj, attr_name):
        """ Nice assertion statement for `assert hasattr(obj, attr_name)`
        """
        estr = "Object {:} missing attribute {:}".format(obj.__repr__(),
                                                         attr_name)
        assert hasattr(obj, attr_name), estr

    def assert_isinstance(self, obj, obj_type):
        """ Nice assertion statement for `assert isinstance(obj, obj_type)`
        """
        estr = "Object {:} is type {:}, but should be type {:}".format(
            obj.__repr__(), type(obj), obj_type)
        assert isinstance(obj, obj_type), estr

    @pytest.mark.all_inst
    def test_modules_standard(self, inst_name):
        """Checks that modules are importable and have standard properties.
        """
        # ensure that each module is at minimum importable
        module = import_module(''.join(('.', inst_name)),
                               package=self.inst_loc.__name__)
        # Check for presence of basic instrument module attributes
        for mattr in self.module_attrs:
            self.assert_hasattr(module, mattr)
            if mattr in self.attr_types.keys():
                self.assert_isinstance(getattr(module, mattr),
                                       self.attr_types[mattr])

        # Check for presence of required instrument attributes
        for inst_id in module.inst_ids.keys():
            for tag in module.inst_ids[inst_id]:
                inst = pysat.Instrument(inst_module=module, tag=tag,
                                        inst_id=inst_id)

                # Test to see that the class parameters were passed in
                self.assert_isinstance(inst, pysat.Instrument)
                assert inst.platform == module.platform
                assert inst.name == module.name
                assert inst.inst_id == inst_id
                assert inst.tag == tag

                # Test the required class attributes
                for iattr in self.inst_attrs:
                    self.assert_hasattr(inst, iattr)
                    self.assert_isinstance(getattr(inst, iattr),
                                           self.attr_types[iattr])

    @pytest.mark.all_inst
    def test_standard_function_presence(self, inst_name):
        """Check if each function is callable and all required functions exist
        """
        module = import_module(''.join(('.', inst_name)),
                               package=self.inst_loc.__name__)

        # Test for presence of all standard module functions
        for mcall in self.inst_callable:
            if hasattr(module, mcall):
                # If present, must be a callable function
                assert callable(getattr(module, mcall))
            else:
                # If absent, must not be a required function
                assert mcall not in self.module_attrs

    @pytest.mark.all_inst
    def test_instrument_test_dates(self, inst_name):
        """Check that module has structured test dates correctly."""
        module = import_module(''.join(('.', inst_name)),
                               package=self.inst_loc.__name__)
        info = module._test_dates
        for inst_id in info.keys():
            for tag in info[inst_id].keys():
                self.assert_isinstance(info[inst_id][tag], dt.datetime)

    @pytest.mark.first
    @pytest.mark.download
    def test_download(self, inst_dict):
        """Check that instruments are downloadable."""

        test_inst, date = initialize_test_inst_and_date(inst_dict)

        # check for username
        dl_dict = inst_dict['user_info'] if 'user_info' in \
            inst_dict.keys() else {}
        test_inst.download(date, date, **dl_dict)
        assert len(test_inst.files.files) > 0

    @pytest.mark.second
    @pytest.mark.download
    @pytest.mark.parametrize("clean_level", ['none', 'dirty', 'dusty', 'clean'])
    def test_load(self, clean_level, inst_dict):
        """Check that instruments load at each cleaning level."""

        test_inst, date = initialize_test_inst_and_date(inst_dict)
        if len(test_inst.files.files) > 0:
            # Set Clean Level
            test_inst.clean_level = clean_level
            target = 'Fake Data to be cleared'
            test_inst.data = [target]
            try:
                test_inst.load(date=date)
            except ValueError as verr:
                # Check if instrument is failing due to strict time flag
                if str(verr).find('Loaded data') > 0:
                    test_inst.strict_time_flag = False
                    with warnings.catch_warnings(record=True) as war:
                        test_inst.load(date=date)
                    assert len(war) >= 1
                    categories = [war[j].category for j in range(0, len(war))]
                    assert UserWarning in categories
                else:
                    # If error message does not match, raise error anyway
                    raise(verr)

            # Make sure fake data is cleared
            assert target not in test_inst.data
            # If cleaning not used, something should be in the file
            # Not used for clean levels since cleaning may remove all data
            if clean_level == "none":
                assert not test_inst.empty
        else:
            pytest.skip("Download data not available")

    @pytest.mark.download
    def test_remote_file_list(self, inst_dict):
        """Check if optional list_remote_files routine exists and is callable.
        """
        test_inst, date = initialize_test_inst_and_date(inst_dict)
        name = '_'.join((test_inst.platform, test_inst.name))

        if hasattr(getattr(self.inst_loc, name), 'list_remote_files'):
            assert callable(test_inst.remote_file_list)
            # check for username
            dl_dict = inst_dict['user_info'] if 'user_info' in \
                inst_dict.keys() else {}
            files = test_inst.remote_file_list(start=date, stop=date, **dl_dict)
            # If test date is correctly chosen, files should exist
            assert len(files) > 0
        else:
            pytest.skip("remote_file_list not available")

    @pytest.mark.no_download
    def test_download_warning(self, inst_dict):
        """Check that instruments without download support have a warning."""
        test_inst, date = initialize_test_inst_and_date(inst_dict)

        with warnings.catch_warnings(record=True) as war:
            test_inst.download(date, date)

        assert len(war) >= 1
        categories = [war[j].category for j in range(0, len(war))]
        assert UserWarning in categories
