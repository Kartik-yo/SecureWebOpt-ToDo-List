import streamlit as st

# Title of the app
st.title("Simple To-Do List")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Function to add a new task
def add_task():
    if st.session_state["new_task"]:
        st.session_state["tasks"].append(st.session_state["new_task"])
        st.session_state["new_task"] = ""  # Clear input field

# Input box for new task
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# Display the list of tasks
st.subheader("Your Tasks:")
for i, task in enumerate(st.session_state["tasks"]):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"{i + 1}. {task}")
    if col2.button("Remove", key=f"remove_{i}"):
        st.session_state["tasks"].pop(i)
        st.experimental_rerun()  # Refresh the app to reflect changes
