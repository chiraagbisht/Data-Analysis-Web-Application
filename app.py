import streamlit as st
import pandas as pd
from helper import *
summer,winter=data_preprocessor()
summer,winter=duplicate_rows_removal(summer,winter)
summer.dropna(subset=["region"],inplace=True)
winter.dropna(subset=["region"],inplace=True)
# st.dataframe(summer)
# st.dataframe(winter)
# st.write("Before")
# st.write(summer.shape)
# st.write(winter.shape)

# summer,winter=duplicate_rows_removal(summer,winter)

# st.write("After")
# st.write(summer.shape)
# st.write(winter.shape)

st.sidebar.title("MENU")
season=st.sidebar.radio("Choose season :",("summer","winter"))
options=st.sidebar.radio("Options",("Medal-Tally","Country-Wise","Year-wise","Year-wise Progress"))
### MEDAL TALLY
if season=="summer" and options=="Medal-Tally":
    st.subheader("Summer olympics medal tally")
    medal_pivot_summer=medal_tally_calculator(summer)
    medal_pivot_summer=medal_pivot_summer.sort_values(by=["Gold","Silver","Bronze"],ascending=False)
    st.dataframe(medal_pivot_summer,width=650)

elif season=="winter" and options=="Medal-Tally":
    st.subheader("Winter olympics medal tally")
    medal_pivot_winter=medal_tally_calculator(winter)
    medal_pivot_winter=medal_pivot_winter.sort_values(by=["Gold","Silver","Bronze"],ascending=False)
    st.dataframe(medal_pivot_winter,width=650)

## Country-wise
elif season=="summer" and options=="Country-Wise":
    st.subheader("Summer Olympics Country-wise")
    medal_pivot_summer=medal_tally_calculator(summer)
    noc=st.selectbox("Select NOC: ",medal_pivot_summer.index.tolist())
    details=countrywise_search(noc,medal_pivot_summer)
    table=pd.DataFrame.from_dict(details,orient="index",columns=["Value"])
    st.dataframe(table,width=650)
elif season=="winter" and options=="Country-Wise":
    st.subheader("Winter Olympics Country-wise")
    medal_pivot_winter=medal_tally_calculator(winter)
    noc=st.selectbox("Select NOC: ", medal_pivot_winter.index.tolist())
    details=countrywise_search(noc,medal_pivot_winter)
    table=pd.DataFrame.from_dict(details,orient="index",columns=["Value"])
    st.dataframe(table,width=650)
      ### YEAR WISE
elif season=="summer" and options=="Year-wise":
    st.subheader("Summer Olympics Year-wise")
    years=sorted(summer["Year"].unique())
    selected_year=st.selectbox("Select Year: ",years)
    countries=sorted(summer[summer["Year"]==selected_year]["region"].unique())
    selected_country=st.selectbox("Select Country: ",countries)
    plot_medals(selected_year,selected_country,summer)

elif season=="winter" and options=="Year-wise":
    st.subheader("Summer Olympics Year-wise")
    years=sorted(winter["Year"].unique())
    selected_year=st.selectbox("Select Year: ",years)
    countries=sorted(winter[winter["Year"]==selected_year]["region"].unique())
    selected_country=st.selectbox("Select Country: ",countries)
    plot_medals(selected_year,selected_country,winter)
    ### YEAR WISE PROGRESS
elif season=="summer" and options=="Year-wise Progress":
    st.subheader("OVERALL ANALYSIS OF A COUNTRY")
    countries=sorted(summer["region"].unique())
    selected_country=st.selectbox("Select country:", countries)

    year_analysis(selected_country ,summer)
else:
    st.subheader("OVERALL ANALYSIS OF A COUNTRY")
    countries=sorted(winter["region"].unique())
    selected_country=st.selectbox("Select country:", countries)

    year_analysis(selected_country ,winter)