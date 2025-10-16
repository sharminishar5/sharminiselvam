import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="Tutorial 3 – Visual Analytics of Netflix by Sharmini", layout="wide")

# --- Title section ---
st.title("🎬 Tutorial 3 – Visual Analytics of Netflix by Sharmini")
st.markdown("""
Welcome to my interactive **Netflix Data Visualization Dashboard**.  
This app presents analytical insights from Netflix’s content data using five meaningful visualizations,  
each supported with concise interpretations for better understanding of trends and patterns.
""")

# --- 1️⃣ Movies vs TV Shows ---
st.subheader("1️⃣ Comparison of Movies and TV Shows on Netflix")
st.image("vis1_movies_vs_tvshows.png", use_container_width=True)
st.info("""
**Interpretation:**  
This visualization highlights the significant difference between the number of movies and TV shows on Netflix.  
Movies dominate the platform’s content library, showing Netflix’s ongoing emphasis on film production and licensing.  
Although TV shows have grown in popularity, movies remain the foundation of Netflix’s global entertainment catalog.  
This reflects a strategic balance between shorter viewing experiences and long-form storytelling.
""")

# --- 2️⃣ Top 10 Countries ---
st.subheader("2️⃣ Top 10 Countries with the Most Netflix Titles")
st.image("vis2_top_countries.png", use_container_width=True)
st.info("""
**Interpretation:**  
The top contributors of Netflix content are the United States, India, and the United Kingdom.  
This pattern reveals Netflix’s heavy reliance on these regions due to their strong entertainment industries.  
It also illustrates how Netflix expands cultural diversity by incorporating titles from various parts of the world.  
Such variety allows Netflix to attract global audiences and cater to multilingual preferences.
""")

# --- 3️⃣ Yearly Release Trend ---
st.subheader("3️⃣ Trend of Content Releases Over the Years")
st.image("vis3_releases_trend.png", use_container_width=True)
st.info("""
**Interpretation:**  
The upward trend after 2015 marks Netflix’s major shift into original productions and international releases.  
The consistent rise in content output indicates growing user demand and investment in digital streaming.  
This also mirrors Netflix’s transformation from a DVD service to a dominant online entertainment platform.  
The data suggests that Netflix’s expansion strategy successfully aligns with global streaming trends.
""")

# --- 4️⃣ Top Genres ---
st.subheader("4️⃣ Top 10 Genres on Netflix")
st.image("vis4_top_genres.png", use_container_width=True)
st.info("""
**Interpretation:**  
Dramas, comedies, and action genres make up the majority of Netflix’s offerings.  
This reflects the platform’s understanding of audience preferences for emotionally engaging and exciting content.  
By providing a mix of familiar and diverse genres, Netflix ensures inclusivity and sustained viewer interest.  
The dominance of these genres showcases Netflix’s focus on balancing entertainment and storytelling appeal.
""")

# --- 5️⃣ Movie Duration Distribution ---
st.subheader("5️⃣ Distribution of Movie Durations on Netflix")
st.image("vis5_duration_dist.png", use_container_width=True)
st.info("""
**Interpretation:**  
Most Netflix movies fall within the 80–120 minute duration range, typical of standard feature-length films.  
This consistency aligns with general audience attention spans and streaming comfort levels.  
It shows that Netflix maintains optimal content length for flexible, enjoyable viewing experiences.  
Overall, the trend reveals Netflix’s effort to meet both short and long-form entertainment needs efficiently.
""")

# --- Footer ---
st.markdown("---")
st.caption("© Sharmini | Tutorial 3 – Visual Analytics of Netflix")
