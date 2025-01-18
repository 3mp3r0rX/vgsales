import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv('curated_video_game_sales.csv')

# Page Configuration
st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .stButton button {
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    footer {
        text-align: center;
        font-size: 14px;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Filters
st.sidebar.header("Filters")
with st.sidebar.expander("Filter by Genre and Platform"):
    genre = st.sidebar.selectbox("Genre", ["All"] + list(data['Genre'].unique()), index=0, help="Filter games by genre.")
    platform = st.sidebar.selectbox("Platform", ["All"] + list(data['Platform'].unique()), index=0, help="Filter games by platform.")

with st.sidebar.expander("Filter by Year Range"):
    year_filter = st.sidebar.radio(
        "Year Range",
        ["All Years", "1980–1989", "1990–1999", "2000–2009", "2010–2020"],
        index=0,
        help="Filter games by release year range."
    )

with st.sidebar.expander("Filter by Region-Specific Sales"):
    region_sales = st.sidebar.multiselect(
        "Region-Specific Sales",
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "GlobalSales"],
        default=["GlobalSales"],
        help="Select regions to analyze sales trends."
    )

# Filter Data
filtered_data = data.copy()

if genre != "All":
    filtered_data = filtered_data[filtered_data['Genre'] == genre]

if platform != "All":
    filtered_data = filtered_data[filtered_data['Platform'] == platform]

if year_filter != "All Years":
    start_year, end_year = map(int, year_filter.split("–"))
    filtered_data = filtered_data[
        (filtered_data['Year'] >= start_year) & (filtered_data['Year'] <= end_year)
    ]

# Handle Empty Data
if len(filtered_data) == 0:
    st.warning("No data found for the selected filters. Please adjust your filters and try again.")
    st.stop()

# Download Filtered Data
st.sidebar.markdown("---")
st.sidebar.markdown("### Download Filtered Data")
csv = filtered_data.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_video_game_sales.csv",
    mime="text/csv",
    help="Download the filtered dataset as a CSV file."
)

# Main Page
st.title("🎮 Video Game Sales Dashboard")
st.markdown(
    """
    Hello, My name is **Majed El-Naser**, and welcome to the **Video Game Sales Dashboard**! 🎮  
    This interactive dashboard is designed to provide comprehensive insights into global video game sales trends.  
    You can explore data by **genre**, **platform**, **year range**, and **regional sales** using advanced filters.  

    ### About This Project:
    - **Purpose**: Analyze video game sales data to uncover market trends, top-performing games, and regional dynamics.  
    - **Features**:
      - Advanced filtering options for in-depth data exploration.  
      - Interactive visualizations for regional trends, decade analysis, and genre-platform performance.  
      - Insights into top-performing games, publishers, and platforms.  
    - **Data**: The dataset includes sales figures across major regions:  
      - North America  
      - Europe  
      - Japan  
      - Other Regions  

    Whether you're a gamer, a data enthusiast, or someone interested in the gaming industry, this dashboard is for you!  
    ---
    """
)
st.markdown("---")

# Summary Statistics
st.subheader("📊 Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Games", len(filtered_data))
col2.metric("Total Sales (Selected Regions)", f"{filtered_data[region_sales].sum().sum():.2f}M")
col3.metric("Average Sales per Game", f"{filtered_data['GlobalSales'].mean():.2f}M" if len(filtered_data) > 0 else "N/A")

st.markdown("---")

# Sales Trends: Stacked Area Chart
st.subheader("📈 Sales Trends by Region")
if len(region_sales) > 0:
    with st.spinner("Loading sales trends..."):
        fig_sales_trends = px.area(
            filtered_data,
            x="Year",
            y=region_sales,
            title="Sales Trends by Region",
            labels={"value": "Sales (M)", "variable": "Region", "Year": "Year"},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_sales_trends, use_container_width=True)
else:
    st.warning("Please select at least one region to view trends.")

st.markdown("---")

# Market Insights
st.subheader("🔍 Market Insights")
col4, col5 = st.columns(2)

# Top Publishers by Sales
with col4:
    top_publishers = filtered_data.groupby('Publisher')['GlobalSales'].sum().nlargest(10).reset_index()
    fig_publishers = px.bar(
        top_publishers,
        x='Publisher',
        y='GlobalSales',
        title='Top 10 Publishers by Global Sales',
        color='GlobalSales',
        labels={'GlobalSales': 'Global Sales (M)', 'Publisher': 'Publisher'},
        color_continuous_scale=px.colors.sequential.Plasma
    )
    st.plotly_chart(fig_publishers, use_container_width=True)

# Platform Market Share
with col5:
    platform_sales = filtered_data.groupby('Platform')['GlobalSales'].sum().reset_index()
    fig_platform = px.pie(
        platform_sales,
        names='Platform',
        values='GlobalSales',
        title='Platform Market Share (Global Sales)',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_platform, use_container_width=True)

st.markdown("---")

# Player Demographics (Mock Data Example)
st.subheader("👥 Player Demographics and Sales Trends")
demographics = pd.DataFrame({
    "Age Group": ["<18", "18-24", "25-34", "35-44", "45+"],
    "Action": [10, 30, 40, 15, 5],
    "RPG": [5, 25, 45, 20, 5],
    "Sports": [20, 35, 30, 10, 5],
    "Shooter": [15, 40, 35, 8, 2],
})
demographics = demographics.set_index("Age Group")
fig_demographics = px.bar(
    demographics,
    barmode='group',
    title="Player Demographics by Genre",
    labels={"value": "Percentage", "variable": "Genre"},
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_demographics, use_container_width=True)

st.markdown("---")

# Game-Specific Insights
st.markdown("### 🎮 Game-Specific Insights")
col1, col2 = st.columns(2)

# Genre Market Share
with col1:
    genre_sales = filtered_data.groupby('Genre')['GlobalSales'].sum().reset_index()
    fig_genre = px.pie(
        genre_sales,
        names='Genre',
        values='GlobalSales',
        title='Genre Market Share (Global Sales)',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_genre, use_container_width=True)

# Top Games
with col2:
    st.markdown("#### Top 10 Games by Global Sales")
    top_games = filtered_data.nlargest(10, 'GlobalSales')[['Name', 'Platform', 'Genre', 'Publisher', 'Year', 'GlobalSales']]
    st.dataframe(top_games, use_container_width=True)

st.markdown("---")

# Heatmap for Correlations
st.subheader("📊 Regional Sales Correlation")
correlation_data = filtered_data[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "GlobalSales"]].corr()
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.markdown("---")

# Footer
st.markdown(
    """
    <footer>
    Created with ❤️ by <strong>Majed El-Naser</strong> |  
    Follow me on <a href="https://www.linkedin.com/in/majedel-naser/" target="_blank">LinkedIn</a> and <a href="https://github.com/3mp3r0rX" target="_blank">GitHub</a>
    </footer>
    """,
    unsafe_allow_html=True
)