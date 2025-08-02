import os
import csv
import re
from flask import Flask, request, render_template

app = Flask(__name__)

# ====== Load CSV Data ======
CSV_FILE_NAME = os.path.join(os.path.dirname(__file__), "imdb_top_1000[1].csv")
movie_reviews = []

try:
    with open(CSV_FILE_NAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("📋 CSV Columns:", reader.fieldnames)  # Debug print

        for row in reader:
            if 'Overview' in row and row['Overview'].strip():
                movie_reviews.append(row['Overview'].strip())

    print(f"✅ Loaded {len(movie_reviews)} reviews.")
except Exception as e:
    print(f"❌ Error loading CSV: {e}")

# ====== Sentiment Map ======
sentiment_map = {
    "positive": {"love", "best", "amazing", "great", "enjoy", "excellent", "masterpiece", "beautiful"},
    "negative": {"boring", "worst", "bad", "terrible", "awful", "disappointing", "poor", "dull"},
    "neutral": {"movie", "film", "story", "acting", "director"}
}

# ====== Analyzer Function ======
def analyze_review(review):
    words = re.findall(r'\b\w+\b', review.lower())
    sentiment_counts = {label: 0 for label in sentiment_map}
    highlights = []

    for word in words:
        for label, word_set in sentiment_map.items():
            if word in word_set:
                sentiment_counts[label] += 1
                highlights.append((word, label))

    dominant = max(sentiment_counts, key=sentiment_counts.get)
    return {
        "Dominant Sentiment": dominant,
        "Counts": sentiment_counts,
        "Highlights": highlights,
        "Review": review
    }

# ====== Web Routes ======
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    sample_reviews = movie_reviews[:3]  # show 3 on homepage

    if request.method == "POST":
        review = request.form["review"]
        result = analyze_review(review)

    return render_template("index.html", result=result, samples=sample_reviews)

if __name__ == "__main__":
    app.run(debug=True)
