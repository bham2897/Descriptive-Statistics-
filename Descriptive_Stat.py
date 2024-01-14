import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

# Load the dataset
file_path = '/Users/divya/Desktop/Python projects/stroke_data.csv'
stroke_data = pd.read_csv(file_path)


# Defining a function to calculate descriptive statistics for numeric features
def descriptive_stats(data, feature):
    return data[feature].describe()

# Defining a function for plotting histograms and boxplots for numeric features
def plot_numeric(data, feature, color):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(data[feature], kde=True, ax=ax[0], color=color)
    ax[0].set_title(f'Histogram of {feature}')
    sns.boxplot(x=data[feature], ax=ax[1], color=color)
    ax[1].set_title(f'Boxplot of {feature}')
    plt.tight_layout()
    plt.show()


# Defining a function for plotting bar charts for categorical features
def plot_categorical(data, feature):
    plt.figure(figsize=(8, 5))
    ax = sns.countplot(x=feature, data=data, palette='Set2')  # Using a color palette for different colors
    plt.title(f'Bar Chart of {feature}')
    plt.xticks(rotation=0)
    # plt.legend(title=feature, loc='upper right', bbox_to_anchor=(1.15, 1), ncol=1)  # Adjusting the legend
    plt.show()

# Selecting features for descriptive analysis and visualization
numeric_features = ['Age', 'Body Mass Index (BMI)', 'Stress Levels']
colors = ['red', 'green', 'blue']  # Specify different colors for each feature


categorical_features = ['Gender', 'Hypertension', 'Heart Disease', 'Smoking Status', 'Alcohol Intake', 
                        'Physical Activity', 'Stroke History', 'Family History of Stroke', 'Dietary Habits', 'Diagnosis']


# Calculating descriptive statistics and plotting for numeric features
for feature, color in zip(numeric_features, colors):
    print(f"Descriptive Statistics for {feature}:")
    print(descriptive_stats(stroke_data, feature))
    plot_numeric(stroke_data, feature, color)

# Plotting for categorical features
for feature in categorical_features:
    plot_categorical(stroke_data, feature)
