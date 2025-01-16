# Naukri.com Data Scientist Job Scraper
![image](https://github.com/user-attachments/assets/2bc1deb2-e6f7-4c9a-96e1-d79a287af29f)

This project is a web scraper that extracts data on Data Scientist job postings from [Naukri.com](https://www.naukri.com). It scrapes key information such as job title, company, ratings, required experience, salary, location, job posting history, skills, and a brief job description.

The data is saved in a CSV format for easy analysis and processing.

## Features

- Scrapes job listings for Data Scientist roles.
- Extracts job details such as:
  - Job title, company, ratings, experience, salary, and location.
  - Posting history, skills required, and job description.
- Handles multiple pages of job listings.
- Outputs the data in CSV format.

## Folder Structure

```bash
├── code/                   # Contains the scraper logic
│   ├── job-scraper.py      # Main scraper script
│
├── data/                   # Folder to store the scraped data
│   └── Naukri.com_datascraped.csv  # Sample output of scraped data
├── README.md               # Project documentation
└── requirements.txt        # List of required dependencies
```

## Prerequisites

Ensure you have the following installed:
- Python 3.x (preferably 3.7+)
- Chrome web browser
- ChromeDriver corresponding to your Chrome version (Download from https://sites.google.com/a/chromium.org/chromedriver/)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/naukri-job-scraper.git
   cd naukri-job-scraper
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver**:
   - Download the appropriate ChromeDriver version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Ensure the `chromedriver.exe` is placed in the `scraper` folder or modify the script to reflect the path to the driver.

---

## Usage

1. **Run the scraper**:

   After setting up the environment and dependencies, run the `job-scraper.py` script:

   ```bash
   python code/job-scraper.py
   ```

   The script will start scraping Data Scientist job listings from Naukri.com and store the scraped data in a CSV file.

2. **Output**:

   The results will be saved in the `data/` folder in a file named `Naukri.com_datascraped.csv`.

---

## Example Output

Here's a preview of the kind of data you can expect from the scraper:

| Title                                       | Company                              | Ratings | Experience | Salary       | Location       | Job_Post_History | Skills                                                                                               | Description                                                                                          |
|---------------------------------------------|--------------------------------------|---------|------------|--------------|----------------|------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Urgent Opening For Data Scientist - Machine Learning | SPI technologies india private limited | 3.7     | NA         | Not disclosed | Chennai         | 4 Days Ago       | ['python', 'nlp', 'machine learning', 'data engineering', 'Pytorch', 'Airflow', 'dba'] | Shift - Flexible shift timing (9hrs of Working). Bachelors degree or higher in computer science or related field. |
| Data Scientist                               | Applied Materials                    | 4.3     | 0-3 Yrs    | Not disclosed | Bangalore/Bengaluru | 8 Days Ago   | ['Unix', 'semiconductor', 'JMP', 'analyzing data', 'statistical analysis', 'Multivariate Analysis'] | Acquire, cleanse, organize and mine massive volumes of data (sensor / system log) using statistical tools. |
| Senior Data Scientist / Lead Data Scientist | Geakminds Technologies Private Limited | 4.4     | NA         | Not disclosed | Chennai         | 6 Days Ago       | ['Machine Learning', 'Python', 'Tableau', 'Azure', 'GCP', 'data mining']  | Full time position. Experience with cloud platforms like Azure or GCP is required.                    |
| Immediate Hiring For DATA Scientist @ HCL   | HCL Technologies                     | 3.8     | 12-18 Yrs  | Not disclosed | Chennai         | 6 Days Ago       | ['Tensorflow', 'deep learning', 'python', 'Semiconductor', 'data scientist']                         | Greetings from HCL Technologies! We are hiring for the position of DATA SCIENTIST @ Chennai.          |

---

## Dependencies

The following Python libraries are required:

- `selenium`: For automating web browser interactions.
- `beautifulsoup4`: For parsing HTML and extracting the job data.
- `pandas`: For storing the scraped data in a structured format (CSV).
- `requests`: For making HTTP requests to fetch the webpage content.
- `html5lib`: A parser used by BeautifulSoup to handle HTML content.

You can install the dependencies by running:

```bash
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions to improve this project! Here's how you can get involved:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request with a description of your changes

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for browser automation
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- [Naukri.com](https://www.naukri.com) for the dataset

---

## Example Improvements

Here are some ideas for improving this project:

- Add functionality to scrape multiple job categories (e.g., Machine Learning, AI, Data Engineering, etc.)
- Introduce error handling and retry mechanisms to make the scraper more robust.
- Implement logging for better debugging and error tracking.
- Enhance the script to scrape job details from other job portals.

---

### `requirements.txt` file

Here’s the content for your `requirements.txt` file:

```
selenium==4.4.0
beautifulsoup4==4.12.0
pandas==1.5.3
requests==2.28.1
html5lib==1.1
```

These dependencies include:

- `selenium` for browser automation.
- `beautifulsoup4` for parsing HTML.
- `pandas` for handling data in CSV format.
- `requests` for making network requests.
- `html5lib` for parsing HTML content with BeautifulSoup.

---
