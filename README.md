# Space Race Data Collection & Analysis

This project involves collecting real-world data on past space missions through web scraping and analyzing it using Python in a Jupyter Notebook. The dataset is sourced from [NextSpaceFlight](https://nextspaceflight.com/launches/past/), a public site tracking space missions globally.

---

## Project Structure

- `webscraper.py`: Python script that scrapes detailed data on past space launches including organization, date, location, rocket status, mission status, and cost.
- `mission_launches_updated_2025-06-24.csv`: Cleaned and structured dataset saved from the scraping process.
- `Space_Missions_Analysis_(start).ipynb`: Jupyter Notebook for visualizing and analyzing the collected data.
- `requirements.txt`: List of required Python libraries.

---

## Features

- **Web Scraping with BeautifulSoup**: Efficiently navigates multiple pages and extracts detailed mission data.
- **Data Cleaning**: Filters out inconsistent data and handles missing cost values.
- **Exploratory Data Analysis**: Perform statistical and visual analysis using:
  - Matplotlib
  - Seaborn
  - Plotly
  - Pandas

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/space-race-analysis.git
   cd space-race-analysis
   
2. Install the required dependencies:
   ```bash 
   pip install -r requirements.txt
   
3. Run the scraper (optional if CSV already exists):

   The scraping may take several minutes due to the number of pages and requests involved. It is recommended to run the scraper only when the dataset is outdated or you need the most recent data.
   ```bash
   python webscraper.py

5. Open the notebook:
   ```bash
   jupyter notebook Space_Missions_Analysis_(start).ipynb

## Analysis Insights (from Notebook)

- Launch activity trends over time
- Evolution of mission outcomes across different years
- Insights into launch patterns during the Cold War era
- Historical trends in launch costs
- Comparative analysis of organizational success rates
- Launch and failure statistics by country
- ...and more in-depth exploratory insights
