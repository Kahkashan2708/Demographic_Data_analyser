# Demographic Data Analyzer

This project is a basic **Demographic Data Analyzer** implemented in Python using **Pandas**. It demonstrates simple data analysis techniques on a small dataset to explore relationships between demographic attributes and income levels.

## Dataset

The dataset is manually created as a small pandas DataFrame, mimicking features found in real-world census or demographic datasets.

### Columns Included:
- `age`
- `workclass`
- `fnlwgt` (final weight)
- `education`
- `education-num`
- `marital-status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `capital-gain`
- `capital-loss`
- `hours-per-week`
- `native-country`
- `salary` (target variable)

## Features & Operations

The script performs the following tasks:

1. **Count of People by Race**  
   Uses `value_counts()` to display frequency of each race in the dataset.

2. **Average Age (excluding one entry)**  
   Computes mean age excluding the record with index `'5'`.

3. **Percentage of People with Bachelor's Degree**  
   Calculates how many individuals hold a Bachelor's degree and computes their percentage in the dataset.

4. **Income >50K among Bachelor's Degree Holders**  
   Identifies people with Bachelor's degrees earning more than 50K and calculates the percentage.

5. **Income >50K among Non-Bachelor Degree Holders**  
   Does similar analysis for individuals without a Bachelor's degree.

6. **Minimum Working Hours**  
   Retrieves the minimum number of hours worked per week in the dataset.

7. **Income >50K Among Minimum Hour Workers**  
   Determines what percentage of people who work the minimum number of hours earn more than 50K.

8. **Overall Income >50K Percentage & Country-wise Insight**  
   Displays total percentage of people earning more than 50K. Since it's a small dataset, a placeholder is used for country-wise insights.

9. **People from India**  
   Filters and displays all entries where the native country is "India".

##  How to Run

1. Make sure you have Python installed (>= 3.6).
2. Install required library:
   ```bash
   pip install pandas

