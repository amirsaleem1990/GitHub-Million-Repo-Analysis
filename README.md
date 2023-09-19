# GitHub-Million-Repo-Analysis

It appears that you have built a Python project for fetching and analyzing GitHub repository metadata using the GitHub Search API. Let's break down your project into its main components:

### _Fetching Script (.fetch-github-repos-data.py)_:
- A Python script responsible for fetching GitHub repository metadata. This script uses the GitHub Search API to  retrieve information about the last one million repositories created. The fetched data is analyzed later in another script.
- The script takes into account rate limiting by handling HTTP status codes like 403 (maximum login attempts exceeded) and - 422 (when you already fetched 1000 items).
- It fetches data for different time periods, divided into hourly intervals, and saves the results in pickle files.

### _Analysis Script (github-repos-basic-analysis.ipynb)_:
- This Jupyter Notebook script is used to analyze the data fetched by the fetching 
- It loads the saved pickle files containing GitHub repository metadata and combines them into a DataFrame.
- It performs various data analysis tasks such as handling duplicates, checking for missing values (NaNs), and exploring the characteristics of the dataset.

- #### The analysis includes:
    - Examining data types of columns
    - Identifying and dropping redundant columns with only one unique value
    - Investigating non-ASCII characters in descriptions
    - Analyzing the distribution of repository creation dates
    - Exploring repository sizes
    - Investigating stargazers and watchers counts
    - Analyzing programming languages used in repositories
    - Examining the presence of issues, projects, wikis, and discussions
    - Investigating default branches, licenses, and owner-related attributes
    - Verifying the relationship between creation and push timestamps

The analysis script generates various visualizations, such as bar charts and heatmaps, to help you understand the data better.

Overall, the project is a comprehensive data analysis for GitHub repositories. It allows to fetch large amounts of data using the GitHub API and gain insights into various aspects of GitHub repositories, such as their characteristics, languages, and user-related attributes. This information can be valuable for making informed decisions and conducting research related to GitHub repositories.

