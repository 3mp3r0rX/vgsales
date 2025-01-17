import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('updated_video_game_sales.csv')

st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")


st.sidebar.header("Filters")
genre = st.sidebar.selectbox('Genre', ['All'] + list(data['Genre'].unique()), index=0)
platform = st.sidebar.selectbox('Platform', ['All'] + list(data['Platform'].unique()), index=0)
year_range = st.sidebar.slider(
    'Year Range',
    int(data['Year'].min()),
    int(data['Year'].max()),
    (int(data['Year'].min()), int(data['Year'].max()))
)

# Filter the data
filtered_data = data.copy()
if genre != 'All':
    filtered_data = filtered_data[filtered_data['Genre'] == genre]
if platform != 'All':
    filtered_data = filtered_data[filtered_data['Platform'] == platform]
filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])]

# Main layout
st.title("🎮 Video Game Sales Dashboard")
st.markdown(
    """
    Welcome to the **Video Game Sales Dashboard**!  
    Use the filters in the sidebar to explore the sales data of video games across genres, platforms, and regions.
    """
)

st.markdown("---")

# Row 1: Summary statistics
st.subheader("📊 Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Games", len(filtered_data))
col2.metric("Total Sales (Global)", f"{filtered_data['GlobalSales'].sum():.2f}M")
col3.metric("Average Sales per Game", f"{filtered_data['GlobalSales'].mean():.2f}M" if len(filtered_data) > 0 else "N/A")

# Row 2: Visualizations - Global Sales by Year and Sales by Region
st.markdown("### 📈 Sales Trends")
col1, col2 = st.columns(2)

# Global Sales Over Years
with col1:
    fig_global = px.bar(
        filtered_data,
        x='Year',
        y='GlobalSales',
        title='Global Sales Over Years',
        color='Genre',
        labels={'GlobalSales': 'Global Sales (M)', 'Year': 'Year'},
        barmode='group'
    )
    st.plotly_chart(fig_global, use_container_width=True)

# Sales by Region Over Time
with col2:
    regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    fig_regions = px.line(
        filtered_data,
        x='Year',
        y=regions,
        title='Sales by Region Over Time',
        markers=True,
        labels={'value': 'Sales (M)', 'variable': 'Region', 'Year': 'Year'}
    )
    st.plotly_chart(fig_regions, use_container_width=True)

# Row 3: Top Publishers and Platform Market Share
st.markdown("### 🏆 Market Insights")
col1, col2 = st.columns(2)

# Top Publishers
with col1:
    top_publishers = filtered_data.groupby('Publisher')['GlobalSales'].sum().nlargest(10).reset_index()
    fig_publishers = px.bar(
        top_publishers,
        x='Publisher',
        y='GlobalSales',
        title='Top 10 Publishers by Global Sales',
        color='GlobalSales',
        labels={'GlobalSales': 'Global Sales (M)', 'Publisher': 'Publisher'}
    )
    st.plotly_chart(fig_publishers, use_container_width=True)

# Platform Market Share
with col2:
    platform_sales = filtered_data.groupby('Platform')['GlobalSales'].sum().reset_index()
    fig_platform = px.pie(
        platform_sales,
        names='Platform',
        values='GlobalSales',
        title='Platform Market Share (Global Sales)',
        hole=0.4
    )
    st.plotly_chart(fig_platform, use_container_width=True)

# Row 4: Genre Market Share and Top Games
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
        hole=0.4
    )
    st.plotly_chart(fig_genre, use_container_width=True)

# Top Games
with col2:
    st.markdown("#### Top 10 Games by Global Sales")
    top_games = filtered_data.nlargest(10, 'GlobalSales')[['Name', 'Platform', 'Genre', 'Publisher', 'Year', 'GlobalSales']]
    st.dataframe(top_games, use_container_width=True)

# Row 5: Sales Correlation Heatmap
st.markdown("### 🔍 Advanced Analysis")
st.subheader("Sales Correlation Heatmap")
correlation_data = filtered_data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'GlobalSales']].corr()
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Row 6: Player Demographics
st.markdown("### 🧑‍🤝‍🧑 Player Demographics")
if 'player_demographic' in filtered_data.columns:
    col1, col2 = st.columns(2)

    # Demographics Distribution
    with col1:
        demographic_counts = filtered_data['player_demographic'].value_counts().reset_index()
        demographic_counts.columns = ['Demographic', 'Count']
        fig_demographics = px.bar(
            demographic_counts,
            x='Demographic',
            y='Count',
            title='Player Demographics Distribution',
            color='Count',
            labels={'Demographic': 'Player Demographic', 'Count': 'Count'}
        )
        st.plotly_chart(fig_demographics, use_container_width=True)

    # Demographics Pie Chart
    with col2:
        fig_demographics_pie = px.pie(
            demographic_counts,
            names='Demographic',
            values='Count',
            title='Player Demographics Breakdown',
            hole=0.4
        )
        st.plotly_chart(fig_demographics_pie, use_container_width=True)
else:
    st.warning("No `player_demographic` data available in the dataset.")

st.markdown("---")
st.markdown("💡 **Tip**: Use the filters in the sidebar to explore specific subsets of the data.")
st.markdown(
    """
    <Footer style="text-align: center; font-size: 18px;">
        Create with ❤️ by Majed El-Naser
    </Footer>
    """,
    unsafe_allow_html=True
)
