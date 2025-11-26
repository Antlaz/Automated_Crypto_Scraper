This project pulls the current Bitcoin price from CoinMarketCap and logs it to a CSV file over time.

It was built as a learning project to understand:
- Differences between static vs dynamic web content
- When to use BeautifulSoup vs Selenium
- Basic automation and file output in Python

How it wokrks
1. Uses `requests` and `BeautifulSoup` to retrieve static page content (coin name).
2. Uses `Selenium` with ChromeDriver to load JavaScript-rendered content (live price).
3. Stores the price, coin name, and timestamp in a pandas DataFrame.
4. Appends results to a CSV file on each run.
