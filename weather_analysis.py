# weather_data_analysis.py

import random
import matplotlib.pyplot as plt
import numpy as np

def generate_weather_data(days):
    """
    Generates random weather data for the given number of days.

    :param days: int, number of days to generate weather data for
    :return: list of tuples, each containing a day and its temperature
    """
    weather_data = [(day, random.uniform(-10, 40)) for day in range(1, days + 1)]
    return weather_data

def analyze_weather_data(weather_data):
    """
    Analyzes the weather data to find average temperature,
    hottest and coldest days.

    :param weather_data: list of tuples, each containing a day and its temperature
    :return: dict, results of the weather data analysis
    """
    temperatures = [temp for day, temp in weather_data]
    
    average_temp = sum(temperatures) / len(temperatures)
    hottest_day = max(weather_data, key=lambda x: x[1])
    coldest_day = min(weather_data, key=lambda x: x[1])
    
    analysis = {
        'average_temp': average_temp,
        'hottest_day': hottest_day,
        'coldest_day': coldest_day
    }
    
    return analysis

def plot_weather_data(weather_data):
    """
    Plots the weather data.

    :param weather_data: list of tuples, each containing a day and its temperature
    """
    days, temperatures = zip(*weather_data)
    
    plt.figure(figsize=(10, 5))
    plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
    plt.title('Weather Data Over Time')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

def main():
    days = 30
    weather_data = generate_weather_data(days)
    analysis = analyze_weather_data(weather_data)
    
    print("Weather Data Analysis:")
    print(f"Average Temperature: {analysis['average_temp']:.2f}°C")
    print(f"Hottest Day: Day {analysis['hottest_day'][0]} with {analysis['hottest_day'][1]:.2f}°C")
    print(f"Coldest Day: Day {analysis['coldest_day'][0]} with {analysis['coldest_day'][1]:.2f}°C")
    
    plot_weather_data(weather_data)

if __name__ == "__main__":
    main()
