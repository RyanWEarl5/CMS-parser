# CMS-parser
Tool to request and parse data from the Centers for Medicare and Medicaid API for Hospital &amp; Non-Hospital Facilities data between 2010 and 2021

## Process ##

API Documentation can be found here: https://data.cms.gov/

In the current version of the main.py file all quarters are selected for the Hospital & Non-Hospital Facilities datasets,
to only run the script for certain versions of the tool simply remove/add fields in the quarter_dict dictionary.

All quarters will be output as seperate CSV files
