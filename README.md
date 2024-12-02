# Data-Analysis-Web-Application
This Olympic Data Analysis Tool uses Streamlit to explore Summer and Winter Olympic datasets. Features include medal tallies, country-wise stats, year-wise analysis, and historical trends. Built with Python, pandas, and matplotlib, it preprocesses data for clean, interactive visualizations using athlete and region datasets.

The provided project is a Streamlit-based Olympic Data Analysis Tool. Here's a brief description:

## Objective:
The project provides interactive visualizations and data analysis for Summer and Winter Olympics, allowing users to explore medal distributions, country-specific performances, and historical trends.

## Features:
 **1) Season Selection:** Users can analyze data separately for Summer and Winter Olympics.
 
 **2) Interactive Options:**
 * **Medal Tally:** Displays a sortable medal tally by country.

 * **Country-wise Analysis:** Provides a breakdown of medals for a selected country.

* **Year-wise Analysis:** Visualizes medal distribution for a selected year and country.

* **Year-wise Progress:** Charts the historical performance of a country across years.


**3)Preprocessing and Cleaning:**
Duplicates are removed, and missing values in the "region" column are handled.
The "Medal" column is standardized with "No medal" for missing entries.


## Backend Highlights:
The helper.py file contains reusable functions for data preprocessing, medal tally computation, country-specific searches, and visualization through bar charts and line graphs.
Data is sourced from two CSV files: athlete data (athlete_events.csv) and regional information (noc_regions.csv).


## Technology Stack:
* **Frontend:** Streamlit for user interface and visualization.

* **Backend:** Python with pandas and matplotlib for data manipulation and plotting.
