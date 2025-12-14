import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

from services.database_manager import DatabaseManager
from services.auth_guard import require_login

require_login()  # if not logged in no access

st.title("CyberSecurity Incident Prediction (KNN)")

# Connect to database
db_path = r"C:\Users\HP\PycharmProjects\CW2_CST1510_M01100679\database\intelligence_platform.db"
db = DatabaseManager(db_path)
db.connect()

# Fetch incidents data
incident_rows = db.fetch_all("""      
    SELECT 
        id,         
        i_date,      
        i_type,      
        status,      
        description, 
        reported_by  
    FROM cyber_incidents   
""")
db.close()

# Convert to DataFrame
incidents_df = pd.DataFrame(incident_rows, columns=["id","date","i_type","status","description","reported_by"])

st.subheader("Sample Incidents")
st.dataframe(incidents_df.head())

# Features for model
features = incidents_df[["status", "reported_by"]]

# Encode target variable
target_encoder = LabelEncoder()
target = target_encoder.fit_transform(incidents_df["i_type"])

# Preprocessing: one-hot encode categorical features
preprocessor = ColumnTransformer([
    ("onehot", OneHotEncoder(), ["status", "reported_by"])
])

# KNN pipeline
knn_model = Pipeline([
    ("preprocess", preprocessor),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train KNN model
knn_model.fit(X_train, y_train)

# Predict and evaluate
predictions = knn_model.predict(X_test)

st.subheader("Model Evaluation")
st.write("Accuracy:", accuracy_score(y_test, predictions))
st.text(classification_report(y_test, predictions, labels=list(range(len(target_encoder.classes_))), target_names=target_encoder.classes_))

# Prediction interface
st.subheader("Predict i_type for a New Incident")
new_status = st.selectbox("Status", incidents_df["status"].unique())
new_reporter = st.selectbox("Reported By", incidents_df["reported_by"].unique())

if st.button("Predict"):
    new_incident = pd.DataFrame([[new_status, new_reporter]], columns=["status","reported_by"])
    predicted_type = knn_model.predict(new_incident)
    st.success(f"Predicted i_type: {target_encoder.inverse_transform(predicted_type)[0]}")
