# 🗂️ JSON Data Manipulation & Merging in Python

## 📌 Problem Statement

Create a Python script that:
1. Reads data from JSON files
2. Loops through a list of items
3. Extracts nested values
4. Merges multiple JSON files **without overlap**

------------------------------------------------------------------------

## 📜 Project Overview

This project demonstrates how to work with JSON files in Python using
the built-in `json` module.
It covers:
- Reading JSON files
- Iterating through list values (e.g., skills)
- Extracting nested dictionary values (e.g., job role, years, company)
- Adding new keys to JSON data
- Merging multiple JSON files into one consolidated JSON file

------------------------------------------------------------------------

## 📂 File Structure

    project/
    │── data1.json          # Sample JSON file (Employee 1)
    │── data2.json          # Sample JSON file (Employee 2)
    │── json_read_write.py  # Main Python script
    │── updated_data1.json  # Output after modifying data1.json
    │── updated_data2.json  # Output after modifying data2.json
    │── merged_data.json    # Final merged JSON file
    │── README.md           # Documentation

------------------------------------------------------------------------

## ▶️ How to Run

1.  Clone this repository

    ``` bash
    git clone https://github.com/your-username/json-merge-py.git
    cd json-merge-py
    ```

2.  Make sure Python 3 is installed on your system.

3.  Run the script:

    ``` bash
    python json_read_write.py
    ```

4.  Check the generated files:

    -   `updated_data1.json`
    -   `updated_data2.json`
    -   `merged_data.json`

------------------------------------------------------------------------

## ✅ Example Output

### Original Data (`data1.json`)

``` json
{
    "id": 101,
    "name": "Imran Ahmad",
    "skills": ["Python", "Selenium", "PyTest"],
    "experience": {
        "role": "Automation Tester",
        "years": 3,
        "company": "Heaven of Freedom"
    }
}
```

### Updated Data (`updated_data1.json`)

``` json
{
    "id": 101,
    "name": "Imran Ahmad",
    "skills": ["Python", "Selenium", "PyTest"],
    "experience": {
        "role": "Automation Tester",
        "years": 3,
        "company": "Heaven of Freedom"
    },
    "status": "processed"
}
```

### Merged Data (`merged_data.json`)

``` json
[
    {
        "id": 101,
        "name": "Imran Ahmad",
        "skills": ["Python", "Selenium", "PyTest"],
        "experience": {
            "role": "Automation Tester",
            "years": 3,
            "company": "Heaven of Freedom"
        },
        "status": "processed"
    },
    {
        "id": 102,
        "name": "Sara Khan",
        "skills": ["Java", "TestNG", "API Testing"],
        "experience": {
            "role": "QA Engineer",
            "years": 2,
            "company": "Never More"
        },
        "status": "rejected"
    }
]
```

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3
-   JSON module

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add support for **merging all JSON files dynamically** from a
    folder.
-   Include **error handling** for malformed or empty JSON files.
-   Extend script to handle **nested merges** across multiple levels.
-   Add **unit tests** to validate JSON processing.
-   Provide a **command-line interface (CLI)** for flexible usage.

------------------------------------------------------------------------
