import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# Sample data for demonstration
data = pd.DataFrame({
    'Location': ['Warehouse A', 'Warehouse B', 'Warehouse C'],
    'Shipment': [100, 200, 150],
    'Delivered': [80, 180, 120],
    'In Transit': [20, 20, 30]
})

def plot_location_graph(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.set(style="whitegrid")
    ax = sns.barplot(x='Location', y='Shipment', data=data)
    ax.set(xlabel='Location', ylabel='Shipment Count')
    return fig

def main():
    st.title('Logistics Management Dashboard')
    
    # Display location tracking graphs
    st.header('Location Tracking')
    fig = plot_location_graph(data)
    st.pyplot(fig)
    
    # Display detailed dashboard
    st.header('Detailed Dashboard')
    st.dataframe(data,width=2000)

if __name__ == '__main__':
    main()
