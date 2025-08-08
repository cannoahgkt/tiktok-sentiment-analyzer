# TikTok Sentiment Analyzer

A comprehensive sentiment analysis tool for TikTok comments built with Python, Streamlit, and NLP techniques. This application demonstrates real-time data processing, interactive visualizations, and modern web deployment practices.

## 🎯 Project Overview

This project provides a complete pipeline for:
- Fetching TikTok comments (mock implementation for demo purposes)
- Preprocessing and cleaning text data
- Performing sentiment analysis using multiple approaches
- Visualizing sentiment patterns and insights
- Deploying a user-friendly Streamlit web application

## 🚀 Features

- **Data Collection**: Mock TikTok comment fetcher with extensible architecture
- **Text Preprocessing**: Comprehensive NLP pipeline with cleaning, tokenization, and lemmatization
- **Sentiment Analysis**: Multiple approaches including TextBlob and machine learning models
- **Interactive Visualizations**: Charts, word clouds, and sentiment distribution plots
- **Web Application**: User-friendly Streamlit interface for real-time analysis
- **Model Training**: Jupyter notebooks for exploratory analysis and model development
- **🔴 Live API Demo**: Real-time simulation for demonstration purposes

## 🚀 Live Demo Features

## 🚀 Live Demo Features

- **🔴 Live API Simulation**: Real-time comment fetching with progress bars
- **📊 Streaming Analytics**: Live sentiment analysis as data loads
- **📈 Professional Visualizations**: Interactive charts and metrics
- **💾 Downloadable Results**: CSV exports for verification
- **🎯 Demo Ready**: Technical demonstration capabilities

## 📡 API Integration Options

### Current Implementation:
- **Mock TikTok API**: Realistic simulation for demonstration purposes
- **Real-time Processing**: Shows how real API integration would work
- **Rate Limiting Simulation**: Professional API handling patterns
- **Error Handling**: Production-ready error management

### For Production (Future Enhancements):
```python
# Alternative APIs that are more accessible:
- YouTube Data API (social media sentiment)
- Twitter API (real-time social sentiment) 
- Reddit API (community sentiment analysis)
- Custom web scraping (with legal compliance)
```

## 🌐 Deployment Options

### Available Deploy Methods:

1. **Streamlit Cloud**:
   ```bash
   # Push to GitHub, then deploy at share.streamlit.io
   git add .
   git commit -m "Deploy to production"
   git push origin main
   ```

2. **Docker Deployment**:
   ```bash
   docker build -t tiktok-sentiment-analyzer .
   docker run -p 8501:8501 tiktok-sentiment-analyzer
   ```

3. **Local Development**:
   ```bash
   docker-compose up
   # App available at http://localhost:8501
   ```

## ⚡ Technical Features
## ⚡ Technical Features

- ✅ **Production-Ready Code**: Clean, documented, and maintainable
- ✅ **Real-time Processing**: Streaming data simulation
- ✅ **Modern Tech Stack**: Python, Streamlit, Docker, NLP
- ✅ **Interactive UI/UX**: Professional, responsive design  
- ✅ **Data Visualization**: Plotly charts and analytics
- ✅ **Containerized**: Docker for consistent deployment

## 🎯 Use Cases
## 🎯 Use Cases

- **Social Media Analytics**: Understanding audience sentiment
- **Content Performance**: Real-time feedback analysis  
- **Data Processing**: Scalable text analysis pipeline
- **Insight Generation**: Actionable sentiment metrics

## 📋 Requirements

- Python 3.8+
- See `requirements.txt` for complete list of dependencies

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd tiktok-sentiment-analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data:**
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"
   ```

## 📁 Project Structure

```
tiktok-sentiment-analyzer/
│
├── app.py                   # Main Streamlit application
│
├── data/                    # TikTok comment data
│   ├── comments.csv         # Sample data
│   └── preprocessed_comments.csv  # Cleaned data (generated)
│
├── model/                   # Trained models
│   └── .gitkeep            # Placeholder for model files
│
├── notebooks/               # Jupyter notebooks
│   └── preprocessing.ipynb  # Data preprocessing and EDA
│
├── utils/                   # Utility functions
│   └── fetch_tiktok.py     # Comment fetcher (mock implementation)
│
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 🎮 Usage

### Running the Web Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

### Using the Jupyter Notebooks

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Open `notebooks/preprocessing.ipynb`** to explore the data preprocessing pipeline

### Using the Comment Fetcher

```python
from utils.fetch_tiktok import TikTokCommentFetcher

# Initialize fetcher
fetcher = TikTokCommentFetcher()

# Fetch comments for a video (mock data)
comments = fetcher.fetch_video_comments("video_id_123", limit=50)

# Batch fetch from multiple videos
video_ids = ["video1", "video2", "video3"]
df = fetcher.fetch_comments_batch(video_ids)
```

## 📊 Analysis Pipeline

1. **Data Collection**: Gather TikTok comments using the fetcher utility
2. **Preprocessing**: Clean and normalize text data
3. **Feature Engineering**: Extract relevant features from comments
4. **Sentiment Analysis**: Apply TextBlob and ML models
5. **Visualization**: Generate insights through charts and graphs
6. **Web Interface**: Present results in an interactive dashboard

## 🔧 Key Components

### Text Preprocessing
- Lowercasing and punctuation removal
- URL and mention filtering
- Stopword removal and lemmatization
- Feature extraction (word count, exclamation marks, etc.)

### Sentiment Analysis Methods
- **TextBlob**: Rule-based sentiment scoring
- **Machine Learning**: Scikit-learn models with TF-IDF features
- **Custom Features**: Engineered features for improved accuracy

### Visualization
- Sentiment distribution charts
- Word clouds by sentiment category
- Polarity vs. subjectivity scatter plots
- Time-series sentiment trends

## 🎯 Applications

This project demonstrates key capabilities in:

- **NLP Processing**: Text cleaning, tokenization, feature engineering
- **Machine Learning**: Classification models, evaluation metrics
- **Data Visualization**: Interactive charts and dashboards
- **Web Development**: Modern application deployment
- **Software Engineering**: Modular architecture and documentation

## 🚧 Future Enhancements

- [ ] Integration with actual TikTok API (when available)
- [ ] Advanced ML models (BERT, RoBERTa)
- [ ] Real-time comment stream processing
- [ ] Database integration for persistent storage
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/GCP/Azure)
- [ ] A/B testing framework for model comparison

## 📈 Performance Metrics

Target performance metrics (to be validated):
- Accuracy: ~85% on test data
- F1-Score: ~0.83 weighted average
- Processing Speed: ~1000 comments/second

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- TextBlob for sentiment analysis capabilities
- Streamlit for the web application framework
- Scikit-learn for machine learning tools
- The open-source community for various NLP libraries

## 📞 Contact

For questions or collaboration opportunities:
- GitHub: [Your GitHub Profile]
- Email: [Your Email]

---

**Note**: This project uses mock TikTok data for demonstration purposes. Integration with actual TikTok APIs would require proper authentication and compliance with TikTok's terms of service.
