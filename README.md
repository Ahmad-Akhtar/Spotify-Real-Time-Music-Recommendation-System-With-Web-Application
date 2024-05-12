# Big data project : Create Your Own Spotify Experience



# Collaborators :
The group members for this assignment are :
- Ahmad Akhtar 21I-1655
- Inam ul Haq 22I-1906
- Abdurrehman 22I-1963

# Data Set 
You can download data set (fma_large.zip) from this link:

"https://github.com/mdeff/fma.git"

This dataset comprising 106,574 tracks, each lasting 30 seconds, and spanning 161 unevenly distributed genres.

# Important Libraries for Phase 1:

- import os
- import shutil
- import random
- import zipfile
- import numpy as np
- import librosa
- from tqdm import tqdm
- from pymongo import MongoClient
- from bson.binary import Binary
- import pickle
- import pandas as pd
- import ast
- import IPython.display as ipd
- from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Extract, Transform, Load (ETL) Pipeline

- Extracting the FMA Metadata Zip File:

The first part of the code extracts a zip file containing metadata related to the FMA dataset.
The function extract_zip is defined to extract the contents of the zip file to a specified directory.

- Setting Directories and Environment Variables:

After extraction, it sets up the directories and environment variables necessary for working with the FMA dataset.
It checks if the required directory exists. If not, it raises a FileNotFoundError.
It sets the environment variable AUDIO_DIR to the directory containing the audio files.

- Loading Metadata:

Next, it loads metadata from CSV files into Pandas DataFrames. This metadata includes information about tracks, albums, artists, and genres.
It loads the metadata from CSV files located in the extracted directory.

- Processing Audio Files:

It defines a function get_tids to retrieve track IDs from audio files in the specified directory.
It collects track IDs for the FMA_LARGE dataset by calling get_tids with the appropriate directory.

- Analyzing Metadata and Audio Files:

The code then performs various analyses on the collected metadata and audio files.
It prints out statistics such as the number of tracks, albums, artists, genres, and audio files collected, as well as any discrepancies or missing data.
It displays a sample of the loaded data for tracks, albums, artists, and genres.



# Formatting Tracks Metadata

It begins by formatting the tracks metadata.
It drops several columns that are deemed unnecessary or have a significant amount of missing data.
The convert_datetime function is used to convert date columns to datetime format.
It converts genres from string representations to lists of integers.
Finally, it renames columns for clarity and consistency.

- Formatting Albums:

Similarly, it formats the albums metadata.
It drops redundant columns already present in the tracks dataframe.
Date columns are converted to datetime format.
Renaming of columns and handling missing values are performed.

- Formatting Artists:

It formats the artists metadata, dropping redundant columns.
Date columns are converted to datetime format, and missing values are handled.
Renaming of columns is also performed.

- Merging DataFrames:

After formatting individual dataframes, they are merged based on common keys (e.g., album_id, artist_id).
Missing values are handled, and duplicate columns resulting from the merge are cleaned up.
It ensures that the merged dataframe maintains consistency and correctness.

- Additional Formatting:

Remaining missing values are filled or replaced with appropriate defaults.
Certain columns are cast to integer data types for consistency.

- Quality Assurance:

Assertions are used to ensure the correctness of the formatting process, checking for expected conditions after each step.
