import streamlit as st
import pandas as pd
import plotly.express as px

# Function to read supply chain data from a CSV file
def read_supply_chain_data(file_path):
    data = pd.read_csv(file_path)
    return data

def plot_location_graph(data):
    fig = px.bar(data, x='sku', y='national_inv')
    return fig

def main():
    st.title('IntelliTrack')

    # Read the supply chain data from the CSV file
    file_path = 'Training_Database.csv'  # Replace with the path to your CSV file
    data = read_supply_chain_data(file_path)

    # Display location tracking graph
    st.header('Order Back Tracking Graph')
    fig = plot_location_graph(data)
    st.plotly_chart(fig)

    # Display detailed dashboard with pagination and filtering
    st.header('Filters')

    # Set the number of rows to display per page
    rows_per_page = 10

    # Filter the data based on user input
    filter_value = st.text_input('Enter a location to filter the data:')
    filtered_data = data[data['sku'].str.contains(filter_value, na=False)]

    # Paginate the data
    num_pages = int(len(filtered_data) / rows_per_page) + 1
    page_number = st.number_input('Enter page number:', min_value=1, max_value=num_pages, step=1)
    start_index = (page_number - 1) * rows_per_page
    end_index = start_index + rows_per_page
    paginated_data = filtered_data.iloc[start_index:end_index]

    # Display the paginated data
    st.dataframe(paginated_data)

if __name__ == '__main__':
    main()
