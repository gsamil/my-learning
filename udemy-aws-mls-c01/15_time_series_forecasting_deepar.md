# Time Series Forecasting - DeepAR

## Introduction to DeepAR Time Series Forecasting (Lesson 155)

- DeepAR is Amazon SageMaker's built-in time series forecasting algorithm that uses recurrent neural networks (RNNs).

### Components of Time Series
- **Noise**: Random fluctuations that can't be predicted.
- **Trend**: Long-term increase or decrease in the target value.
- **Seasonality**: Patterns that repeat at specific intervals.

### Benefits of Using DeepAR
- **Handling Non-Stationarity**: Unlike ARIMA, DeepAR doesn't require removing seasonal and trend components, simplifying the process.
- **Multiple Time Series**: Capable of training on multiple related time series, useful for diverse applications like utility usage forecasting.
- **Feature Inclusion**: Supports flags for events like Black Friday or Diwali to improve forecasting accuracy.

## DeepAR Training and Inference Formats (Lesson 156)

### Training Data Division
- **Other Algorithms**: Random division into training and test sets.
- **DeepAR**: Requires time-ordered data; cannot randomly divide. 

### Prediction Length Hyperparameter
- **DeepAR Specific**: Defines how far in the future the model forecasts.
- **Immutability**: Once set, the prediction length cannot be changed after training.

### Training and Test Set Splitting
- **Training Set**: Comprises the entire time series except the last 'prediction length' number of points.
- **Test Set**: Includes the entire time series, encompassing the last 'prediction length' points.

### Training File Format
- **Formats Supported**: JSON Lines, Parquet and optional compression of training files.
- **Inference Input**: Requires JSON format.

### Structure of Training File
- **start**: Timestamp for the time series.
- **target**: Array of floating or integer values.
- **dynamic_feat**: Optional input featues, array of arrays for each feature.
- **cat**: Optional category, identifies a specific time series.

### Challenges with Dynamic Features
- **No Missing Values Allowed**: Requires handling missing values for dynamic features.
- **Future Prediction**: Requires future values of dynamic features for forecasting.

### Inference Format
- **Similar to Training**: Wrapped in an 'instances' field.
- **Necessity of Complete Time Series**: Includes historical data, dynamic features, and categories for prediction.
- **Length Consideration**: Number of values in dynamic features should equal the length of the target plus prediction length.
