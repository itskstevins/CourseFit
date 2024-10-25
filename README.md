# CourseFit
A tool to simplify course qualification for students based on their grades.

## Description:
CourseFit is designed to streamline the process of checking university course qualifications. Using pdfplumber, the tool extracts data tables from PDFs containing course information and cutoff points. The extracted data is converted to JSON format, making it easy to process and search. Students can input their grades, and the tool calculates their KUCCPS cluster points, then matches them with qualifying courses and universities.

## Features:

1.PDF Data Extraction: Automatically extracts course tables from PDF files. \n
2.Data Conversion: Converts extracted data to JSON format for easier handling and storage.
3.Cluster Point Calculation: Calculates KUCCPS cluster points based on user-provided grades.
4.Course Matching: Outputs a list of qualified courses and respective universities.

## Technologies:

Python (for core functionality)
pdfplumber (for PDF table extraction)
JSON (for structured data storage and manipulation)

## Usage:


Enter student grades to calculate cluster points.
View the list of qualified courses and universities based on student eligibility.
