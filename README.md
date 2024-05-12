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



# Formatting Metadata

- Formatting Tracks:

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

- Removing Unwanted Tracks:

The function keep filters out tracks based on certain criteria, such as tracks with missing audio or clips, or tracks for which feature extraction failed.
It prints the number of tracks lost and the number of tracks remaining after each filtering step.

- Cleaning Genres:

It performs various cleaning operations on the genres data.
Redundant columns like 'genre_handle' and 'genre_color' are dropped.
Missing values in the 'parent' column are filled with zeros, and the column is converted to integer type.
Corrections are made for specific genre-parent relationships where the parent was missing or incorrect.
A specific genre (806) is replaced with another genre (21) to correct a mistake.
A function get_parent is defined to retrieve the parent genre recursively.
Another function get_all_genres is defined to gather all genres encountered from leaf to root.
The number of tracks per genre is counted.
Genres with zero tracks are identified and printed.

- Matching Genres with Tracks:

It matches the 'genre_top' values from tracks with genre IDs from the genres DataFrame.
A new DataFrame is created with matched genre IDs and their corresponding information from the genres DataFrame.

- Merging DataFrames:

The matched genres DataFrame is merged with additional information from the tracks DataFrame, such as album ID, album title, artist ID, artist name, and track title.
Column names are updated for clarity.
Unnecessary columns like 'genre_id', 'album_id', and 'artist_id' are dropped.
Redundant columns are dropped again.
Finally, column names are further refined for clarity.

# Extract MFCC Features and save in MongoDb 
  Next we define a function extract_and_store_mfcc that extracts Mel-frequency cepstral coefficients (MFCC) features from audio files and saves them into a MongoDB database. Here's what the code does:

- Function Definition:

The function extract_and_store_mfcc is defined, taking several parameters such as the audio directory, MongoDB connection parameters (URI, database name, collection name), a DataFrame containing track information, and an optional scaler for normalization or standardization.

- Connecting to MongoDB:

The function connects to the MongoDB instance using the provided connection parameters.

- Iterating Through Audio Files:

It iterates through each folder in the specified audio directory.
For each folder, it iterates through each audio file.
It loads the audio file and extracts MFCC features using the librosa library.
Applying Normalization or Standardization:

If a scaler is provided, it normalizes or standardizes the MFCC features.

- Matching Track Information:

It extracts the track ID from the file name and matches it with corresponding information from the provided DataFrame (merged_df).

- Storing Data in MongoDB:

It creates a dictionary containing the track's genre, album, artist, track ID, title, and MFCC features.
It inserts this data into the MongoDB collection.

- Handling Errors:

It catches any exceptions that occur during processing and prints error messages.
Closing MongoDB Connection:

After processing all audio files, it closes the MongoDB connection.

- Calling the Function:

Finally, the function is called with the specified parameters to extract MFCC features from audio files in the given directory and store them in MongoDB.
This code enables the extraction and storage of MFCC features, facilitating further analysis or machine learning tasks such as music recommendation or genre classification.

# Deployment (Melodify Application) 

- Flask:

Flask is like the foundation of our music streaming website. It helps us create different parts of the website and decide what to do when someone visits certain pages.
- KafkaProducer:

Think of KafkaProducer like a mailman. It's responsible for sending messages about what people are doing on our website to a special place called Kafka.
- KafkaConsumer:

KafkaConsumer is like a listener who waits for messages from Kafka. When someone does something on our website, like listening to a song, KafkaConsumer hears about it.
- Initialization:

We set up the mailman (KafkaProducer) and the listener (KafkaConsumer) to connect to our website and Kafka, making sure they know where to send and receive messages.
- Routes:

We decide what happens when someone visits different parts of our website. For example, when someone goes to the main page, they get a welcoming message. When they ask for music recommendations, we handle that too.This is like a special function that's called when someone asks for music recommendations. It tells the mailman (KafkaProducer) to send a message saying someone is listening to music. Then, it waits for recommendations to come back from Kafka, our message hub.

- Running the Application :

When we run the code, it starts our music streaming website. It's like opening a shop for people to visit on the internet.
- Output:

When someone visits our website, they'll see a nice welcome message.
If someone wants music recommendations, they can ask, and our website will give them some based on what other people are listening to.
