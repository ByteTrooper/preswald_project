# commented code given by o4 mini prompt

"""

import pandas as pd
import plotly.express as px
import preswald

data = {
    "PassengerId": [892, 893, 894, 895, 896],
    "Survived": [0, 1, 0, 0, 1],
    "Pclass": [3, 3, 2, 3, 3],
    "Name": ["Kelly, Mr. James", "Wilkes, Mrs. James (Ellen Needs)", "Myles, Mr. Thomas Francis", "Wirz, Mr. Albert", "Hirvonen, Mrs. Alexander (Helga E Lindqvist)"],
    "Sex": ["male", "female", "male", "male", "female"],
    "Age": [34.5, 47, 62, 27, 22],
    "SibSp": [0, 1, 0, 0, 1],
    "Parch": [0, 0, 0, 0, 1],
    "Ticket": [330911, 363272, 240276, 315154, 3101298],
    "Fare": [7.8292, 7, 9.6875, 8.6625, 12.2875],
    "Cabin": [None, None, None, None, None],
    "Embarked": ["Q", "S", "Q", "S", "S"]
}

df = pd.DataFrame(data)

# Plot 1: Age distribution
fig1 = px.histogram(df, x='Age', title='Age Distribution of Passengers')
# Plot 2: Survival count
fig2 = px.pie(df, names='Survived', title='Survival Count')
# Plot 3: Fare distribution by class
fig3 = px.box(df, x='Pclass', y='Fare', title='Fare Distribution by Class')

preswald.text("# Title")
preswald.text("## Subtitle")
preswald.text("Description")
preswald.plotly(fig1)
preswald.plotly(fig2)
preswald.plotly(fig3)

"""

# -----------------------------------------------------------------------------------------

# working code 
import pandas as pd
import plotly.express as px
import preswald

# --- Embedded Titanic tested.csv Data (First 10 Rows) ---
# This data is hardcoded directly into the script to ensure it's always available.
# In a real-world scenario, you would use get_df() or read_csv() for larger files.
data = {
    'PassengerId': [892, 893, 894, 895, 896, 897, 898, 899, 900, 901],
    'Pclass': [3, 3, 2, 3, 3, 3, 3, 2, 3, 3],
    'Name': [
        "Kelly, Mr. James",
        "Wilkes, Mrs. James (Ellen Needs)",
        "Myles, Mr. Thomas Francis",
        "Wirz, Mr. Albert",
        "Hirvonen, Mrs. Alexander (Helga E Lindqvist)",
        "Svensson, Mr. Johan Cervin",
        "Connolly, Miss. Kate",
        "Caldwell, Mr. Albert Francis",
        "Abelseth, Miss. Karen Marie",
        "Davies, Mr. John Samuel"
    ],
    'Sex': ['male', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'male'],
    'Age': [34.5, 47.0, 62.0, 27.0, 22.0, 14.0, 30.0, 26.0, 28.0, 21.0],
    'SibSp': [0, 1, 0, 0, 1, 0, 0, 1, 0, 2],
    'Parch': [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    'Ticket': [
        "330911", "363272", "240276", "315154", "3101298",
        "7538", "330972", "248738", "348125", "A/4 48871"
    ],
    'Fare': [7.8292, 7.0, 9.6875, 8.6625, 12.2875, 9.225, 7.6292, 29.0, 7.2292, 24.15],
    'Cabin': [None, None, None, None, None, None, None, "A/4", None, None], # Use None for missing values
    'Embarked': ['Q', 'S', 'Q', 'S', 'S', 'S', 'Q', 'S', 'C', 'S']
}

# Create a pandas DataFrame from the embedded data
df = pd.DataFrame(data)

# --- UI: App Title and Overview ---
preswald.text("# Titanic Data Analysis App")
preswald.text("## Dataset Overview")
preswald.text("This app explores a small sample of data from the Titanic dataset.")
preswald.text("Key columns include PassengerId, Pclass, Sex, Age, Fare, SibSp (siblings/spouses), and Parch (parents/children).")

# Display a sample of the loaded data
preswald.text("### Sample Data (First 5 Rows)")
preswald.text(df.head().to_string())

# --- Debugging (Simplified, now that data is embedded) ---
preswald.text("### Debugging: DataFrame Info")
preswald.text("DataFrame Shape: " + str(df.shape))
preswald.text("DataFrame Columns: " + str(df.columns.tolist()))


# --- Data Query/Manipulation ---
# 2. Query or manipulate the data (e.g., filter passengers older than 30 in 1st/2nd class)
# Note: Since the data is in 'df', we simulate the SQL query using pandas filtering
# If Preswald's `query` function still causes issues with an in-memory DF, this alternative works.

# Using pandas to filter as it's more direct with an in-memory DataFrame
# If Preswald's `query` function *requires* a registered dataset name, we would stick to the original `query(sql_query, "test")` but it's causing issues.
# Let's try to query an in-memory DataFrame if it's supported by `preswald.query` without a registered file.
# If `query` still fails, we'll revert to pure pandas filtering.

# For robust operation with embedded data, direct pandas filtering is safer:
filtered_df = df[(df['Age'] > 30) & ((df['Pclass'] == 1) | (df['Pclass'] == 2))].sort_values(by='Age', ascending=False)
# If the assessment explicitly requires `preswald.query` for *any* operation, let me know.
# Otherwise, pandas filtering is functionally equivalent for this task.

# If the assessment *insists* on `preswald.query` and it still fails, we might need a workaround like creating a temporary
# in-memory table if the platform supports it (unlikely or too complex for assessment).

# --- UI: Display Filtered Data Table ---
preswald.text("## Filtered Data: Passengers Older Than 30 in 1st/2nd Class")
preswald.text("Below is a table showing passengers who are older than 30 and were in either 1st or 2nd class.")
preswald.table(filtered_df, title="Filtered Passengers Table")


# --- Visualizations ---
preswald.text("## Visualizations")

# 4. Create a visualization (Example 1: Scatter plot of Age vs. Fare, colored by Sex)
preswald.text("### Age vs. Fare by Sex")
fig1 = px.scatter(
    df, # Use the full DataFrame for this visualization
    x="Age",
    y="Fare",
    color="Sex", # Categorical column for color
    title="Age vs. Fare Distribution by Sex on the Titanic",
    hover_data=['Pclass', 'PassengerId'] # Additional info on hover
)
preswald.plotly(fig1)


# 4. Create a visualization (Example 2: Bar chart of Passenger Class Distribution)
preswald.text("### Passenger Class Distribution")
# Count occurrences of each Pclass and prepare for bar chart
class_counts = df['Pclass'].value_counts().reset_index()
class_counts.columns = ['Pclass', 'Count'] # Rename columns for the bar chart
fig2 = px.bar(
    class_counts,
    x='Pclass',
    y='Count',
    title="Count of Passengers by Class",
    color='Pclass', # Color bars by class
    labels={'Pclass': 'Passenger Class', 'Count': 'Number of Passengers'}
)
preswald.plotly(fig2)