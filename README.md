Here’s a well-structured `README.md` file that provides clear documentation for the pipeline:

---

# Physical Activity Monitoring ML Pipeline

This repository implements a machine learning pipeline for analyzing physical activity data from wearable sensors (IMUs and heart rate monitors). The goal is to develop predictive models to classify physical activities and derive actionable insights to improve the Colibri Wireless device.

## Project Structure

```
physical_activity_monitoring/
├── data/                          # Folder to store datasets
├── src/                           # Folder to store scripts
│   ├── data_loader.py             # Data loading and preprocessing
│   ├── feature_engineering.py     # Feature engineering and selection
│   ├── model_training.py          # Model training and hyperparameter tuning
│   ├── model_evaluation.py        # Model evaluation and metrics
│   └── utils.py                   # Utility functions
├── main_pipeline.py               # Main pipeline script
├── requirements.txt               # List of dependencies
└── README.md                      # Project documentation
```

## Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Pipeline Components](#pipeline-components)
- [Setup and Installation](#setup-and-installation)
- [Running the Pipeline](#running-the-pipeline)
- [Customization](#customization)
- [Results and Evaluation](#results-and-evaluation)

## Overview

This project aims to:
1. Preprocess wearable sensor data (IMUs, heart rate monitors).
2. Perform feature engineering and selection.
3. Train models to classify physical activities.
4. Evaluate models for accuracy and other performance metrics.

The pipeline enables a modular approach to data preprocessing, feature selection, model training, and evaluation. It allows for rapid experimentation and fine-tuning to improve activity classification accuracy.

## Dataset

The dataset contains sensor readings from multiple IMUs and a heart rate monitor, with data collected for various physical activities. Each sample includes:
- IMU data (acceleration, gyroscope, magnetometer readings) from wrist, chest, and ankle.
- Heart rate data.
- Activity labels for each time sample (e.g., walking, running).

Ensure the dataset is named `collected_data.csv` and placed in the `data/` folder.

## Pipeline Components

### 1. Data Loader and Preprocessing (`src/data_loader.py`)
- **Functionality**: Loads and preprocesses data, drops irrelevant columns, handles missing values, and removes transient activity records.
  
### 2. Feature Engineering and Selection (`src/feature_engineering.py`)
- **Functionality**: Uses Sequential Feature Selector (SFS) to identify the most important features for activity classification.
  
### 3. Model Training (`src/model_training.py`)
- **Functionality**: Supports model training for linear regression and random forest models, with optional hyperparameter tuning via GridSearchCV.

### 4. Model Evaluation (`src/model_evaluation.py`)
- **Functionality**: Evaluates models using Mean Squared Error (MSE) and R-squared. This component can be extended to include additional metrics as needed.

### 5. Utility Functions (`src/utils.py`)
- **Functionality**: Provides helper functions for file path management, configuration, and other reusable functions.

### 6. Main Pipeline (`main_pipeline.py`)
- Orchestrates the entire pipeline, integrating data loading, preprocessing, feature selection, model training, and evaluation.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/physical_activity_monitoring.git
   cd physical_activity_monitoring
   ```

2. **Install Dependencies**:
   - Use `requirements.txt` to install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Prepare the Dataset**:
   - Place `collected_data.csv` in the `data/` directory.

## Running the Pipeline

Run the pipeline by executing:

```bash
python main_pipeline.py
```

The pipeline will:
1. Load and preprocess the data.
2. Select important features using Sequential Feature Selector.
3. Train a machine learning model.
4. Output model performance metrics, including MSE and R-squared.

## Customization

To customize the pipeline:
- **Change Models**: Modify `train_model` in `model_training.py` to use different models or adjust hyperparameters.
- **Adjust Feature Selection**: Change the number of features in `select_features` within `feature_engineering.py`.
- **Add New Metrics**: Extend `evaluate_model` in `model_evaluation.py` to include additional evaluation metrics.

## Results and Evaluation

Model performance metrics (MSE and R-squared) will be printed to the console after each run. These metrics help assess the accuracy and effectiveness of the model in predicting physical activities.

---

## Notes

1. **Hyperparameter Tuning**: This pipeline includes basic hyperparameter tuning for the random forest model. You can extend tuning options as needed.
2. **Modular Design**: Each module can be run independently or modified for specific experiments without affecting the entire pipeline.

## Contact

For questions, please contact [yogeswara badepalli](mailto:yogeswar1992.b@gmail.com).

---

This `README.md` file provides a clear overview of the project and guides users through setup, execution, and customization options, ensuring the pipeline is easy to understand and extend.
