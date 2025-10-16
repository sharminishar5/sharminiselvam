import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="Tutorial 3 – Visual Analytics of Netflix by Sharmini", layout="wide")

# --- Title section ---
st.title("🎬 Tutorial 3 – Visual Analytics of Netflix by Sharmini")

# --- 1️⃣ Movies vs TV Shows ---
st.subheader("1️⃣ Comparison of Movies and TV Shows on Netflix")
st.image("vis1_movies_vs_tvshows.png", use_container_width=True)
st.info("""
This visualization highlights the noticeable difference between the number of movies and TV shows available on Netflix. Movies dominate the platform’s content library, reflecting Netflix’s focus on film production and licensing. Although TV shows are becoming increasingly popular, movies continue to serve as the foundation of Netflix’s global entertainment offerings, providing a balance between shorter viewing experiences and long-form storytelling.
""")

# --- 2️⃣ Top 10 Countries ---
st.subheader("2️⃣ Top 10 Countries with the Most Netflix Titles")
st.image("vis2_top_countries.png", use_container_width=True)
st.info("""
The top contributors to Netflix’s content are the United States, India, and the United Kingdom, revealing the company’s reliance on countries with strong entertainment industries. This distribution also demonstrates Netflix’s efforts to diversify its catalog by including titles from multiple regions, promoting cultural representation and attracting global audiences through multilingual and cross-cultural content.
""")

# --- 3️⃣ Yearly Release Trend ---
st.subheader("3️⃣ Trend of Content Releases Over the Years")
st.image("vis3_releases_trend.png", use_container_width=True)
st.info("""
The chart shows a clear upward trend in Netflix content releases, especially after 2015, when the platform began heavily investing in original productions. This growth aligns with the global shift toward digital streaming and increasing demand for on-demand entertainment. The trend highlights Netflix’s evolution from a DVD rental service to a global leader in the streaming industry, driven by technological innovation and audience expansion.
""")

# --- 4️⃣ Top Genres ---
st.subheader("4️⃣ Top 10 Genres on Netflix")
st.image("vis4_top_genres.png", use_container_width=True)
st.info("""
The analysis reveals that dramas, comedies, and action titles dominate Netflix’s content catalog. This genre distribution reflects the company’s understanding of audience preferences for emotionally engaging, entertaining, and high-energy storytelling. By maintaining a strong mix of popular genres, Netflix ensures inclusivity and continues to appeal to diverse viewer interests across different age groups and cultural backgrounds.
""")

# --- 5️⃣ Movie Duration Distribution ---
st.subheader("5️⃣ Distribution of Movie Durations on Netflix")
st.image("vis5_duration_dist.png", use_container_width=True)
st.info("""
Most Netflix movies fall within the 80 to 120-minute range, which aligns with the standard feature-length film duration preferred by audiences. This consistency suggests that Netflix curates its movie collection to fit typical viewer attention spans and streaming habits, ensuring comfort and satisfaction. The balance of short and long-form content supports both casual and dedicated viewing experiences.
""")

# --- Footer ---
st.markdown("---")
st.caption("© Sharmini | Tutorial 3 – Visual Analytics of Netflix")
