# 📊 District Data Viewer
![Python](https://img.shields.io/badge/python-3.12-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.24.0-orange)

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
district_data_viewer/
│-- app.py                  # Main Streamlit application
│-- requirements.txt        # Python dependencies
│-- README.md               # Project description
│-- .gitignore              # Files/folders to ignore


**Explanation:**

- `app.py` → main app file with Streamlit dashboard  
- `requirements.txt` → all required Python packages (`streamlit`, `pandas`, `matplotlib`)  
- `.gitignore` → prevents unnecessary files (virtual environment, cache, OS files) from uploading  

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Satyamkr9ind/district_data_viewer.git
cd district_data_viewer
```
2. Create a virtual environment (Python 3.12):
```bash
py -3.12 -m venv .venv
source .venv/Scripts/activate  # On Git Bash / Linux / Mac

```
3. Install dependencies:
  ```bash
pip install -r requirements.txt

```
4. Run the app:
```bash
streamlit run app.py
```
5. Open the browser when prompted to explore your dashboard.

## 📝 How to Use

1. Click "Browse" and upload your CSV file.  
2. Select the chart type from the sidebar.  
3. Choose the columns to visualize.  
4. The chart updates in real-time based on your selection.

### CSV Format Example

| District | Population | Area | LiteracyRate |
|----------|-----------|------|--------------|
| A        | 50000     | 100  | 75           |
| B        | 75000     | 150  | 80           |

   
**🔗 Screenshots / Demo **
<img width="1897" height="762" alt="image" src="https://github.com/user-attachments/assets/e929abc3-ae5b-462a-a3b1-fce3d75d7397" />
<img width="1904" height="802" alt="image" src="https://github.com/user-attachments/assets/eefc2215-d350-47c5-8d29-f2938cf92ada" />
<img width="1087" height="820" alt="image" src="https://github.com/user-attachments/assets/bcc27084-5510-41e3-8708-b29778e5c725" />

## 📦 Dependencies

- Python 3.12  
- streamlit==1.24.0  
- pandas==2.3.3  
- matplotlib==3.8.0

## 👤 Author

- **Name:** Satyam Kumar  
- **GitHub:** [https://github.com/Satyamkr9ind](https://github.com/Satyamkr9ind)

## 🚀 Future Improvements

- Add more chart types (Heatmap, Radar)  
- Integrate data filtering and sorting options  
- Add export functionality (PDF, PNG of charts)  
- Host the app online for live demo (Streamlit Cloud)

  




   




