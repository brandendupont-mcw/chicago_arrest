# Assign Offense Categories to Chicago Arrest Data

A postprocess script in Github's Flat Data actions is used to fire a Python script that collects arrest data from the Chicago's Open Data Portal.

## Execution :

- the Flat Data action is scheduled weekly.

- the `postprocess.ts` script is then run, triggers the install of python packages, and runs the main python script `postprocess.py`.

- `postprocess.py` prints out its received arguments, and then generates a CSV file `chicago_arrests.csv`. 



## Thanks

- Thanks to the Github Octo Team
- Thanks to [Pierre-Olivier Simonard](https://github.com/pierrotsmnrd/flat_data_py_example) for his repo on implementing Flat data as a Python postprocess file.

