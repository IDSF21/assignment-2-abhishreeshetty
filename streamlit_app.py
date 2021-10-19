import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title('Analyzing salaries of STEM jobs')

@st.cache
def load_data():
    df = pd.read_csv("Levels_Fyi_Salary_Data.csv")
    return df

df1 = load_data()
df = df1.copy()

st.header(' Is there a prominent *wage gap* between genders in *STEM* Jobs?')
st.subheader('Does this trend vary for different job titles?')
titles_chosen = st.multiselect(
   "Choose the job titles that you want to compare",
    ('Software Engineer', 'Data Scientist', 'Hardware Engineer','Product Manager','Software Engineering Manager','Business Analyst','Technical Program Manager','Solution Architect'),
    default=['Software Engineer','Data Scientist'])

genderdf = df[ (df['gender']=='Female') | (df['gender']=='Male') | (df['gender']=='Other')]
genderdf = genderdf[ (genderdf['title'].isin(titles_chosen))]
genderdf = genderdf[ (genderdf['basesalary']<150000)]
ax = px.box(genderdf, x="title", y="basesalary", color="gender", labels = dict(title="Job Title", basesalary='Base Salary', gender='Gender'))
st.plotly_chart(ax)
st.subheader('🔎 Observation')
st.write('There is no prominent wage gap between Males and Females in the dataset provided. As this dataset represents salary data from the year 2017 to 2021 which is very recent, it could mean that the wage gap that existed earlier has gotten better over time. However, \'other\' gender category salary in STEM jobs is alarmingly low for Data Scientist and Software Engineering Manager roles. The dataset does not mention if \'Other\' refers to non-binary gender roles or the values where gender remains unspecified. Since the total count of \'Other\' is considerably lower compared to Male & Female, we cannot make an inference.  But, a more important thing to note is that, although the wage gap between genders doesn\'t seem to exist, the overall representation of \'women\' and \'other\' in stem jobs is still lower compared to men as can be seen in the below count plot.')


gender_proportion_chart = px.histogram(genderdf, x='title', color="gender", barmode='group', labels = dict(title="Job Title", gender='Gender'))
st.plotly_chart(gender_proportion_chart)

### END OF VISUALIZATION #1 ###

st.header('How does the salary of STEM jobs vary in top 10 states of US?')# (CA, WA, NY, TX, MA, PA, GA, DC, NJ)')
st.subheader('Does this trend vary differently for a Data Scientist job in comparison to other jobs?')
df["US State"] = df["location"].apply(lambda x: x.split()[-1])
#top 10 - CA, WA, NY, TX, MA, PA, GA, DC, NJ, because sample set of other countries were very limited & data didn't mention currency details
location_trend_df = df[df["US State"].isin(["CA", "WA", "NY", "TX", "MA", "PA", "GA", "DC", "NJ"])]

role_to_compare = st.selectbox(
   "Choose a role to compare with Data Scientist",
    ('Software Engineer', 'Hardware Engineer','Product Manager','Software Engineering Manager','Business Analyst','Technical Program Manager','Solution Architect'),
)
#default='Software Engineer'

location_trend_role1_df = location_trend_df[location_trend_df["title"]=='Data Scientist'].groupby(by="US State").mean()
y1 = list(location_trend_role1_df.index)
x1 = location_trend_role1_df["totalyearlycompensation"]
location_trend_role2_df = location_trend_df[location_trend_df["title"]==role_to_compare].groupby(by="US State").mean()
y2 = list(location_trend_role2_df.index)
x2 = location_trend_role2_df["totalyearlycompensation"]

layout = go.Layout(
    xaxis=dict(
        title="Top 10 States in US"
    ),
    yaxis=dict(
        title="Total Yearly Compensation"
    ) )

fig = go.Figure(layout=layout, data=[
    go.Bar(name='Data Scientist', x = y1, y = x1),
    go.Bar(name=role_to_compare, x = y2, y = x2)
])
# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(fig)
st.subheader('🔎 Observation')
st.write('Across different job roles, salaries offered in states like California, Washington, Massachusetts, and New York is on the higher end. Whereas, states like DC, Georgia, Texas, and Pennsylvania salaries are comparatively on the lower end. This directly correlates to the cost of living and expenses for these states. Dataset here does not indicate any noteworthy difference in the trends across states based on job roles in comparison with Data Science Roles. ')



st.header('📊 Dataset Reference')

st.write('This dataset has been collected from Kaggle - [Link](https://www.kaggle.com/jackogozaly/data-science-and-stem-salaries). It contains 62,000 salary records of STEM salaries from top companies. This data was scraped off levels.fyi and records range from the Year 2017 to 2021. While the dataset contains salaries from countries other than the US, the currency used for salary remains unspecified and the records count for these countries is limited. Hence, the scope of the location analysis in this project is limited to the states within the US alone. ')
# Will only run once if already cached
if st.checkbox('Click to view the raw data'):
    st.write(df1)
