# PyInspireStat

## pyinspirestat.py

The script is largely based on `pyinspire.py` by Ian Huston (https://bitbucket.org/ihuston/pyinspire). The script can be used to get time series from the `inSpire` database (http://inspirehep.net/) assuming a given `query`. The script, by default, returns the number of papers that satisfy the `query` as function of the time. The maximum number of papers in a given year is `max_number_results`.

The code is optimized to return the number of papers in a given year, however it can be easily modified to obtain more sophisticated information.
