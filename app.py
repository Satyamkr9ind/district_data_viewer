import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="District Data Viewer",
    page_icon="📊",
    layout="wide",
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#f0f4ff,#e8fff7);
}
.upload-box {
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
}
.title {
    font-size:40px;
    font-weight:700;
    text-align:center;
    color:#1a1a1a;
}
.sub {
    font-size:18px;
    text-align:center;
    color:#555;
}
.stAlert {
    background: #e8ffe8 !important;
    border-left: 6px solid #27ae60 !important;
}
.stAlert > div {
    color: #1a1a1a !important;
    font-weight: 600 !important;
}            
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 class='title'>📊 District Data Viewer</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub'>Upload CSV → Explore Data → Visualize Instantly</p>", unsafe_allow_html=True)
st.write("")

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Visualization Options")

chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    [
        "Line Chart",
        "Bar Chart",
        "Area Chart",
        "Scatter Plot",
        "Pie Chart",
        "Histogram",
        "Box Plot"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Upload a CSV file to get started.")

# ---------- FILE UPLOAD ----------
st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ---------- PROCESS FILE ----------
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Show data
    st.subheader("📄 Data Preview")
    st.dataframe(df, use_container_width=True)

    # Numeric columns only
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    text_cols = df.select_dtypes(include="object").columns.tolist()

    if len(numeric_cols) < 1:
        st.error("❌ CSV must contain numeric columns for visualization.")
    else:
        st.subheader("📈 Visualization")

        col1, col2 = st.columns(2)

        # Dropdowns based on chart type
        if chart_type == "Pie Chart":
            y_axis = col1.selectbox("Select Column for Pie Chart", numeric_cols)
            labels_col = col2.selectbox("Labels (Optional)", text_cols)
        elif chart_type in ["Histogram", "Box Plot"]:
            y_axis = col1.selectbox("Select Numerical Column", numeric_cols)
        else:
            x_axis = col1.selectbox("X-axis", numeric_cols)
            y_axis = col2.selectbox("Y-axis", numeric_cols)

        # Matplotlib chart area
        fig, ax = plt.subplots()

        # ---------- CHART LOGIC ----------
        if chart_type == "Line Chart":
            ax.plot(df[x_axis], df[y_axis])

        elif chart_type == "Bar Chart":
            ax.bar(df[x_axis], df[y_axis])

        elif chart_type == "Area Chart":
            ax.fill_between(df[x_axis], df[y_axis], alpha=0.5)

        elif chart_type == "Scatter Plot":
            ax.scatter(df[x_axis], df[y_axis])

        elif chart_type == "Pie Chart":
            pie_values = df[y_axis].head(10)
            pie_labels = df[labels_col].head(10)
            ax.pie(pie_values, labels=pie_labels, autopct="%1.1f%%")
            ax.set_title("Top 10 Pie Chart")

        elif chart_type == "Histogram":
            ax.hist(df[y_axis], bins=20)
            ax.set_title(f"Histogram of {y_axis}")

        elif chart_type == "Box Plot":
            ax.boxplot(df[y_axis], vert=True)
            ax.set_title(f"Box Plot of {y_axis}")

        # ---------- LABELS ----------
        if chart_type not in ["Pie Chart", "Histogram", "Box Plot"]:
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title(f"{chart_type}: {x_axis} vs {y_axis}")

        st.pyplot(fig)

else:
    st.warning("Upload a CSV to begin visualization.")
