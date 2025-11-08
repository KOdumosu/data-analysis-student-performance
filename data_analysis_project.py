# data_analysis_project.py
# Author: Kehinde Olusegun Odumosu
# Course: CSE 310 – Applied Programming (Data Analysis Module)
# Description: Analyze and visualize student performance data using Pandas, Matplotlib, and Seaborn.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load dataset
    data = pd.read_csv("StudentsPerformance.csv")

    # Display first few rows
    print("Preview of dataset:")
    print(data.head())

    # Basic info
    print("\nDataset Info:")
    print(data.info())

    # Handle missing values (if any)
    data = data.dropna()

    # Summary statistics
    print("\nSummary Statistics:")
    print(data.describe())

    # Correlation heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap of Scores")
    plt.show()

    # Distribution plots
    plt.figure(figsize=(8,6))
    sns.histplot(data["math score"], bins=20, kde=True)
    plt.title("Distribution of Math Scores")
    plt.xlabel("Math Score")
    plt.ylabel("Count")
    plt.show()

    plt.figure(figsize=(8,6))
    sns.boxplot(x="gender", y="reading score", data=data)
    plt.title("Reading Scores by Gender")
    plt.show()

    # Group comparison: parental education vs average scores
    avg_scores = data.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
    avg_scores.plot(kind="bar", figsize=(10,6))
    plt.title("Average Scores by Parental Education Level")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print("\nAverage Scores by Parental Education Level:")
    print(avg_scores)

if __name__ == "__main__":
    main()
