# SecureWebOpt-ToDo-List

A comprehensive project integrating **performance tuning**, **security hardening**, and **web server management** within a Streamlit-based dashboard. This project also includes a simple and interactive **To-Do List application**.

## Features

### Performance Monitoring
* Real-time metrics for CPU, memory, and disk usage using `psutil`.

### Security Hardening
* Checklist for implementing essential server security measures.
* Simulated security audit functionality.

### Web Server Management
* Manage web server status (start, stop, restart).
* Simulate configuration of websites on IIS (Internet Information Services).

### To-Do List Application
* Add, update, and delete tasks.
* Save and retrieve task lists.

## Project Structure

```
SecureWebOpt-ToDo-List/
│
├── app.py             # Main Streamlit application
├── dashboard.py       # To-Do List functionality
├── integration.py     # Integrates performance, security, and web management
├── requirements.txt   # Python dependencies
├── README.md         # Project documentation
├── .gitignore        # Ignored files for Git
├── .venv/            # Virtual environment (not tracked by Git)
└── .git/             # Git repository
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SecureWebOpt-ToDo-List.git
   cd SecureWebOpt-ToDo-List
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at:
   ```
   http://localhost:8501
   ```

## Technologies Used

* **Python**
* **Streamlit** for the dashboard interface
* **psutil** for performance monitoring
* **IIS** (simulated) for web server management

## Future Enhancements

* Integrate actual IIS management for Windows-based systems
* Add automation scripts for server hardening
* Implement live log monitoring for security auditing

![Screenshot 2025-01-04 161900](https://github.com/user-attachments/assets/1b632ecd-03f7-494c-b948-09ebf8da9212)
![Screenshot 2025-01-04 183507](https://github.com/user-attachments/assets/1757498c-4f85-47a3-a5ca-6d83145cd81b)
![Screenshot 2025-01-04 183525](https://github.com/user-attachments/assets/15b51813-1974-4f3a-99f7-5a8b4a2cbd18)
![Screenshot 2025-01-04 183538](https://github.com/user-attachments/assets/61108818-1b92-4432-818a-338b2a1a651a)
