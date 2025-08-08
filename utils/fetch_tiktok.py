"""
Enhanced TikTok Comment Fetcher with Real-Time Simulation
This module provides realistic API simulation for portfolio demonstration.
"""

import pandas as pd
import requests
import json
import time
import random
import streamlit as st
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional

class TikTokCommentFetcher:
    """
    Enhanced TikTok comment fetcher with real-time simulation capabilities.
    Perfect for portfolio demonstrations with realistic API behavior.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the enhanced TikTok comment fetcher."""
        self.api_key = api_key or "demo_api_key_12345"
        self.base_url = "https://api.tiktok.com/v1/"
        self.session = requests.Session()
        
        # Enhanced realistic comments database
        self.realistic_comments = [
            # Positive comments (40%)
            "This is amazing! Love it! 😍", "Absolutely fantastic work! 🔥", 
            "Great job on this video!", "Really creative and fun! ✨",
            "Perfect content, keep it up! 👌", "So good! More please! 🙏",
            "This made my day! 😊", "Incredible skills! 💯",
            "Best video I've seen today! 🌟", "You're so talented! 🎨",
            "Outstanding work! 👏", "Love your creativity! 🎭",
            "This deserves more views! 📈", "Amazing as always! ⭐",
            "Can't stop watching this! 🔁", "You inspire me! ✨",
            
            # Neutral comments (35%)
            "Not really my style but okay", "Pretty good content, keep it up!",
            "Meh, could be better", "It's alright I guess", 
            "Interesting concept", "Thanks for sharing",
            "Good effort", "Nice try", "Could use some work",
            "Decent video", "Not bad", "Fair enough",
            "I've seen better", "It's okay", "Average content",
            
            # Negative comments (25%)
            "Terrible video, waste of time", "I don't like this at all",
            "This is boring and pointless", "Not impressed 😒",
            "Skip this one", "Not worth watching", "Disappointing",
            "Could be much better", "Not my thing", "Needs improvement",
            "Boring content", "Don't like it", "Waste of time"
        ]
        
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def fetch_comments_realtime(self, video_url: str, max_comments: int = 50) -> List[Dict]:
        """
        Enhanced real-time comment fetching with progress simulation.
        Perfect for live portfolio demonstrations.
        """
        st.info("🚀 **Live API Demo Mode**: Simulating real TikTok API calls for portfolio demonstration")
        
        # Step 1: API Authentication
        with st.status("🔐 Authenticating with TikTok API...", expanded=True) as status:
            st.write("→ Validating API credentials...")
            time.sleep(0.8)
            st.write("→ Checking rate limits...")
            time.sleep(0.5)
            st.write("✅ Authentication successful!")
            time.sleep(0.3)
            
        # Step 2: Video Analysis
        with st.status("📹 Analyzing video content...", expanded=True) as status:
            st.write(f"→ Processing URL: {video_url}")
            time.sleep(0.7)
            video_info = self.get_enhanced_video_info(video_url)
            st.write(f"→ Video ID: {video_info['video_id']}")
            st.write(f"→ Author: {video_info['author']}")
            st.write(f"✅ Found video with {video_info['view_count']:,} views")
            time.sleep(0.5)
            
        # Step 3: Real-time Comment Streaming
        st.subheader("💬 Live Comment Stream")
        
        comments = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        comment_container = st.container()
        
        # Simulate realistic batch processing
        batch_size = 8
        batches = (max_comments + batch_size - 1) // batch_size
        
        for batch in range(batches):
            batch_start = batch * batch_size
            batch_end = min((batch + 1) * batch_size, max_comments)
            
            status_text.text(f"🔄 Streaming batch {batch+1}/{batches} (comments {batch_start + 1}-{batch_end})...")
            
            # Simulate realistic API delay
            time.sleep(random.uniform(0.5, 1.2))
            
            # Generate batch of realistic comments
            batch_comments = []
            for i in range(batch_start, batch_end):
                comment_text = random.choice(self.realistic_comments)
                
                # Add realistic variation
                if random.random() < 0.3:  # 30% chance to add emojis
                    emojis = ["❤️", "😂", "🔥", "👍", "😍", "💯", "✨", "👏"]
                    comment_text += f" {random.choice(emojis)}"
                
                comment = {
                    "comment_id": f"live_{i+1}_{random.randint(1000, 9999)}",
                    "comment_text": comment_text,
                    "username": f"@{random.choice(['tiktok', 'user', 'fan', 'creator', 'viewer'])}_{random.randint(100, 9999)}",
                    "timestamp": (datetime.now() - timedelta(
                        hours=random.randint(1, 72),
                        minutes=random.randint(0, 59)
                    )).isoformat(),
                    "likes": random.randint(0, 500),
                    "replies": random.randint(0, 25),
                    "is_verified": random.random() < 0.05  # 5% verified users
                }
                comments.append(comment)
                batch_comments.append(comment)
            
            # Show live comments as they stream in
            with comment_container:
                for comment in batch_comments[-3:]:  # Show last 3 comments
                    verified_badge = "✓" if comment.get('is_verified') else ""
                    st.write(f"**{comment['username']}{verified_badge}**: {comment['comment_text']}")
            
            # Update progress
            progress = (batch + 1) / batches
            progress_bar.progress(progress)
            
        status_text.text(f"✅ Successfully streamed {len(comments)} live comments!")
        
        # Final summary
        st.success(f"🎉 **Live fetch complete!** Collected {len(comments)} comments in real-time")
        
        return comments
    
    def get_enhanced_video_info(self, video_url: str) -> Dict:
        """Generate enhanced realistic video metadata"""
        video_titles = [
            "Amazing Dance Challenge 💃",
            "Cooking Hack You Need to Try! 👨‍🍳", 
            "Life Advice That Changed Everything 💭",
            "Funny Pet Moments Compilation 🐕",
            "DIY Home Project Tutorial 🔨",
            "Travel Destination Review ✈️",
            "Fashion Trend Alert! 👗",
            "Tech Review: Is It Worth It? 📱",
            "Fitness Motivation Monday 💪",
            "Art Process Timelapse 🎨"
        ]
        
        creators = [
            "@creativedancer", "@kitchenhacks", "@lifeguru", 
            "@petlover", "@diyqueen", "@worldtraveler",
            "@fashionista", "@techreviewer", "@fitcoach", "@artist"
        ]
        
        return {
            "video_id": f"enhanced_demo_{random.randint(100000, 999999)}",
            "title": random.choice(video_titles),
            "author": random.choice(creators),
            "view_count": random.randint(100000, 5000000),
            "like_count": random.randint(10000, 500000),
            "share_count": random.randint(1000, 50000),
            "comment_count": random.randint(500, 10000),
            "upload_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
            "duration": random.randint(15, 180),  # seconds
            "hashtags": random.sample(["#fyp", "#viral", "#trending", "#foryou", "#tiktok"], 3)
        }
    
    def fetch_video_comments(self, video_id: str, limit: int = 100) -> List[Dict]:
        """Standard comment fetching (backwards compatible)"""
        comments = []
        
        try:
            self.logger.info(f"Fetching comments for video: {video_id}")
            time.sleep(1)
            
            mock_comments = self._generate_mock_comments(video_id, limit)
            comments.extend(mock_comments)
            
            self.logger.info(f"Successfully fetched {len(comments)} comments")
            
        except Exception as e:
            self.logger.error(f"Error fetching comments: {str(e)}")
            
        return comments
    
    def _generate_mock_comments(self, video_id: str, limit: int) -> List[Dict]:
        """
        Generate mock comment data for testing purposes.
        
        Args:
            video_id: Video ID
            limit: Number of mock comments to generate
            
        Returns:
            List of mock comment dictionaries
        """
        mock_comments = [
            "This is amazing! Love it! 😍",
            "Not my favorite content tbh",
            "So funny! Can't stop watching 😂",
            "This is boring 😴",
            "Best video ever! Keep it up! 🔥",
            "Could be better",
            "Amazing content as always! 👏",
            "Meh, not impressed",
            "Love your style! ✨",
            "This made my day! 🌟",
            "Absolutely incredible work!",
            "I don't like this at all",
            "Pretty good video",
            "Outstanding! More please! 🙌",
            "Waste of time",
            "Creative and fun! 🎨",
            "Not bad, could improve",
            "Fantastic job! 💯",
            "Boring content",
            "Love the creativity! 🎭"
        ]
        
        comments = []
        for i in range(min(limit, len(mock_comments))):
            comment = {
                'comment_id': f"comment_{video_id}_{i+1}",
                'username': f"user{i+1}",
                'comment_text': mock_comments[i],
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'video_id': video_id,
                'likes': 0,  # Mock data
                'replies': 0  # Mock data
            }
            comments.append(comment)
            
        return comments
    
    def search_videos_by_hashtag(self, hashtag: str, limit: int = 50) -> List[str]:
        """
        Search for video IDs by hashtag.
        
        Args:
            hashtag: Hashtag to search for (without #)
            limit: Maximum number of videos to return
            
        Returns:
            List of video IDs
        """
        try:
            self.logger.info(f"Searching videos for hashtag: #{hashtag}")
            
            # Mock implementation - return sample video IDs
            video_ids = [f"video_{hashtag}_{i}" for i in range(1, min(limit, 10) + 1)]
            
            self.logger.info(f"Found {len(video_ids)} videos")
            return video_ids
            
        except Exception as e:
            self.logger.error(f"Error searching videos: {str(e)}")
            return []
    
    def fetch_comments_batch(self, video_ids: List[str], comments_per_video: int = 50) -> pd.DataFrame:
        """
        Fetch comments for multiple videos in batch.
        
        Args:
            video_ids: List of video IDs
            comments_per_video: Number of comments to fetch per video
            
        Returns:
            DataFrame containing all comments
        """
        all_comments = []
        
        for video_id in video_ids:
            self.logger.info(f"Processing video: {video_id}")
            comments = self.fetch_video_comments(video_id, comments_per_video)
            all_comments.extend(comments)
            
            # Add delay to avoid rate limiting
            time.sleep(0.5)
        
        df = pd.DataFrame(all_comments)
        
        if not df.empty:
            # Convert timestamp to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
        self.logger.info(f"Total comments collected: {len(df)}")
        return df
    
    def save_comments_to_csv(self, comments_df: pd.DataFrame, filename: str):
        """
        Save comments DataFrame to CSV file.
        
        Args:
            comments_df: DataFrame containing comments
            filename: Output filename
        """
        try:
            comments_df.to_csv(filename, index=False)
            self.logger.info(f"Comments saved to {filename}")
        except Exception as e:
            self.logger.error(f"Error saving comments: {str(e)}")

def main():
    """
    Example usage of TikTokCommentFetcher
    """
    # Initialize fetcher
    fetcher = TikTokCommentFetcher()
    
    # Example 1: Fetch comments for a single video
    video_id = "example_video_123"
    comments = fetcher.fetch_video_comments(video_id, limit=20)
    
    # Example 2: Search videos by hashtag and fetch comments
    hashtag = "funny"
    video_ids = fetcher.search_videos_by_hashtag(hashtag, limit=5)
    
    # Example 3: Batch fetch comments
    if video_ids:
        comments_df = fetcher.fetch_comments_batch(video_ids, comments_per_video=10)
        
        # Save to CSV
        output_file = "../data/fetched_comments.csv"
        fetcher.save_comments_to_csv(comments_df, output_file)
        
        print(f"Fetched {len(comments_df)} comments and saved to {output_file}")

if __name__ == "__main__":
    main()
