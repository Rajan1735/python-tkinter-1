import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the data from the Excel file
data_path = "C:/Users/user/Downloads/jobs_data_clean_1.xlsx"
df = pd.read_excel(data_path)

# Rename the 'Sector' column to 'sector' if needed
df.rename(columns={'Sector': 'sector'}, inplace=True)

# Create a directed graph
G = nx.DiGraph()

# Add nodes (sectors) to the graph
for sector in df['sector'].unique():
    G.add_node(sector, name=sector)

# Add edges (parent-child relationships) to the graph
for _, row in df.iterrows():
    sector = row['sector']
    skills = row['skills'].split(', ')  # Assuming skills are separated by a comma and space
    for skill in skills:
        G.add_edge(sector, skill)

# Create a hierarchical layout for the graph
pos = nx.spring_layout(G, seed=42)  # You can change the layout algorithm as needed

# Draw the graph with labels
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_color='black')
plt.title("Sector-Skills Hierarchy")
plt.axis('off')
plt.show()
