# 155. Introduction to DeepAR Time Series Forecasting

## Introduction to Time Series Forecasting
- **Definition**: Forecasting based on time series data, where values are collected at specific frequencies.
- **Characteristics**: Data correlated with previous time steps, potential for seasonal patterns and trends.

## Time Series vs. Regular Algorithms
- **Temporal Order**: Regular algorithms like XGBoost don't handle date-time features natively, requiring feature engineering.
- **Time Series Algorithms**: Directly learn from the temporal order of data, handling date-time features inherently.

## Components of Time Series
- **Noise**: Random fluctuations that can't be predicted.
- **Trend**: Long-term increase or decrease in the target value.
- **Seasonality**: Patterns that repeat at specific intervals.

## Benefits of Using DeepAR
- **Handling Non-Stationarity**: Unlike ARIMA, DeepAR doesn't require removing seasonal and trend components, simplifying the process.
- **Multiple Time Series**: Capable of training on multiple related time series, useful for diverse applications like utility usage forecasting.
- **External Features Support**: Accommodates external variables affecting the time series, enhancing the model's learning capability.

## Use Cases
1. **Banking**: Aggregating ATM transactions for cash management.
2. **Social Media**: Analyzing post timings.
3. **Healthcare**: Scheduling doctor appointments.

## DeepAR Advantages
- **Training Efficiency**: Unlike classical algorithms, DeepAR allows training a single model for multiple time series.
- **Seasonality and Trend**: No need for data transformation to remove these components.
- **Feature Inclusion**: Supports flags for events like Black Friday or Diwali to improve forecasting accuracy.

## Summary
- Time series forecasting addresses a wide range of business problems.
- DeepAR offers advantages in handling multiple time series and external factors.
- Suitable for datasets with hundreds of related time series, outperforming traditional methods like ARIMA and ETS.

# 156. DeepAR Training and Inference Formats

## Overview
- **Context**: Time series forecasting with Amazon SageMaker's DeepAR algorithm.
- **Focus**: Key differences from other SageMaker algorithms in terms of training and inference.

## Training Data Division
- **Other Algorithms**: Random division into training and test sets.
- **DeepAR**: Requires time-ordered data; cannot randomly divide. 

## Prediction Length Hyperparameter
- **DeepAR Specific**: Defines how far in the future the model forecasts.
- **Immutability**: Once set, the prediction length cannot be changed after training.

## Training and Test Set Splitting
- **Training Set**: Comprises the entire time series except the last 'prediction length' number of points.
- **Test Set**: Includes the entire time series, encompassing the last 'prediction length' points.

## Example: Energy Consumption Forecasting
- **Single Model Training**: For all customers, using their time series data.
- **Forecasting for Specific Customer**: Provide customer-specific time series to the trained model.

## Training File Format
- **Formats Supported**: JSON Lines and Parquet.
- **Compression**: Optional compression of training files.
- **Inference Input**: Requires JSON format.

## Structure of Training File
- **Start Field**: Timestamp for the time series.
- **Target Field**: Array of floating or integer values.
- **Dynamic Features**: Optional, array of arrays for each feature.
- **Categories**: Optional, identifies a specific time series.

## Challenges with Dynamic Features
- **No Missing Values Allowed**: Requires handling missing values for dynamic features.
- **Future Prediction**: Requires future values of dynamic features for forecasting.

## Inference Format
- **Similar to Training**: Wrapped in an 'instances' field.
- **Necessity of Complete Time Series**: Includes historical data, dynamic features, and categories for prediction.
- **Length Consideration**: Number of values in dynamic features should equal the length of the target plus prediction length.

## Key Takeaways
- DeepAR requires careful consideration of time series data for training and prediction.
- Handles missing values in target but not in dynamic features.
- Suitable for forecasting scenarios with detailed time-ordered data.

# 157. Working with Time Series Data, Handling Missing Values

## Introduction
- **Objective**: Understand handling time series data in Python, detecting and handling missing steps/values.

## Tools and Data
- **Libraries**: pandas, numpy, matplotlib.
- **Data**: Sample file `Vehicletraffic.csv` with hourly traffic data.

## Preparing Data
- **Parse Dates**: Convert 'Timestamp' from object to datetime type using `parse_dates`.
- **Indexing**: Set 'Timestamp' as index for easier slicing and filtering.

## Data Slicing and Filtering
- Examples of querying data by year, month, and specific time windows using timestamp indexing.

## Plotting Time Series Data
- **Issue**: Missing time steps (e.g., 5 a.m. and 6 a.m.) are not visible due to automatic interpolation in line plots.
- **Solution**: Ensure no gaps in time series for accurate training with DeepAR.

## Handling Time Series in DeepAR
- **Resample for Missing Steps**: Use pandas' `resample` to fill missing time steps.
- **Start Time and Frequency**: Define start time and frequency (e.g., hourly) for DeepAR.
- **Handling NaN Values**: DeepAR interprets missing timestamps, important for accurate forecasting.

## Example: Vehicle Traffic Data
- **Resampling**: Filling missing time steps with NaN to show breaks in continuity.
- **Preparing for DeepAR**: Listing start time and values, including NaN for missing steps.

## Handling Missing Feature Values
- **Feature vs. Target**: DeepAR supports missing values in target time series, not in features.
- **Filling Techniques**:
  - **Forward Fill**: Propagate last valid observation forward.
  - **Backward Fill**: Use next valid observation to fill earlier gaps.
  - **Interpolation**: Linear, quadratic, polynomial, spline, etc.
- **Adding Filled Columns**: Demonstration of different filling methods for a feature.

## Summary
- Basic time series indexing and resampling techniques.
- Detection and handling of missing time steps for DeepAR.
- Various methods to fill missing feature values in time series datasets.

# 164. Summary

## Key Strengths of DeepAR
- **Multiple Time Series Training**: Capable of training with hundreds of related time series.
- **Performance**: Outperforms traditional methods like ARIMA and ETS, especially when dealing with numerous time series.
- **Prediction Methodology**: Requires historical time series data for forecasting future values.
- **Dynamic Features Support**: Accommodates external factors influencing the time series.
- **Categorization**: Allows grouping of time series for more nuanced analysis.

## Challenges in Time Series Forecasting
- **Data Preparation**: Involves handling missing steps and features.
- **Handling Missing Data**: Critical for the accuracy and effectiveness of the forecasting model.

## Resources
- Provided links for further reading and understanding of DeepAR and time series forecasting.

## Conclusion
- DeepAR is a robust tool for a variety of business forecasting needs, with the main challenge lying in meticulous data preparation.
- The section concludes with an emphasis on the importance of handling data correctly for optimal use of DeepAR.
