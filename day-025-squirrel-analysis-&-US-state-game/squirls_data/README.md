---

### 📄 Project 2: Squirrel Census Analysis 🐿️

```markdown
# Day 25: Central Park Squirrel Census Analysis 🐿️

This project is a data analysis tool that processes a real-world dataset containing thousands of records from the 2018 Central Park Squirrel Census.

## 📝 Description
The goal of this project was to parse a large, complex CSV file to answer a specific data question: "How many squirrels of each primary fur color exist in Central Park?" The script filters the data, counts the occurrences of Gray, Cinnamon, and Black squirrels, and exports a clean summary report.

## ✨ Features
- **Big Data Processing:** Efficiently handles a dataset with over 3,000 rows of observations.
- **Data Filtering:** Targets specific columns (Primary Fur Color) and ignores empty or irrelevant data points.
- **Automated Reporting:** Generates a new, condensed CSV file (`squirrel_count.csv`) that summarizes the findings.
- **Dictionary Integration:** Uses a Python dictionary to structure analyzed data before converting it into a Pandas DataFrame.

## 💡 What I Learned
- **Exploratory Data Analysis (EDA):** Using `pandas` to navigate large external datasets.
- **Conditional Counting:** Implementing logic to iterate through data lists and increment counters based on specific values.
- **Building DataFrames:** Constructing a professional table from scratch using `pandas.DataFrame()`.
- **Data Pipeline:** The process of taking raw, "dirty" data, extracting meaningful metrics, and saving them into an organized format for stakeholders.

## 🚀 How to Run
1. Ensure you have `pandas` installed.
2. Ensure the script and the `2018_Central_Park_Squirrel_Census...csv` file are in the same folder.
3. Run the script:
   ```bash
   python Main.py