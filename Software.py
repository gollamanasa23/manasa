# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:01:35 2023

@author: User
"""

# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset

data1=pd.read_csv(r"C:\Users\house_national_forecast.csv")

# EDA

print(data1.head(4))

print(data1.tail())

data1.info()

print(data1.describe())

print(data1.columns)

# Checking the null values

print(data1.isna().sum())

print(data1.shape)

# Convert the "forecastdate" column to a datetime object
data1['forecastdate'] = pd.to_datetime(data1['forecastdate'])

# Select the data for a specific party (e.g., 'D')
party_data = data1[data1['party'] == 'D']


# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(party_data['forecastdate'], party_data['mean_seats'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Mean Seats')
plt.title('Mean Seats Over Time for Party D')
plt.grid(True)
plt.show()


# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data1['win_probability'], data1['mean_seats'], alpha=0.5)
plt.xlabel('Win Probability')
plt.ylabel('Mean Seats')
plt.title('Scatter Plot of Win Probability vs. Mean Seats')
plt.grid(True)
plt.show()


# Histogram Plot
data_to_plot = data1['mean_seats']
plt.figure(figsize=(10, 6))
plt.hist(data_to_plot, bins=20, edgecolor='k', alpha=0.7)
plt.xlabel('Mean Seats')
plt.ylabel('Frequency')
plt.title('Histogram of Mean Seats')
plt.grid(True)
plt.show()

# Pie Charts
total_mean_seats = party_data['mean_seats'].sum()
plt.figure(figsize=(8, 8))
plt.pie(party_data['mean_seats'], labels=party_data['forecastdate'], autopct='%1.1f%%')
plt.title('Distribution of Mean Seats for Party D')
plt.axis('equal') 
plt.show()