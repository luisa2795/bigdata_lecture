import streamlit as st
import pandas as pd
import altair as alt 
import numpy as np


gap_data=pd.read_csv(r'tidy_df.csv')

year_sel=st.slider('Select Year: ', min_value=1990, max_value=2019, step=1, value=2010)
country_sel=st.multiselect('Select country: ', options=gap_data['country'].unique()) 


c = alt.Chart(gap_data[(gap_data['year']==year_sel) & (gap_data['country'].isin(country_sel))]).mark_circle().encode(
    x=alt.X('GNI_per_cap', scale= alt.Scale(type='log', domain=[200,133000]), 
    axis=alt.Axis(format='$', title='Gross Natition Income (GNI) per captia (PPP)')),
    y=alt.Y('life_expectancy', axis=alt.Axis(title='life expectancy'), scale=alt.Scale(domain=[5,90])),
    size='population', color='country', tooltip='country')

st.altair_chart(c, use_container_width=True)