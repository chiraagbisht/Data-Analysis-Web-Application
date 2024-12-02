import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

athlete=pd.read_csv("data/athlete_events.csv")
regions=pd.read_csv("data/noc_regions.csv")
def data_preprocessor():
    global athlete,regions 
    df=pd.merge(athlete,regions,on="NOC")
    df.drop_duplicates(inplace=True)
    df["Medal"].fillna("No medal",inplace=True)
    summer=df[df["Season"]=="Summer"]
    winter=df[df["Season"]=="Winter"]
    return summer,winter
def duplicate_rows_removal(df1,df2):
    df1=df1.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event"])
    df2=df2.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event"])
    return df1 ,df2
def medal_tally_calculator(df):
   medal_grouped=df.groupby(["NOC","Medal"]).size().reset_index(name="count")
   medal_pivot=medal_grouped.pivot(index="NOC",columns="Medal",values="count")
   medal_pivot=medal_pivot.astype('Int32')
   if "No Medal" in medal_pivot.columns:
       medal_pivot.drop(columns=["No Medal"],inplace=True)
   medal_pivot["Total Medal"]=medal_pivot[["Gold","Silver","Bronze"]].sum(axis=1)
   return medal_pivot

def countrywise_search(noc,pivot_table):
 if noc in pivot_table.index:
     details={
         "Gold": pivot_table.loc[noc,"Gold"],
         "Silver":pivot_table.loc[noc,"Silver"],
         "Bronze":pivot_table.loc[noc,"Bronze"],
         "Total Medal":pivot_table.loc[noc,"Total Medal"]
     }
     return details
 else:
  print("No NOC exists")
def plot_medals(Year, Country, df):
    medal_count=df.groupby(["Year","region","Medal"]).size().unstack(fill_value=0)
    medal_count=medal_count.reset_index()
    medal_count["Total_Medal"]= medal_count["Gold"]+medal_count["Silver"]+medal_count["Bronze"]
    # Filter the DataFrame for the given year and country
    filtered_df = medal_count[(medal_count["Year"] == Year) & (medal_count["region"] == Country)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        print(f"No data available for Year: {Year} and Country: {Country}.")
        return
    
    # Extract medal counts
    Gold = filtered_df["Gold"].values[0]
    Silver = filtered_df["Silver"].values[0]
    Bronze = filtered_df["Bronze"].values[0]
    Total_Medal = filtered_df["Total_Medal"].values[0]
    
    # Define labels and counts
    medals = ["Gold", "Silver", "Bronze", "Total Medals"]
    counts = [Gold, Silver, Bronze, Total_Medal]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(medals, counts, color=["gold", "silver", "brown", "green"])
    
    # Add titles and labels
    ax.set_title(f"Medal Distribution for {Country} in {Year}")
    ax.set_ylabel("Number of Medals")
    ax.set_xlabel("Medal Type")
    
    # Display the plot
    st.pyplot(fig)

def year_analysis(country, df):
    medal_count=df.groupby(["Year","region","Medal"]).size().unstack(fill_value=0)
    medal_count=medal_count.reset_index()
    medal_count["Total_Medal"]= medal_count["Gold"]+medal_count["Silver"]+medal_count["Bronze"]
    filtered_df=medal_count[medal_count["region"]==country]
    fig, ax = plt.subplots()
    ax.plot(filtered_df["Year"], filtered_df["Gold"], color="gold", label="Gold", marker="o", linestyle="-")
    ax.plot(filtered_df["Year"], filtered_df["Silver"], color="silver", label="Silver", marker="o", linestyle="-")
    ax.plot(filtered_df["Year"], filtered_df["Bronze"], color="brown", label="Bronze", marker="o", linestyle="-")
    ax.plot(filtered_df["Year"], filtered_df["Total_Medal"], color="green", label="Total Medals", marker="o", linestyle="-")
    
    ax.legend()
   
    st.pyplot(fig)
    
   