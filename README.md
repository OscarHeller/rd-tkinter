# rd-tkinter

## Windows install

### OS-level dependencies

* Install latest Python 3 (last tested with 3.6.0): https://www.python.org/downloads/windows/ 
  * The default install for Python 3.6.0 includes tkinter, another dependency of the project.
* Add Python 3 to your system path
* Rename the `python` executable to `python3`
* Test by running `python3 --version` in a new command prompt
* Install git: https://git-for-windows.github.io/
* Install virtualenv: `http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html`

### One-time setup

* Open a command prompt and navigate to the parent folder of your choice
* Pull the repository: `git clone git@github.com:OscarHeller/rd-tkinter.git`
* Enter the project directory: `cd rd-tkinter`
* Create a virtual environment: `virtualenv venv -p <absolute path to python3 install>`
  * Example: `virtualenv venv -p "C:\Users\username\AppData\Local\Programs\Python\Python36"`

### Run

* Pull the latest version: `git pull`
* Activate the virtual environment: `venv\Scripts\activate`
* Run the project: `python main.py`
