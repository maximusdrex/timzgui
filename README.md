# Interface

The code for the interface is contained in `interface/`. `gui.py` is the main file for the project, running it should be sufficient to run the program.

To rebuild any changes, run `python -m build` in the top level directory of this project. This will generate a file which can be installed by pip in `dist/`. Install it by running `pip install TimZGUI-1.1.0-py3-none-any.whl` or whatever the generated whl file's name is. Then the program can be run by `/path/to/Python3/Scripts/gui` or just `gui` if `path/to/Python3/Scripts` is in the `PATH` env variable.

# Config

When the program is run, it will look for a file in the directory it is ran named `gui.cfg`, in order for it to run this file must include the host, username, and password, necessary to access your MySQL database. The file should look like this:

    [GUI]
    Help: This is an example help text

    [Database]
    User: root
    Pass: Kashdref4382
    Host: localhost