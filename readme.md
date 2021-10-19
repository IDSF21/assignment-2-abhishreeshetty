# Interactive Data Science Project

## Project Goals
1. Inspect STEM salary data for any prominent wage gap between genders and observe this trend across STEM job titles<br />
3. Compare salaries of a Data Scientist role to other STEM roles<br />
4. Analyse the trend of salaries across different states in US<br />

## Dataset
The dataset used for this project is from Kaggle - [Source Link](https://www.kaggle.com/jackogozaly/data-science-and-stem-salaries). It contains 62,000 salary records of STEM salaries from top companies. This data was scraped off levels.fyi and records range from the Year 2017 to 2021.


## Questions addressed in this project
### Question 1: Is there a prominent wage gap between genders in STEM Jobs? Does this trend vary for different job titles?
Inferences from the visualizations - There is no prominent wage gap between Males and Females in the dataset provided. As this dataset represents salary data from the year 2017 to 2021 which is very recent, it could mean that the wage gap that existed earlier has gotten better over time However, 'other' gender category salary in STEM jobs is alarmingly low for Data Scientist and Software Engineering Manager roles. The dataset does not mention if 'Other' refers to non-binary gender roles or the values where gender remains unspecified. Since the total count of 'Other' is considerably lower compared to Male & Female, we cannot make an inference. But, a more important thing to note is that, although the wage gap between genders doesn't seem to exist, the overall representation of 'women' and 'other' in stem jobs is still lower compared to men which is a metter of concern. 

### Question 2: How does the salary of STEM jobs vary in top 10 states of US? Does this trend vary differently for a Data Scientist job in comparison to other jobs?
Inferences from the visualizations - Across different job roles, salaries offered in states like California, Washington, Massachusetts, and New York is on a higher end. Whereas, states like DC, Georgia, Texas, and Pennsylvania salaries are comparatively on a lower end. This directly correlates to the cost of living and expenses for these states. Dataset here does not indicate any noteworthy difference in the trends across states based on job roles in comparison with Data Science Roles. 

## Design Decisions
1. Decision - Box Plot to analysis wage gap between genders and Count plot to analyse the distribution of gender across roles<br />
Reasoning: In order to analyse gender wage gap, I explored bar chart, linegraph, box plots and scatter plots. However, as box plots include the data distribution across 4 quartiles for each categories, this proved to be the best visualization that enabled comparison between roles and genders at a highly granular level. 
In order to analyse gender distribution, I explored pie charts, sunburst plotly charts, histograms and count plots. Sunburst plotly charts was one of the better alternatives for a smaller set of categories. However, in this case, the categories are dynamically rendered based on the user choice from a multi-select list and readability of Sunburst chart was deteriorating with increased number of categories. Hence, I decided to use bar plot for its robustness to varying category size and ability to visualize side by side bars for each categories. 

2. Decision - Employing side by side stacked bar chart for visualizing salary trend of job roles across 10 states in US<br />
Reasoning: I initially explored, stacked bar chart, side-by-side(or grouped) bar chart and box plots for this. As the number of categories were nested with 20 total combinations (10 states * 2 roles), legibility of the information in stacked bar chart and box plots were not as good as that in side-by-side bar chart. Hence, I chose side-by-side bar chart which helps analyse trend between the roles as well as across countries. 

3. Decision - Limiting top 10 states in US for location trend analysis<br />
Reasoning: While the dataset comprised of salaries from countries other than the US, the currency used for salary remained unspecified and the records count for these countries was insignificant in number. Hence, the scope of the location analysis in this project is limited to the states within the US alone. Top 10 states were chosen based on states with most number of salary records in this dataset. 

3. Decision - Limiting filter values in the interactive components of the website to a subset of job titles<br />
Reasoning: The dataset had 15 distinct roles, however records were limited for most of them to enable a compehensive visualization. Hence, only those roles representative of overall data and with significant salary records have been chosen.

## Development Process
I worked solo on this project. I spent close to 15 people-hours in total that comprised of tasks from figuring out the dataset, performing exploratory data analysis to publishing the visualizations to the website and writing project report. <br />
Performing exploratory data analysis in order to understand the data and to be able to come up with compelling questions that the visualizations can answer took the most time. Selection of dataset alone took some time as well since I was aiming to find a newer datasets with fewer to no visualizations online that could help me come up with novel questions. I looked into recently published datasets on Kaggle to choose the dataset that fit my intentions. Streamlit is a well documented tool with high ease-of-access, hence, learning to use streamlit and publishing the script was an easy and interesting part of this project. 
