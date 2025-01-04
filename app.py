import streamlit as st
import psutil

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

st.title("System Performance Dashboard")

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
st.write(f"CPU Usage: {cpu_usage}%")

# Memory Usage
memory = psutil.virtual_memory()
st.write(f"Memory Usage: {memory.percent}%")

# Disk Usage
disk = psutil.disk_usage('/')
st.write(f"Disk Usage: {disk.percent}%")

# Application Title
st.title("Secure Web Management Dashboard")

# Create Tabs
tab1, tab2, tab3 = st.tabs(["Performance Monitoring", "Security Hardening", "Web Server Management"])

# Tab 1: Performance Monitoring
with tab1:
    st.header("System Performance Monitoring")
    
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    st.metric("CPU Usage", f"{cpu_usage}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    st.metric("Memory Usage", f"{memory.percent}%")

    # Disk Usage
    disk = psutil.disk_usage('/')
    st.metric("Disk Usage", f"{disk.percent}%")

    st.write("**Note:** These metrics are updated in real-time for server health monitoring.")

# Tab 2: Security Hardening
with tab2:
    st.header("Security Hardening Checklist")

    # Checklist for Security Hardening
    st.write("### Key Security Measures")
    checklist = [
        "Enable Firewall",
        "Enforce HTTPS for websites",
        "Restrict IP access to server",
        "Disable unused modules/services",
        "Regularly update and patch the system",
        "Set up secure backups and recovery",
        "Monitor logs for suspicious activities",
    ]

    # Display checklist items as checkboxes
    for item in checklist:
        st.checkbox(item)

    st.write("### Simulated Security Actions")
    if st.button("Run Security Audit"):
        st.success("Security audit completed successfully!")

# Tab 3: Web Server Management
with tab3:
    st.header("Web Server Management (Simulated IIS)")
    
    # Server Status Management
    st.write("### Manage Web Server Status")
    server_status = st.radio("Server Status:", ["Running", "Stopped", "Restart"])
    if server_status == "Running":
        st.success("Web Server is Running")
    elif server_status == "Stopped":
        st.warning("Web Server is Stopped")
    elif server_status == "Restart":
        st.info("Web Server Restarted Successfully")

    # Website Configuration
    st.write("### Configure a Website")
    domain = st.text_input("Enter Domain Name:")
    if st.button("Add Website"):
        if domain:
            st.success(f"Website '{domain}' has been configured successfully!")
        else:
            st.error("Please enter a valid domain name.")

# Footer
st.markdown("---")
st.write("Powered by Streamlit | Project: SecureWeb Manager")
