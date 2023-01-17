# Unidentified Aerial Phenomena - UAP

## Introduction and Motivation
Would the careful application of machine learning techniques to the analysis of unidentified aerial phenomena (UAP) yield insights into the nature of these objects and events? More specifically, are there clusters of sightings within the data that demonstrate statistically significant patterns in word choice, and color description? Finding these clusters would be a first step in understanding the nature of UAP, and for the first time, providing a rationality score to the phenomenon; transforming a community of conspiracy theorists into a more credible and data-backed group of paranormal enthusiasts.

## Use of chatGPT for this project

### What is chatGPT?

chatGPT is a chatbot that uses a large language model to generate responses to user input. It is a project by OpenAI.

### What prompt should we use to get the project going?

The prompt for this project is:

> You are a UFOlogist (Researcher of UAP, unidentified aerial phenomena) and Python Programmer with specialities in Machine learning, Unsupervised Learning, Clustering, Neural Networks, Text Mining, and NLP.
> Defining the Goal:
> Goal 1. Your first goal is to create a program that will be able to use data preprocessing pipelines to clean raw report text data from reports of UAP.
> Goal 2. Use the text data collected along with the dates of the reports, geographic locations of the reports, and the shapes of the reported UAPs, and build a model to cluster the reports, considering them like points on a plane. The plane will have 3 dimensions: time, location (lat,long). The clusters will be the groups of reports that are similar to each other. This introduces another dimension to the plane: the shape of the UAPs. The clusters will be the groups of reports that are similar to each other after the text has been vectorized with TFIDF and the shape of the UAPs has been one-hot encoded.
> Goal 3. You will give them a credibility score from 0 to 100 based on the words they use in their reports and how well they align with others in the same area(s) and time(s).

> The Outcome of the Project: The outcome of the project will be a program that can be used to cluster UFO reports and give them a credibility score based on the words they use in their reports and how well they align with others in the same area(s) and time(s).

> You will abide by the following constraints:
* The program must be written in Python 3.6 or higher.
* Any libraries used must be open source and free to use.
* Use Pandas, Numpy, and Matplotlib for data manipulation, analysis, and visualization.
* Use NLTK for natural language processing.
* Use SciPy for scientific computing.
* Use Scikit-learn for machine learning.
* Use Keras for deep learning.

## Project Planning

To achieve the defined goals, the following steps can be taken:

Data preprocessing: Use Pandas to load and clean the raw text data from the reports of UAP. Use NLTK for text preprocessing tasks such as tokenization, stemming, and stop-word removal.

Feature engineering: Use the cleaned text data, along with the dates of the reports, geographic locations of the reports, and the shapes of the reported UAPs, to create a dataset that can be used to train the model. Use one-hot encoding to represent the shape of the UAPs and TF-IDF to vectorize the text data.

Clustering: Use Scikit-learn's KMeans or DBSCAN to cluster the reports based on their similarity. The features used for clustering will be the vectorized text, the one-hot encoded shape, and the location and date of the report.

Credibility scoring: Use the clustering results, along with the words used in the reports, to give a credibility score to each report. This can be done by analyzing how well the words used in a report align with the words used in other reports in the same cluster.

Visualization: Use Matplotlib to visualize the clusters on a 2D or 3D plane.


## Data

### What data do we have on UAP?

* The National UFO Reporting Center (NUFORC) has been collecting data on UAP sightings since 1974. The data is available for download in CSV format, and will be included in our data folder as `nuforc_reports.csv` for use in this project. The data is also available in JSON format, and can be found at the [NUFORC API](https://www.nuforc.org/webreports.html).

* The Mutual UFO Network (MUFON) has been collecting data on UAP sightings since 1969. The data is available for download in CSV format, and will be included in our data folder as `mufon_reports.csv` for use in this project. *The data is also available in JSON format, and can be found at the [MUFON API](https://api.mufon.com/).*

## Data Dictionary

### NUFORC Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|datetime|object|NUFORC|Date and time of the sighting|
| city|object|NUFORC|City where the sighting occurred|
| state|object|NUFORC|State where the sighting occurred|
| shape|object|NUFORC|Shape of the object sighted|
| duration (seconds)|float|NUFORC|Duration of the sighting in seconds|
| duration (hours/min)|object|NUFORC|Duration of the sighting in hours and minutes|
| summary|object|NUFORC|Summary of the sighting|
| posted|object|NUFORC|Date and time the report was posted|
| latitude|float|NUFORC|Latitude of the sighting|
| longitude|float|NUFORC|Longitude of the sighting|


### MUFON Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|datetime|object|MUFON|Date and time of the sighting|

## Data Preparation

### NUFORC Data Preparation

<!-- notebooks/data_cleaning.ipynb -->
To prepare the NUFOC data for analysis, we ran the `notebooks/data_cleaning.ipynb` notebook. This notebook does the following:

* list what it does

**Result: the cleaned file ** is saved to `data/processed/ufos_clean.csv`.

### MUFON Data Preparation

This is more difficult than the NUFORC data. It also does not include latitude and longitude natively, as these have to be derived from city names which does not lend itself to a high accuracy score. The data is also not as clean as the NUFORC data, and requires more preprocessing and wrangling.

## Feature Engineering

### NUFORC Feature Engineering

Run the `notebooks/feature_engineering.ipynb` notebook to create the features for the model. This notebook does the following:

* list what it does

It produces a data file called `data/processed/nuforc_clean_plusfeatures.csv` that is used in the modeling notebook.

### MUFON Feature Engineering

None yet for MUFON data.

## Modeling