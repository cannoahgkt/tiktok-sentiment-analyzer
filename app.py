# TikTok Sentiment Analyzer
import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import time
from datetime import datetime
from utils.fetch_tiktok import TikTokCommentFetcher
from typing import Tuple

# Configure Streamlit page
st.set_page_config(
    page_title="TikTok Sentiment Analyzer",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

SIMPLE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Manrope', sans-serif !important;
}

/* Just basic styling, let Streamlit handle dark mode */
div[data-testid="stMetric"] {
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.stButton > button {
    border-radius: 6px;
    font-weight: 500;
}

.stTabs [data-baseweb="tab-list"] {
    border-radius: 6px;
    padding: 0.25rem;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 4px;
    font-weight: 500;
}

details {
    border-radius: 6px;
}

.stDataFrame {
    border-radius: 6px;
}
</style>
"""

def inject_css():
    st.markdown(SIMPLE_CSS, unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def load_data(uploaded_file) -> Tuple[pd.DataFrame, str | None]:
    """Load CSV data."""
    try:
        df = pd.read_csv(uploaded_file)
        return df, None
    except Exception as e:
        return pd.DataFrame(), str(e)

def analyze_sentiment(text: str) -> tuple[float, float, str]:
    """Analyze sentiment of text and return polarity, subjectivity, and classification"""
    try:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        polarity = float(sentiment.polarity)  # type: ignore
        subjectivity = float(sentiment.subjectivity)  # type: ignore
        
        if polarity > 0.1:
            classification = "positive"
        elif polarity < -0.1:
            classification = "negative"
        else:
            classification = "neutral"
            
        return polarity, subjectivity, classification
    except Exception as e:
        st.error(f"Error during sentiment analysis: {e}")
        return 0.0, 0.0, "neutral"

def show_sentiment_charts(df):
    """Display sentiment charts"""
    if 'sentiment' not in df.columns:
        return
        
    col1, col2 = st.columns(2)
    
    with col1:
        sentiment_counts = df['sentiment'].value_counts()
        fig_pie = px.pie(
            values=sentiment_counts.values, 
            names=sentiment_counts.index,
            title="Sentiment Distribution",
            color_discrete_map={
                'positive': '#22c55e',
                'neutral': '#f59e0b', 
                'negative': '#ef4444'
            }
        )
        st.plotly_chart(fig_pie, use_container_width=True, theme="streamlit")
    
    with col2:
        fig_bar = px.bar(
            x=sentiment_counts.index,
            y=sentiment_counts.values,
            title="Sentiment Count",
            color=sentiment_counts.index,
            color_discrete_map={
                'positive': '#22c55e',
                'neutral': '#f59e0b', 
                'negative': '#ef4444'
            }
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True, theme="streamlit")

def show_polarity_chart(df):
    """Display polarity distribution"""
    if 'polarity' not in df.columns:
        return
        
    fig_hist = px.histogram(
        df, 
        x="polarity", 
        nbins=30, 
        title="Polarity Distribution",
        color="sentiment" if 'sentiment' in df.columns else None,
        color_discrete_map={
            'positive': '#22c55e',
            'neutral': '#f59e0b', 
            'negative': '#ef4444'
        }
    )
    st.plotly_chart(fig_hist, use_container_width=True, theme="streamlit")

def show_sample_comments(df):
    """Show sample comments by sentiment"""
    if 'sentiment' not in df.columns:
        return
    
    sentiment_choice = st.selectbox("View comments by sentiment:", ["positive", "neutral", "negative"])
    
    sentiment_data = df[df["sentiment"] == sentiment_choice]
    
    if len(sentiment_data) > 0:
        st.write(f"**{len(sentiment_data)} {sentiment_choice} comments found**")
        
        # Find text column
        text_col = None
        for col in ['comment_text', 'text', 'original_text']:
            if col in df.columns:
                text_col = col
                break
                
        if text_col:
            sample_comments = sentiment_data.head(5)
            for i, (idx, row) in enumerate(sample_comments.iterrows()):
                with st.expander(f"Comment {i+1} (Polarity: {row.get('polarity', 'N/A')})"):
                    st.write(row[text_col])
        else:
            st.warning("No text column found in the data")
    else:
        st.info(f"No {sentiment_choice} comments found")

def generate_wordcloud(df):
    """Generate simple word cloud"""
    # Find text column
    text_col = None
    for col in ['comment_text', 'text', 'original_text', 'cleaned_comment']:
        if col in df.columns:
            text_col = col
            break
    
    if not text_col:
        return None
        
    text_data = ' '.join(df[text_col].dropna().astype(str).tolist())
    if not text_data.strip():
        return None
        
    wordcloud = WordCloud(
        width=800, 
        height=400, 
        background_color='white',
        max_words=100,
        colormap='viridis'
    ).generate(text_data)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return buf

def live_api_demo():
    """Live API demonstration feature for portfolio"""
    st.subheader("🚀 Live TikTok API Demo")
    st.info("**Portfolio Demo**: This simulates real TikTok API calls with realistic data and processing")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        video_url = st.text_input(
            "Enter TikTok Video URL:",
            value="https://www.tiktok.com/@demo/video/1234567890",
            placeholder="https://www.tiktok.com/@username/video/1234567890"
        )
        
        max_comments = st.slider(
            "Number of comments to fetch:",
            min_value=10, 
            max_value=100, 
            value=30,
            help="More comments = more realistic demonstration"
        )
    
    with col2:
        st.markdown("**🎯 Demo Features:**")
        st.write("✅ Real-time API simulation")
        st.write("✅ Progressive data loading")
        st.write("✅ Live sentiment analysis")
        st.write("✅ Realistic comment patterns")
        st.write("✅ Portfolio-ready presentation")
        
    if st.button("🔴 Start Live API Demo", type="primary", use_container_width=True):
        if not video_url or not video_url.startswith("http"):
            st.error("Please enter a valid TikTok URL")
            return
            
        # Initialize fetcher and run live demo
        fetcher = TikTokCommentFetcher()
        
        with st.container():
            # Fetch comments with real-time simulation
            comments = fetcher.fetch_comments_realtime(video_url, max_comments)
            
            if comments:
                # Convert to DataFrame
                df = pd.DataFrame(comments)
                
                # Real-time sentiment analysis
                st.subheader("🧠 Live Sentiment Analysis")
                progress_text = st.empty()
                sentiment_progress = st.progress(0)
                
                sentiments = []
                polarities = []
                
                for i, comment in enumerate(comments):
                    progress_text.text(f"Analyzing comment {i+1}/{len(comments)}...")
                    
                    # Analyze sentiment
                    polarity, subjectivity, sentiment = analyze_sentiment(comment['comment_text'])
                    sentiments.append(sentiment)
                    polarities.append(polarity)
                    
                    # Update progress
                    sentiment_progress.progress((i + 1) / len(comments))
                    
                    # Small delay for realism
                    if i % 5 == 0:  # Every 5th comment
                        time.sleep(0.1)
                
                # Add sentiment data to DataFrame
                df['sentiment'] = sentiments
                df['polarity'] = polarities
                df['subjectivity'] = [analyze_sentiment(text)[1] for text in df['comment_text']]
                
                progress_text.text("✅ Sentiment analysis complete!")
                
                # Show results
                st.success(f"🎉 **Live Analysis Complete!** Processed {len(df)} comments in real-time")
                
                # Quick metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    positive_pct = (df['sentiment'] == 'positive').mean() * 100
                    st.metric("Positive", f"{positive_pct:.1f}%", delta=f"{len(df[df['sentiment']=='positive'])} comments")
                with col2:
                    neutral_pct = (df['sentiment'] == 'neutral').mean() * 100
                    st.metric("Neutral", f"{neutral_pct:.1f}%", delta=f"{len(df[df['sentiment']=='neutral'])} comments")
                with col3:
                    negative_pct = (df['sentiment'] == 'negative').mean() * 100
                    st.metric("Negative", f"{negative_pct:.1f}%", delta=f"{len(df[df['sentiment']=='negative'])} comments")
                with col4:
                    avg_polarity = df['polarity'].mean()
                    st.metric("Avg Polarity", f"{avg_polarity:.3f}", delta="Overall sentiment")
                
                # Show live charts
                st.subheader("📊 Live Results")
                show_sentiment_charts(df)
                
                # Store in session state for download
                st.session_state['live_demo_data'] = df
                
                # Download button
                csv_data = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "💾 Download Live Analysis Results",
                    data=csv_data,
                    file_name=f"live_tiktok_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )

def live_sentiment_analysis():
    """Simple live sentiment analysis"""
    st.subheader("🔍 Live Sentiment Analysis")
    
    user_text = st.text_area(
        "Enter text to analyze:",
        placeholder="Type your comment here...",
        height=100
    )
    
    if user_text and user_text.strip():
        polarity, subjectivity, sentiment = analyze_sentiment(user_text)
        
        # Show results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Sentiment", sentiment.upper())
        with col2:
            st.metric("Polarity", f"{polarity:.3f}")
        with col3:
            st.metric("Subjectivity", f"{subjectivity:.3f}")
        
        # Simple interpretation
        if sentiment == "positive":
            st.success("😊 This text expresses positive sentiment!")
        elif sentiment == "negative":
            st.error("😞 This text expresses negative sentiment!")
        else:
            st.info("😐 This text is neutral.")

def main():
    inject_css()
    
    st.title("📱 TikTok Sentiment Analyzer")
    st.markdown("Analyze sentiment in TikTok comments using TextBlob NLP")
    
    # Simplified sidebar
    with st.sidebar:
        st.header("📂 Upload Data")
        uploaded_file = st.file_uploader(
            "Choose CSV file", 
            type=["csv"],
            help="Upload a CSV file with comment data"
        )
        
        if uploaded_file:
            st.success("File uploaded successfully!")
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Data Analysis", "🚀 Live API Demo", "🔍 Live Analysis", "ℹ️ About"])
    
    with tab1:
        if uploaded_file is not None:
            df, error = load_data(uploaded_file)
            
            if error:
                st.error(f"Error loading file: {error}")
            else:
                st.success(f"✅ Loaded {len(df)} rows of data")
                
                # Basic metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Total Comments", len(df))
                with col2:
                    if 'sentiment' in df.columns:
                        positive_count = len(df[df['sentiment'] == 'positive'])
                        st.metric("Positive", positive_count)
                    else:
                        st.metric("Positive", "N/A")
                with col3:
                    if 'sentiment' in df.columns:
                        negative_count = len(df[df['sentiment'] == 'negative'])
                        st.metric("Negative", negative_count)
                    else:
                        st.metric("Negative", "N/A")
                with col4:
                    if 'sentiment' in df.columns:
                        neutral_count = len(df[df['sentiment'] == 'neutral'])
                        st.metric("Neutral", neutral_count)
                    else:
                        st.metric("Neutral", "N/A")
                
                st.divider()
                
                # Data preview
                with st.expander("📋 Data Preview", expanded=True):
                    st.dataframe(df.head(10), use_container_width=True)
                
                # Charts
                if 'sentiment' in df.columns:
                    st.subheader("📊 Sentiment Analysis")
                    show_sentiment_charts(df)
                    
                    if 'polarity' in df.columns:
                        st.subheader("📈 Polarity Distribution")
                        show_polarity_chart(df)
                    
                    # Sample comments
                    st.subheader("💬 Sample Comments")
                    show_sample_comments(df)
                    
                    # Word cloud
                    st.subheader("☁️ Word Cloud")
                    wordcloud_img = generate_wordcloud(df)
                    if wordcloud_img:
                        st.image(wordcloud_img, use_column_width=True)
                    else:
                        st.info("Could not generate word cloud - no text data found")
                
                # Download
                st.divider()
                csv_data = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "💾 Download Processed Data",
                    data=csv_data,
                    file_name="sentiment_analysis.csv",
                    mime="text/csv"
                )
        else:
            st.info("👆 Upload a CSV file to get started")
            
            # Show example format
            st.subheader("Expected Data Format")
            example_df = pd.DataFrame({
                'comment_text': ['Great video!', 'Not bad', 'This is terrible'],
                'sentiment': ['positive', 'neutral', 'negative'],
                'polarity': [0.8, 0.0, -0.9]
            })
            st.dataframe(example_df, use_container_width=True)
    
    with tab2:
        live_api_demo()
    
    with tab3:
        live_sentiment_analysis()
    
    with tab4:
        st.markdown("## About This App")
        st.write("""
        This TikTok Sentiment Analyzer helps you understand the emotional tone of comments 
        using Natural Language Processing (NLP).
        
        **Features:**
        - Upload and analyze CSV files with comment data
        - View sentiment distribution and polarity scores
        - Test live sentiment analysis on any text
        - Generate word clouds from comment text
        - Download processed results
        
        **Built with:**
        - Streamlit for the web interface
        - TextBlob for sentiment analysis
        - Plotly for interactive charts
        - WordCloud for text visualization
        
        **How to use:**
        1. Upload a CSV file with your comment data
        2. Explore the visualizations and metrics
        3. Try the live analysis feature with your own text
        """)

if __name__ == "__main__":
    main()
