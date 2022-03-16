# Welcome onboard!

This is the repository for the minischool on MOABB, the Mother of All BC Benchmarks.

## Installation

There is several possibilities. If you already have a working Python 3 environnement, you could use pip: \
`pip install MOABB`

If you do not have a Python environment, we recommand installing [Ananconda](https://www.anaconda.com/products/individual). We have USB key with the 
There are two option, the first on is creating a specific environment. You need to download this [environment.yml](https://gist.githubusercontent.com/sylvchev/4d04fd88d6f382d936a3ca56294f8393/raw/07d69e6d8bfe54c0523c7d71a5c07da949d732f6/environment.yml) file on this page and run the following command: \
`conda env create -f environment.yml` \
The other option is to use poetry, as explained on the [MOABB website](https://github.com/NeuroTechX/moabb/#installation).

# Minischool

## Part 0 - Verification

Check your installation with [`notebooks/0_Minischool_Verify_Installation`](https://github.com/sylvchev/moabb_minischool/blob/main/notebooks/0_Minischool_Verify_Installation.ipynb)

## Part 1 - Discovering MOABB

This first notebook demonstrate how to use MOABB, with a simple example on a famous motor imagery dataset. See [`notebooks/1_Minischool_Discovering_MOABB.ipynb`](https://github.com/sylvchev/moabb_minischool/blob/main/notebooks/1_Minischool_Discovering_MOABB.ipynb)

## Part 1bis - Pyriemann

This interlude is meant to demonstrate some simple code to use Riemannian geometry with PyRiemann. See [`notebooks/1bis_Minischool_Pyriemann`](https://github.com/sylvchev/moabb_minischool/blob/main/notebooks/1bis_Minischool_Pyriemann.ipynb)

## Part 2 - Benchmark with P300 datasets

This notebook illustrate advanced possibilities of MOABB with an example benchmark on P300 dataset. See [`notebooks/2_Minischool_P300_Benchmarks`](https://github.com/sylvchev/moabb_minischool/blob/main/notebooks/2_Minischool_P300_Benchmarks.ipynb)

