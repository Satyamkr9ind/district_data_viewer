# 📊 District Data Viewer

A modern and interactive **data visualization tool** built with **Streamlit**, allowing users to upload CSV files and explore their data through multiple chart types.

---

## 🛠️ Tech Stack

- **Python 3.12**  
- **Streamlit** – Interactive UI and dashboard  
- **Pandas** – Data processing and analysis  
- **Matplotlib** – Charts and visualizations  

---

## 💡 Project Overview

The **District Data Viewer** helps non-technical users quickly analyze CSV datasets by providing a clean and easy-to-use interface. Users can preview data, visualize trends, and generate multiple types of charts in real-time.

---

## ✨ Features

- Upload CSV files directly through the interface  
- Preview data in a table format  
- Multiple interactive chart types:  
  - Line Chart  
  - Bar Chart  
  - Area Chart  
  - Scatter Plot  
  - Pie Chart  
  - Histogram  
  - Box Plot  
- User-friendly sidebar for selecting chart types and axes  
- Modern dashboard layout with gradient background  

---

## 👨‍💻 Role & Contribution

- Designed and developed the **frontend and backend** using **Python and Streamlit**  
- Implemented **data processing and chart generation** using Pandas and Matplotlib  
- Created a **responsive, clean, and modern UI** for non-technical users  

---

## 📁 Project Folder Structure
app.py # Main Streamlit application
│-- requirements.txt # Python dependencies
│-- README.md # Project description and instructions
│-- .gitignore # Files/folders to ignore on GitHub


**Explanation:**

- `app.py` → main app file with Streamlit dashboard  
- `requirements.txt` → all required Python packages (`streamlit`, `pandas`, `matplotlib`)  
- `.gitignore` → prevents unnecessary files (virtual environment, cache, OS files) from uploading  
- `data/` → optional folder for sample CSVs  
- `screenshots/` → optional images/GIFs of the dashboard for visual demonstration  
- `assets/` → optional CSS, images, or icons for UI customization  

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/district_data_viewer.git
cd district_data_viewer
Create a virtual environment (Python 3.12):

py -3.12 -m venv .venv
source .venv/Scripts/activate  # On Git Bash / Linux / Mac
Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Open the browser when prompted to explore your dashboard.

🔗 Screenshots / Demo
