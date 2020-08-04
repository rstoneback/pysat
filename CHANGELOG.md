# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [3.0.0] - 2020-07-03
- New Features
  - Added registry module for registering custom external instruments
  - Added Meta.mutable flag to control attribute mutability
  - custom.attach replaces custom.add
  - Unit tests are now pytest compatible
  - Added altitudes to test instruments
  - New flags added to instruments to streamline unit testing: `_test_download`, `_test_download_travis`, `_password_req`
  - Madrigal instruments migrated to pysatMadrigal
  - methods.nasa_cdaweb.list_files moved to methods.general
  - `strict_time_flag` now defaults to True
  - Use of start / stop notation in remote_file_list
  - Added variable rename method to Instrument object (#91)
- Deprecations
  - Removed ssnl
  - Removed utils.stats
  - Removed model_utils
  - Removed deprecated pandas.Panel
  - imports datetime from datetime, not pandas (deprecated)
  - import DataFrame and Series directly from pandas, not pysat
  - Removed coords.scale_units
  - Removed time.season_date_range
  - DeprecationWarning for strict_time_flag only triggered if sloppy data is found
  - Remove convenience methods imported from pandas
  - Changed the default `custom.attatch` input to allow keyword arguement use when additional function input is required
  - Removed python 2.7 syntax
  - Removed utils.coords.geodetic_to_geocentric
  - Removed utils.coords.geodetic_to_geocentric_horizontal
  - Removed utils.coords.spherical_to_cartesian
  - Removed utils.coords.global_to_local_cartesian
  - Removed utils.coords.local_horizontal_to_global_geo
- Documentation
  - Added info on how to register new instruments
  - Fixed description of tag and sat_id behaviour in testing instruments
  - Added a tutorial for developers of instrument libraries for pysat
- Bug Fix
  - Fixed custom instrument attribute persistence upon load
  - Improved string handling robustness when writing netCDF4 files in Python 3
- Maintenance
  - nose dependency removed from unit tests
  - Specify dtype for empty pandas.Series for forward compatibility
  - Remove wildcard imports, relative imports
  - Include flake8 check as part of testing suites
  - Improve unit testing coverage of instrument functions and instrument object
  - Updated path to rocsat data

  ## [2.2.1] - 2020-07-29
  - Documentation
     - Improved organization of documentation on ReadTheDocs
  - Bug Fix
     - Adopted .readthedocs.yml to restore online documentation on ReadTheDocs
     - Modified MANIFEST.in to include pysat_testing instruments
     - Rename default branch as `main`

  ## [2.2.0] - 2020-07-24
  - New Features
     - Decreased time to load COSMIC GPS data by about 50%
     - Added DE2 Langmuir Probe, NACS, RPA, and WATS instruments
     - Updated `test_files.py` to be pytest compatible
     - Added check to ensure non-pysat keywords supplied at instantiation
       are supported by underlying data set methods
     - Updates to instrument testing objects for consistency
     - Changed madrigal methods to use `madrigalWeb` as a module rather than
       calling it externally
     - Added warning when FillValue metadata could lead to unexpected results
       when writing a netCDF4 file
     - Use conda to manage Travis CI test environment
     - Update ICON instrument file structure
     - Added NaN filter for metadata when writing netCDF4 files
     - Test instruments now part of compiled package for development elsewhere
     - Reviewed and improved documentation
     - Custom instrument keywords and defaults are now always found in inst.kwargs
     - Added support for ~ and $ variables when setting pysat data dir
     - Added custom.attach to make transitions to v3.0 easier
  - Deprecation Warning
    - custom.add will be renamed custom.attach in pysat 3.0.0
    - Several functions in coords will be removed in pysat 3.0.0.  These functions will move to pysatMadrigal
      - geodetic_to_geocentric
      - geodetic_to_geocentric_horizontal
      - spherical_to_cartesian
      - global_to_local_cartesian
      - local_horizontal_to_global_geo
    - methods.nasa_cdaweb.list_files will move to methods.general.list_files in pysat 3.0.0.
  - Documentation
    - Fixed description of tag and sat_id behaviour in testing instruments
    - Added discussion of github install, develop branches, and reqs to docs
  - Bug Fix
    - `_files._attach_files` now checks for an empty file list before appending
    - Fixed boolean logic when checking for start and stop dates in `_instrument.download`
    - Fixed loading of COSMIC atmPrf files
    - Fixed feedback from COSMIC GPS when data not found on remote server
    - Fixed deprecation warning for pysat.utils.coords.scale_units
    - Fixed a bug when trying to combine empty f107 lists
    - Fixed a bug where `remote_file_list` would fail for some instruments.
    - Made import of methods more robust
    - Fixed `SettingWithCopyWarning` in `cnofs_ivm` cleaning routine
    - Fixed cosmic load method definition to include altitude_bin
    - Fixed pysat_testing method definition to include mangle_file_dates keyword
    - Added small time offsets (< 1s) to ensure COSMIC files and data have unique times
    - Updates to Travis CI environment
    - Removed `inplace` use in xarray `assign` function, which is no longer allowed
    - Removed old code and incorrect comments from F10.7 support
    - Updated use of numpy.linspace to be compatible with numpy 1.18.
    - Fixed output of orbit_info during print(inst)
    - Fixed a bug when requesting non-existent files from CDAWeb (#426)
    - Improved compatibility of parse_delimited_filenames (#439)
    - Fixed bug assigning dates to COSMIC files
    - Fixed bug limiting local time orbit breakdowns for instruments much slower
      than 1 Hz

## [2.1.0] - 2019-11-18
- New Features
   - Added new velocity format options to utils.coords.scale_units
   - Improved failure messages for utils.coords.scale_units
   - Added some tests for model_utils
   - Added option to to_netCDF that names variables in the written file
     based upon the strings in the Instrument.meta object
   - Improved compatibility with NASA ICON's file standards
   - Improved file downloading for Kp
   - Added keyword ignore_empty_files to pysat.Instrument and Files objects
     to filter out empty files from the stored file list
   - Added slice and list ability to meta
   - Converted all print statements to logging statements
   - Updated cleaning routines for C/NOFS IVM
   - Added S4 scintillation data to the cosmic-gps instrument
   - pysat no longer creates a default data directory. User must specify location.
   - User set custom attributes are transparently stored within Meta object and are
     available via both Instrument and Meta.
   - Improved robustness of required library specification across multiple
     platforms
- Code Restructure
  - Move `computational_form` to `ssnl`, old version is deprecated
  - Move `scale_units` to `utils._core`, old version is deprecated
  - Replace `season_date_range` with `create_date_range`, old version is deprecated
  - Added deprecation warnings to stat functions
  - Added deprecation warnings to `ssnl` and `model_utils`
  - Removed `pysat_sgp4` instrument
  - Added cleaning steps to the C/NOFS IVM ion fraction data
- Bug fix
   - Fixed implementation of utils routines in model_utils and jro_isr
   - Fixed error catching bug in model_utils
   - Updated Instrument.concat_data for consistency across pandas and xarray. Includes support for user provided keywords.
   - Fixed error introduced by upstream change in NOAA F10.7 file format
   - Fixed bugs in DEMETER file reading introduced by changes in codecs
   - Fixed issue with data access via Instrument object using time and name slicing and xarray. Added unit test.
   - Updated travis.yml to work under pysat organization
   - Added missing requirements (matplotlib, netCDF4)
   - Fixed a bug when trying to combine empty kp lists
   - Updated travis.yml to work with python 2.7.15 and beyond
   - Unit tests reload pysat_testing_xarray for xarray tests
   - Updated setup.py to not overwrite default `open` command from `codecs`
   - Updated Travis CI settings to allow forks to run tests on local travis accounts
   - Fixed keep method to be case insensitive
   - Fixed a bug with COSMIC GPS downloads
   - Fixed selection bugs in the DEMETER IAP, CNOFS IVM, and model_utils routines
   - Updated URL link in setup.py
- Documentation
  - Added info on how to cite the code and package.
  - Updated instrument docstring
  - Corrected pysat.Instrument examples using COSMIC

## [2.0.0] - 2019-07-11
 - New Features
   - `pysatData` directory created in user's home directory if no directory specified
   - Added preliminary support for `xarray` to the `instrument` object
   - Support for `today`, `tomorrow`, and `yesterday` as datetime objects
   - Added `model_utils`, featuring preliminary support for data-model comparison
   - Added support for 1d median in seasonal averages
   - Added routine to convert from kp to Ap
   - Added `pyglow` integration support for python 3.x
   - Added option to check that loaded data has a unique and monotonic time index. Will be enforced in a future version.
   - Refactored data access through the Instrument object and expanded testing.
   - Added .empty attribute to Instrument object, True when no data loaded.
   - Added .index access mechanism to Instrument object, providing consistent access to the pandas DatetimeIndex associated with loaded data.
   - Added mechanism to return a list of loaded variables, .variables.
   - Added Instrument method to concat input data with data already loaded into Instrument object.
   - Updated format of printed dates to day month name and year, 01 January 2001.
   - Added Instrument property .date, returns date of loaded data.
   - Added download_updated_files, Instrument method that downloads any remote data not currently on the local machine.
   - Added remote_date_range, an Instrument method that returns first and last date for remote data.
   - Download method now defaults to most recent data (near now).
   - Improves input handling for datetime parameters that are more precise than just year, month, and day, where appropriate
   - Added merging routines to allow combination of measured and forecasted Kp and F10.7 indexes into a single instrument object
   - Files class internally refactored to improve robustness.
   - Added feature to handle delimited filenames, in addition to fixed_width names.
   - Exposed methods to allow users to more easily benefit from features in Files. Used to support remote_file_lists and make data downloads more convenient.
   - Expanded testing with Files.
   - Updated keyword names to be more complete. 'sec' to 'second', etc.
   - Updated Files access mechanisms to remove deprecated calls and improve robustness.
 - Code restructure
   - Moved instrument templates and methods to subdirectories
   - Moved utils into multiple subdirectories to aid with organization
 - Instrument Updates
   - NASA CDAWeb download now uses https protocol rather than FTP
   - `_instrument.py` supports xarray
   - Support for listing files from remote server
   - COSMIC RO data unified into single instrument object
   - Added support for DEMETER IAP
   - Added support for DMSP IVM Level 2 data.  Uses OpenMadrigal.
   - Added routines to update DMSP ephemeris and drifts
   - Added warnings to instruments without download support
   - Added preliminary support for ICON FUV and MIGHTI
   - Added support for Jicamarca Radio Observatory ISR
   - Added support for F10.7 and more Kp forecast products
   - Added instrument templates for Madrigal, CDAWeb, and netcdf_pandas
   - Added support for TIMED SABER
   - Added support for UCAR TIEGCM
   - OMNI HRO instrument now uses CDAWeb methods
   - Switched download methods for CDAWeb and COSMIC data to use `requests`
   - Added Madrigal methods
   - Removed support for SuperDARN and SuperMAG downloads while server changes are sorted out
 - Updates to travis configuration
   - Tests run for python 2.7 and 3.7
   - Added display port to test plots
 - Updates to community docs
   - Added Issue templates
   - Added Pull Request Template
   - Added note for PR to be made to develop, not master
 - Style updates throughout
   - Consistent documentation for docstrings and instruments
   - Cleaned up commented code lines
   - PEP8 scrub
 - Documentation
   - Added FAQ section
   - Added "powered by pysat" logo
   - Updated supported instruments
 - Unit Test Updates
   - Dropped instrument templates from coverage
   - Added multiple output options for `pysat_testing` object to aid with constellation tests. Removed old constellation test objects.
   - Added test data for space weather indices to speed up testing
   - Cyclic data for test instruments now generated from single test method
   - test objects for xarray added
   - Added test for parsed delimited files
   - Removed ftp downloads from travis tests, still will run locally
 - Bug fixes
   - `pandas.ix` notation replaced with `pandas.loc` and `pandas.iloc` throughout
   - Fixed a bug that forced user into interactive mode in `ssnl.plot`
   - Bug fixes and cleanup in demo codes
   - Fix for orbit iteration when less than one orbit of data exists. Fix now covers multiple days with less than one orbit.
   - Fixed a bug in python 3.7 caused by change in behaviour of StopIteration (#207)
   - Update to use of `len` on xarray to handle new behaviour (#130)
   - Updated import of reload statements now that python 3.3 has reached end of life
   - Updated deprecated behaviour of `get_duplicates`, `.apply`, and `.to_csv` when using pandas
   - Fixed bug in assigning units to metadata (#162)
   - Fixed timing bug introduced by reading only the first date/data pair from each line in the 45-day file data blocks


## [1.2.0] - 2018-09-24
 - SuperMAG support added
 - Increased data access robustness when using integer indexing
 - Added template for supporting netCDF4 based instruments (pysat_netCDF4)
 - Added support for MSIS within the pysat satellite simulation (based on sgp4)
 - Added plotting routine to sgp4
 - Initial support for the upcoming NASA/INPE SPORT Ion Velocity Meter (IVM)
 - Fixed bug triggerd when invoking multi_file_day option in Instrument object

## [1.1.0] - 2018-07-05
 - Initial support for Constellation objects, which allows operations and analysis on mixed groups of Instrument objects. Developed by UT Dallas senior undergraduate computer science students (UTDesign 2018).
 - Bug fixes when iterating by file
 - Added pysat_sgp4, a Two Line Element based satellite orbit propagator that is coupled with ionosphere, thermosphere, and geomagnetic models. Supports projecting these quantities onto the relevant spacecraft frame to create signals suitable for satellite data simulation and testing. Routine uses pyglow, pysatMagVect, sgp4, and pyEphem.
 - Further along the road toward windows compatibility
 - Fixed orbit number reporting in orbits.current
 - Added support for Defense Meteorological Satellite Program (DMSP) Ion Velocity Meter (IVM) data. Downloads from the Madrigal database (https://openmadrigal.org)
 - Added support for both sat_id and tag variations within filenames in the NASA CDAWeb template
 - Updated docummentation covering requirements for adding new instruments to pysat

## [1.0.1] - 2018-05-06
 - Improved robustness of Meta object when working with high and low order data
 - Improved Meta test coverage
 - Added dayside reconnection calculation for OMNI-HRO data
 - Improved test behavior when instrument data could not be downloaded

## [1.0.0] - 2018-04-29
 - Improved consistency when handling higher order metadata
 - Improved translation of metadata within netCDF4 files to pysat standard
 - Added pysatCDF as package requirement
 - PEP8 upgrades throughout
 - Updated load_netCDF4 routine to support ICON EUV files natively
 - to_netCDF4 function updated to be consistent with load_netCDF4
 - Meta object upgraded to handle more attributes by default
 - Meta object has been upgraded to preserve case of variable and attribute names
 - Metadata access is case insensitive for ease of use
 - Changes to units_label or name_label are automatically applied to underlying metadata
 - Improved handling of custom units and name labels at Instrument level
 - Additional functions added to Meta object, attrs, keys, keys_nD, has_attr, routines that return preserved case
 - Additional unit tests for Meta added
 - Reduced resources required for unit tests
 - Improved windows compatibility
 - Added more unit tests for seasonal averages
 - Added more simulated data types to pysat_testing2D
 - Added initial support for ICON EUV
 - Added initial support for ICON IVM
 - Added support for version/revision numbers in filenames within Files class constructor from_os


## [0.6.0] - 2017-08-11
 - Many changes since the last note here.
 - Unit tests have been expanded significantly, bug fixes as appropriate.
 - Coverage is over 80%
 - There are new requirements on loading routines to support testing.
 - Instrument object prints out nice information to command line
 - Attributes in netCDF and similar files are transferred to the Instrument object as part of loading
 - Added attribute 'empty', True if there is no data
 - Orbit support significantly improved, multiple orbit types are supported
 - Added concat to Meta
 - Python 3 compatible
 - Corrected intersection of data_padding and multi_file_day
 - Added support for higher order MetaData objects, needed for DataFrame within DataFrames
 - Windows compatibility
 - Additional scientific instrument support


### Changed
 - Initial support for sat_id in Instrument
 - Files class will now remove duplicate file times rather than simply raise an exception

## [0.3.3] - 2016-01-07
### Changed
 - Added manual_org flag to Instrument instantion. Simple file management flag.
 - Improved COSMIC demo plotting
 - Improved support for instruments with no files

## [0.3.2] - 2015-12-01
### Changed
 - Fixed error raised by pysat.utils.set_data_dir
 - Partial unit test coverage for files class
 - File tracking more robust
 - Download methods now log off from server at the end of download
 - Improved to_netcdf3 and load_netcdf3 routines, netcdf files produced pass standards check

## [0.3.1] - 2015-07-21
### Changed
 - Added missing file close statement in SuperDARN load command
 - Fixed COSMIC UTS bug
 - Fixed check for unique datetimes associated with files
 - Improved instrument docstrings
 - Added step size (freq) keyword to bounds and download methods
 - Added C/NOFS IVM and COSMIC GPS demo
 - Added support for OMNI data, 1 and 5 min files, time shifted to magnetopause
 - Moving toward python 3 compatibility
 - PEP 8 improvements
 - fixed demo ssnl_occurence_by_orbit file, replaced binx with bin_x
 - Doubled loading performance for SuperDARN grdex files (3 seconds down to 1.5)

## [0.3] - 2015-06-18
### Changed
 - Improved polar orbit determination
 - Added file sorting in files.from_os constructor to ensure datetime index is correct
 - Added Instrument instantiation option, multi_file_day
  - good when data for day n is in a file labeled by day n-1, or n+1
 - Chaged binx to bin_x in return statements
 - Improved PEP-8 compatibility
 - Fixed bad path call in meta.from_csv
 - Added simple averaging by day/file/orbit instrument independent routines
 - Added instrument independent seasonal averaging routines
 - Improved loading performance for cosmic2013
 - made pysat import statements more specific
 - fixed bad import call on load_netcdf3
 - fixed tab/space issues
 - Improved performance of comsic 2013 data loading

## [0.2.2] - 2015-05-17
### Changed
 - Expanded coverage in tutorial documentation
 - Expanded test coverage for pysat.Meta()
 - Improved robustness of Meta __setitem__
 - Updated C/NOFS VEFI method to exempt empty file errors
 - Updated C/NOFS VEFI download method to remove empty files
 - Updated C/NOFS VEFI instrument module to use metadata from CDF file
 - Updated superdarn cleaning method to remove empty velocity frames
 - Updated Instrument download method to update bounds if bounds are default
 - Updated C/NOFS IVM download method to remove empty files
 - Updated C/NOFS IVM instrument module to use metadata from CDF file
 - Performance improvements to seasonal occurrence probability
 - Improved docstrings

## [0.2.1] - 2015-04-29
### Changed
- Removed spacepy and netCDF from setup.py requirements. Both of
  these packages require non-python code to function properly.
  pysat now builds correctly as determined by travis-cl.
  Installation instructions have been updated.

## [0.2.0] - 2015-04-27
### Changed
- Added information to docstrings.
- Expanded unit test coverage and associated bugs.
- Changed signature for pysat.Instrument, orbit information
  condensed into a single dictionary. pad changed from a boolean
  to accepting a pandas.DateOffest or dictionary.
- Changed doy parameter in create_datetime_index to day.
- Changed Instrument.query_files to update_files
- Improved performance of cnofs_ivm code
