# Movie Recommendation System

A simple content- and metadata-based movie recommendation system built with Python and Flask. This repository includes the dataset files, precomputed model artifacts, a Jupyter notebook for exploration, and a small Flask app to serve recommendations.

Repository: https://github.com/DS-Parihar/Movie_Recommendation_System

## Features

- Preprocessed datasets (TMDb 5000 movies and credits CSVs)
- Precomputed recommendation model artifacts (movies.pkl, movies_dict.pkl)
- Jupyter notebook demonstrating data exploration and model building (Movie_Recommeder.ipynb)
- Flask web app to serve movie recommendations (app.py)
- Deployment helpers: `requirements.txt`, `setup.sh`, and `procfile`

## Files

- `Movie_Recommeder.ipynb` — Notebook showing data processing and recommendation logic.
- `app.py` — Flask application that loads precomputed pickles and exposes a web UI/API for recommendations.
- `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv` — Raw datasets used to build the recommender.
- `movies.pkl`, `movies_dict.pkl` — Serialized model/data objects used by `app.py` at runtime.
- `requirements.txt` — Python dependencies.
- `setup.sh` — Optional setup script (e.g., for Heroku deployment).
- `procfile` — Process file for Heroku-like deployments.

## Quickstart (Run locally)

1. Clone the repository

   git clone https://github.com/DS-Parihar/Movie_Recommendation_System.git
   cd Movie_Recommendation_System

2. (Optional) Create and activate a virtual environment

   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows (PowerShell)

3. Install dependencies

   pip install -r requirements.txt

4. Start the Flask app

   python app.py

5. Open your browser and go to http://127.0.0.1:5000 to use the web UI (or check the endpoints defined in `app.py`).

Notes:
- The app expects the precomputed `movies.pkl` and `movies_dict.pkl` files to be present in the repository root; they are already included.
- If you want to rebuild the model from the CSV files, open `Movie_Recommeder.ipynb` and follow the notebook steps to preprocess and recompute the artifacts.

## Deployment

- This project contains a `procfile` and `setup.sh` to help deploy on Heroku or similar platforms. The Procfile typically uses a WSGI server like Gunicorn (e.g., `web: gunicorn app:app`) — verify `procfile` contents before deploying.

## Implementation notes

- The recommendation algorithm in the notebook uses metadata (genres, cast, crew, keywords) and TF-IDF/ cosine similarity approaches to compute movie similarity.
- The Flask app (`app.py`) loads precomputed pickles to serve recommendations quickly without recomputing features at runtime.

## Contributing

Contributions, issues, and feature requests are welcome. If you want to improve the recommender, consider:

- Adding caching for faster responses
- Exposing a JSON API for programmatic access
- Improving recommendations with collaborative filtering or hybrid approaches
- Cleaning and standardizing the TMDb data further

Please open an issue or submit a pull request.

## License

This repository does not include an explicit license. If you want to add one, consider adding a LICENSE file (e.g., MIT License) to clarify usage and contributions.

## Contact

Maintainer: DS-Parihar 
