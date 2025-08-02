# 🎬 IMDb Movie Overview Sentiment Analyzer

This is a lightweight web application built with Python and Flask that performs basic sentiment analysis on movie overviews from the IMDb Top 1000 dataset. It classifies each description into a general sentiment — positive, negative, or neutral — based on the presence of specific keywords.

---

## 📖 Project Overview

The goal of this project is to explore a simple, keyword-based approach to sentiment analysis, without relying on external libraries such as NLTK or pandas. The application reads movie overviews from a CSV file and highlights the dominant sentiment along with supporting keywords.

This can serve as an introductory-level project for students learning about Flask, sentiment analysis, and working with datasets in Python.

---

## 🔧 How It Works

- Loads data directly from a CSV file (`imdb_top_1000[1].csv`)
- Analyzes the “Overview” column using regular expressions
- Classifies each review into:
  - **Positive** (e.g., "amazing", "love", "great")
  - **Negative** (e.g., "boring", "bad", "worst")
  - **Neutral** (e.g., "movie", "film", "acting")
- Displays the dominant sentiment, word counts, and highlighted keywords

---

### Requirements

- Python 3.7+
- Flask

## 🗂 Project Structure

