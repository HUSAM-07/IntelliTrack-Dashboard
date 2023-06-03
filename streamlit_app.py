import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide",page_title="IntelliTrack",page_icon="📦")

# Sample data for demonstration
data = pd.DataFrame({
    'Location': ['Warehouse A', 'Warehouse B', 'Warehouse C'],
    'Shipment': [100, 200, 150],
    'Delivered': [80, 180, 120],
    'In Transit': [20, 20, 30]
})

def plot_location_graph(data):
    fig = px.bar(data, x='Location', y='Shipment', labels={'Location': 'Location', 'Shipment': 'Shipment Count'})
    return fig

def main():
    st.title('Logistics Management Dashboard')
    
    # Display location tracking graphs
    st.header('Location Tracking')
    fig = plot_location_graph(data)
    st.plotly_chart(fig)
    
    # Display detailed dashboard
    st.header('Detailed Dashboard')
    st.dataframe(data,width=2000)

if __name__ == '__main__':
    main()
