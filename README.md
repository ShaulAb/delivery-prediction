# Delivery Prediction Project

## Overview
This project analyzes e-commerce delivery data to predict delivery times and understand factors affecting shipping efficiency.

## Data Exploration

### Data Loading and Preprocessing

Notebook: `interactive/00_data_loading.ipynb`
- Loaded multiple datasets and made initial data inspection
- Visualized key columns in the data to understand general behavior
- Merged all the data sources to a single dataframe
- Temporally splitted the data into training and test sets

### EDA and Benchmark Model

Notebook: `interactive/01_EDA.ipynb`
- Performed minor EDA on the training set
- Built a benchmark model using only the training set
- Evaluated the benchmark model on the test set and compared to default estimation

