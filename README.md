# Interface

The code for the interface is contained in `interface/`. `gui.py` is the main file for the project, running it should be sufficient to run the program.

To rebuild any changes, run `python -m build` in the top level directory of this project. This will generate a file which can be installed by pip in `dist/`. Install it by running `pip install TimZGUI-1.1.0-py3-none-any.whl` or whatever the generated whl file's name is. Then the program can be run by `/path/to/Python3/Scripts/gui` or just `gui` if `path/to/Python3/Scripts` is in the `PATH` env variable.