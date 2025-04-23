# PRISMXsec

This repository contains the code accompanying our paper on cross-section measurements using the PRISM Proof of Concept (PoC) for the Deep Underground Neutrino Experiment (DUNE). It provides scripts and workflows to perform cross-section analysis, including event rate calculations, differential cross-sections, and unfolding procedures. The repository is organized to follow a logical sequence of steps for analysis.

## Overview

This repository facilitates the analysis and reproduction of results presented in our study. Below is the recommended order of usage for the Jupyter Notebooks to guide you through the workflow:

1. **Toy Data Generation and Preparation**:
   - `ToyWeightsGenerator.ipynb`: Generates weights for toy datasets.
   - `DefineRebinningEventByEvent.ipynb`: Prepares event-by-event rebinning.
   - `ToysROOTtoNumpy.ipynb`: Converts ROOT files to NumPy arrays for easier manipulation.
   - `NumpyToysToMeasurements.ipynb`: Converts off-axis toy measurements into virtual flux measurement, preparing it for cross-section calculation plots.

2. **Cross-Section Calculations**:
   - `DiffXSec.ipynb`: Calculates differential cross-sections.
   - `IntegratedXSec.ipynb`: Computes integrated cross-sections.

In addition to the code used to produce the main plots of the paper, we also include the following:

1. **Unfolding Procedures**:
   - `NumpyToysToUnfoldedMeasurements.ipynb`: Turns off-axis toy measurements into virtual event rates unfolded into true energy transfer.
   - `UnfoldingPlot.ipynb`: Visualizes the results of the unfolding procedures.

2. **Event Rate Estimations**:
   - `EventRatesAccordingToRunPlan.ipynb`: Our calculation of the estimated event rates based on the run plan cited in the paper.

3. **Coefficient Calculations**:
   - `CoefficientsCalcPlus.ipynb`: A notebook containing functions used by many other notebooks (by importing).

## Repository Structure

The repository is organized as follows:

- **Grid scripts**:
  - Located in `ToyGenerationScripts/` for generating toy datasets.
- **NuWro simulation scripts**:
  - Located in `NuWro/` for generating NuWro samples.
- **Data Files**:
  - `Fluxes.ND.root`: ND neutrino flux nominal data.
  - `flux_shifts_OffAxis.root`: ND flux uncertainties for off-axis positions.
- **Processed Data Files**:
  - `.csv` files (`Nbins`, `BinWidths` and `BinCenters`) created by directly fetching the data from the TH2Jagged in the flux uncertainty file:
    - `Nbins.csv` contains the number of bins in each off-axis position.
    - `BinWidths.csv` contains the width in GeV for each off-axis, energy bin.
    - `BinCenters.csv` contains the center of each energy bin in GeV.
- **Analysis Notebooks**:
  - Jupyter Notebooks as outlined in the workflow above.
