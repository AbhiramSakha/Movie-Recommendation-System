# 🎥 Movie Recommender System

This project is a **Machine Learning-based Movie Recommender System** done as part of minor project at my college, **University School of Automation and Robotics, IPU East Campus, New Delhi**. This project provides personalized movie recommendations based on the movie you select. The application is powered by Python, Streamlit, and machine learning techniques, leveraging cosine similarity and the TMDB dataset.  

---

## 🌟 Features

- **Personalized Recommendations**: Suggests similar movies based on user-selected titles.
- **Poster Display**: Fetches and displays movie posters using the TMDB API.
- **Interactive UI**: Provides a user-friendly interface built with Streamlit.
- **Efficient Deployment**: Ready for deployment on Render or similar platforms.

---

## 🚀 Technologies Used

- **Machine Learning**: Cosine similarity for recommendation.
- **Streamlit**: For building the interactive front-end.
- **TMDB API**: For fetching movie posters.
- **Python Libraries**: Pandas, Scikit-learn, Requests, and more.

---

## 📂 Dataset

This project uses the **TMDb 5000 Movies dataset** from Kaggle, which includes:

- Movie metadata (title, genre, keywords, cast, crew, etc.)
- Revenue and budget details
- TMDB IDs for fetching posters

### Dataset Files:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These files are preprocessed to generate the recommendation system's core data.

---

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally:

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Pip
- Virtual environment tools (like `venv` or `conda`)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vedantroy475/movie-recommender.git
   cd movie-recommender

2. **Set Up the Virtual Environmnet**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate   # On Windows: myenv\Scripts\activate

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

4. Download Additional Files: The project requires the following preprocessed files:
    - movie_list.pkl

    - similarity.pkl  # These files are automatically downloaded from Google Drive during the app's runtime.
    - Or if you want, you can run the python code available at google colab on [here](https://colab.research.google.com/drive/1fBWvjzMKpQuqzI8ixl_RET4dFjAvSLju?usp=sharing). Make sure you first upload the 2 datasets by downloading them from the following links:
    - Link for [tmdb_5000_movies.csv](https://drive.google.com/file/d/1iA7ErSNXtFwj8bNlZE3BYf6ObyGCLIqz/view?usp=sharing) and link for [tmdb_5000_credits.csv](https://drive.google.com/file/d/1i4wKN3SHpoE8X_AkF-pwuUlUdLfUNBZC/view?usp=sharing).

5. Run the Application:
    ```bash
    streamlit run app.py

6. Access the App: Open the URL displayed in the terminal, typically http://localhost:8501.

---
## 📄 Additional Files
The repository includes:

1. Project Report: A detailed explanation of the project in PDF format (**Vedant Roy Minor Project Report on Movie Recommendation System.pdf**).
2. Presentation Slides: A concise slide deck used for the college presentation in pdf format (**Vedant Roy Minor Project Movie-Recommender-System PPT.pdf**).
---
## 🔧 Deployment

This project is ready to be deployed on Render or similar platforms. Follow these steps:

1. Push your project repository to GitHub.
2. Create a new Web Service on Render.
3. Link your GitHub repository to Render.
4. Set up a requirements.txt file for dependencies.
5. Add environment variables if necessary (e.g., TMDB API key).
6. Deploy the app, and Render will handle the rest.

---
## 🎥 Demo Video
Excited to see how the Movie Recommender System works? Check out the demo video showcasing the project in action! It demonstrates:

The interactive Streamlit interface.
Movie recommendation functionality.
Poster fetching using the TMDB API.
Click the link below to watch the full demo:
[Watch Demo Video](https://drive.google.com/file/d/1N0rXA0NhheV-fT-t9lmB8Udl1yRAfpGH/view?usp=sharing)

This video provides a comprehensive walkthrough of the project and its features. Let me know your feedback or suggestions! 😊

---
## 📬 Contact
For queries, suggestions, or collaboration, feel free to reach out to me:

LinkedIn: [Vedant Roy](https://www.linkedin.com/in/vedant-roy-b58117227/)
GitHub: [Vedantroy475](https://github.com/Vedantroy475)
Email: vedantroy3@gmail.com

---
## 🔗 References
TMDB API: The Movie Database API
Dataset: TMDb 5000 Movie Dataset on Kaggle

---
## 🙌 Acknowledgments
Special thanks to TMDB and Kaggle for providing the data and resources for this project.

🌟 Star the repository if you found this helpful!

