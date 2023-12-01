import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
df = pd.read_csv('BreakDataClean.csv')
df.head(1)
df = df.drop('ID', axis=1)

st.title('Analyzing Robotic Fabrication Output')
st.write("This is a summary of statistical output of this data-set")




st.write(df.describe())


Q1 = df.quantile(0.25, numeric_only=True)
Q3 = df.quantile(0.75, numeric_only=True)
IQR = Q3 - Q1
st.write(' ## This represents where *50%* of the data resides')
st.write(IQR)

### Determining number of bins for Histogram Plots

num_bins = int(np.ceil(1+np.log2(len(df))))

def main():
    st.write('<p style="font-size:30px; color:green;">Histogram of OEE</p>',unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df['OEE'], bins=num_bins, kde=True, color='green', label='Efficiency Percentage', ax=ax)
    ax.set_xlabel('OEE')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')
    ax.legend()

    st.pyplot(fig)
    
if __name__ == "__main__":
    main()
    
st.write('<p style="font-size:30px; color:green;">Histogram of UnplannedDowntime</p>',unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(12,6))
sns.histplot(df["UnplannedDowntime"], bins=num_bins, kde=True, color='green')
ax.set_xlabel('UnplannedDowntime')
ax.set_ylabel('Frequency')
ax.legend()
st.pyplot(fig)

st.write('<p style="font-size:30px; color:red;">Histogram of No Status</p>',unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(df['NoStatus'], bins=num_bins, kde=True, color='red')
ax.set_xlabel('NoStatus')
ax.set_ylabel('Frequency')

st.pyplot(fig)
