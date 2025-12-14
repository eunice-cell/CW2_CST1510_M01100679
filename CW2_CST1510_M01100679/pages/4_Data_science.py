import streamlit as st
from services.database_manager import DatabaseManager
from models.datasets import Dataset   # Import Dataset class
import matplotlib.pyplot as plt

from services.auth_guard import require_login
require_login()# if not logged in no access
st.title("Data Science — Uploaded Datasets")

    # Full absolute path
DB_PATH = r"C:\Users\HP\PycharmProjects\CW2_CST1510_M01100679\database\intelligence_platform.db"

db = DatabaseManager(DB_PATH)
db.connect()

# Fetch dataset rows
rows = db.fetch_all("""
        SELECT 
            id,
            name,
            rows,
            columns,
            uploaded_by,
            date
        FROM datasets
    """)

datasets: list[Dataset] = []

# Convert DB rows → Dataset objects
for row in rows:
    d = Dataset(
        id=row[0],          # MUST be "id", matching your class
        name=row[1],
        rows=row[2],
        columns=row[3],
        uploaded_by=row[4],
        date=row[5]
    )
    datasets.append(d)

st.subheader("All Available Datasets")

# Display each dataset
for d in datasets:
    with st.expander(f"Dataset #{d.get_id()} — {d.get_name()}"):
        st.write("**Name:**", d.get_name())
        st.write("**Rows:**", d.get_rows())
        st.write("**Columns:**", d.get_columns())
        st.write("**Uploaded By:**", d.get_uploaded_by())
        st.write("**Upload Date:**", d.get_date())

db.close()
#  DATASET ANALYTICS (PIE CHART)


st.subheader(" Dataset Analytics From Database")

# Count how many datasets each user uploaded
uploaders = [d.get_uploaded_by() for d in datasets]

uploader_counts = {}
for u in uploaders:
    uploader_counts[u] = uploader_counts.get(u, 0) + 1

st.write("Datasets Uploaded By Each User")

fig, ax = plt.subplots()

ax.pie(
    uploader_counts.values(),
    labels=uploader_counts.keys(),
    autopct='%1.1f%%',
    startangle=90
)

ax.set_title("Dataset Upload Distribution", fontsize=14)
ax.axis("equal")

st.pyplot(fig)