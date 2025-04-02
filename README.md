# BioIO plotter

A simple library to easily plot BioIO images with matplotlib.

## Installation

```bash
git clone https://github.com/Rylern/bioio-plotter          # clone this repository
cd python-lut                                           # go to the project directory
python -m venv ./.venv                                  # create a local virual environment
source ./.venv/bin/activate                             # activate the venv
pip install -e ".[dev,test]"                            # install bioio_plotter (-e means changes are loaded dynamically)
jupyter lab .                                           # to start the Jupyter notebooks
pytest                                                  # to run unit tests
```