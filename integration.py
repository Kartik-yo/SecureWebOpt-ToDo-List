import streamlit as st

st.title("SecureWebOpt Dashboard")

tab1, tab2, tab3 = st.tabs(["Performance Monitoring", "Security Hardening", "Web Server Management"])

# Tab 1: Performance Monitoring
with tab1:
    import psutil

    st.write("### System Performance Metrics")
    st.write(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    memory = psutil.virtual_memory()
    st.write(f"Memory Usage: {memory.percent}%")
    disk = psutil.disk_usage('/')
    st.write(f"Disk Usage: {disk.percent}%")

# Tab 2: Security Hardening
with tab2:
    st.write("### Security Hardening Checklist")
    checklist = [
        "Enable Firewall",
        "Enforce HTTPS for websites",
        "Restrict IP access to server",
        "Disable unused IIS modules",
        "Regularly update and patch server",
        "Enable secure backups",
    ]
    for item in checklist:
        st.checkbox(item)

# Tab 3: Web Server Management
with tab3:
    st.write("### Web Server Management")
    status = st.radio("Select Server Status:", ("Running", "Stopped", "Restart"))
    if status:
        st.success(f"Server is {status}")

    domain = st.text_input("Enter domain name to configure:")
    if st.button("Configure"):
        if domain:
            st.success(f"Website {domain} configured successfully!")
