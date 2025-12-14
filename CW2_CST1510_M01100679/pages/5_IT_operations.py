import streamlit as st
import matplotlib.pyplot as plt

from services.database_manager import DatabaseManager
from models.it_tickets import ITTicket

from services.auth_guard import require_login
require_login()# if not logged in no access
st.title(" IT Operations — Support Tickets")

# Using your FULL DB PATH
DB_PATH = r"C:\Users\HP\PycharmProjects\CW2_CST1510_M01100679\database\intelligence_platform.db"

db = DatabaseManager(DB_PATH)
db.connect()

# Fetch rows from your *real* tickets table
rows = db.fetch_all("""
        SELECT 
            id,
            priority,
            description,
            status,
            created_at,
            created_date
        FROM tickets
    """)

tickets: list[ITTicket] = []

#  Convert DB rows → ITTicket objects
for row in rows:
    t = ITTicket(
        id=row[0],            #  matches your constructor exactly
        priority=row[1],
        description=row[2],
        status=row[3],
        created_at=row[4],
        created_date=row[5]
    )
    tickets.append(t)

st.subheader(" All IT Tickets")

# Display each ticket using getters
for t in tickets:
    with st.expander(f"Ticket #{t.get_id()} — {t.get_status()}"):

        st.write("**Priority:**", t.get_priority())
        st.write("**Description:**", t.get_description())
        st.write("**Status:**", t.get_status())
        st.write("**Created At:**", t._ITTicket__created_at)      #  accessing private attr safely
        st.write("**Created Date:**", t._ITTicket__created_date)  #  accessing private attr safely

        #  Button to close tickets
        if t.get_status().lower() != "closed":
            if st.button(f"Close Ticket #{t.get_id()}"):
                t.close()  # update object status

                db.execute_query(
                    "UPDATE tickets SET status = ? WHERE id = ?",
                    (t.get_status(), t.get_id())
                )

                st.success("Ticket closed! Refresh page to update display.")

db.close()

# IT Operations Ticket Analytics (Pie Chart Only)


st.subheader("Ticket Analytics")

# Extract all ticket statuses from objects
statuses = [t.get_status() for t in tickets]

# Count each status manually
status_counts = {}
for s in statuses:
    status_counts[s] = status_counts.get(s, 0) + 1

# PIE CHART — Ticket Status Distribution
st.write("Tickets by Status")

fig, ax = plt.subplots()

ax.pie(
    status_counts.values(),
    labels=status_counts.keys(),
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Ticket Status Distribution", fontsize=14)
ax.axis("equal")

st.pyplot(fig)
