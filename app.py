import streamlit as st

st.set_page_config(page_title="Tutorial 3 – Netflix Visualizations by Sharmini", layout="wide")

st.title("🎬 Tutorial 3 – Netflix Visualizations by Sharmini")
st.caption("Visualizations created in Google Colab and interpreted here using Streamlit.")

# --- 1️⃣ Movies vs TV Shows ---
st.subheader("1️⃣ Movies vs TV Shows")
st.image("vis1_movies_vs_tvshows.png", use_container_width=True)
st.info("""
**Interpretation:**  
The visualization clearly shows that Netflix hosts a larger number of movies compared to TV shows. 
This suggests that the platform still emphasizes film content as its main offering, even though TV shows are gaining popularity. 
It highlights Netflix’s long-standing commitment to movie production and acquisition while gradually expanding its series portfolio. 
Overall, the dominance of movies reflects viewer demand for short-form entertainment rather than long-term series engagement.
""")

# --- 2️⃣ Top 10 Countries ---
st.subheader("2️⃣ Top 10 Countries with Most Titles")
st.image("vis2_top_countries.png", use_container_width=True)
st.info("""
**Interpretation:**  
The visualization shows that the United States, India, and the United Kingdom contribute the most content to Netflix’s library. 
This pattern reflects the strong entertainment industries in these countries and Netflix’s partnerships with major studios and production houses. 
It also demonstrates how Netflix targets markets with high content diversity and global viewership potential. 
Hence, Netflix’s catalog represents a mix of Western and Asian influences, appealing to a wide international audience.
""")

# --- 3️⃣ Trend of Releases Over Years ---
st.subheader("3️⃣ Trend of Releases Over Years")
st.image("vis3_releases_trend.png", use_container_width=True)
st.info("""
**Interpretation:**  
The trend line indicates a significant increase in the number of titles released after 2015. 
This surge corresponds to Netflix’s rapid global expansion and growing investment in original productions. 
It also reflects technological advancements and shifting consumer preferences toward streaming services. 
In summary, the data shows how Netflix has transformed from a DVD rental service into a leading global entertainment platform.
""")

# --- 4️⃣ Top 10 Genres ---
st.subheader("4️⃣ Top 10 Genres")
st.image("vis4_top_genres.png", use_container_width=True)
st.info("""
**Interpretation:**  
The genre distribution reveals that dramas, comedies, and action movies dominate Netflix’s content catalog. 
This pattern indicates that viewers tend to prefer emotionally engaging and entertaining stories. 
Netflix strategically focuses on these genres to maintain viewer interest and satisfaction across different age groups. 
By offering a variety of content within these genres, Netflix continues to attract diverse audiences worldwide.
""")

# --- 5️⃣ Movie Duration Distribution ---
st.subheader("5️⃣ Distribution of Movie Durations")
st.image("vis5_duration_dist.png", use_container_width=True)
st.info("""
**Interpretation:**  
The histogram shows that most movies on Netflix range between 80 and 120 minutes in duration. 
This duration range aligns with the standard feature-length movie format preferred by audiences. 
It also suggests that Netflix maintains a consistent structure in its movie offerings for convenience and viewer engagement. 
Overall, the data highlights how Netflix balances content length with accessibility for casual and frequent viewers alike.
""")

st.markdown("---")
st.caption("© Sharmini | Tutorial 3 Visualization App")
