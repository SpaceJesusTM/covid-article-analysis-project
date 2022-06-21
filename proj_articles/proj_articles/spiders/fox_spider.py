"""
This file contains the class responsible for scraping all Fox News articles.
"""
import scrapy


class FNspider(scrapy.Spider):
    """Spider Class for Fox News Articles"""
    name = "foxnews"
    start_urls = [
        'https://www.foxnews.com/health/coronavirus-vaccine-rollout-plagued-protests-failed-technology-frontline-workers-missing-out',
        'https://www.foxnews.com/opinion/congressman-tests-positive-covid-vaccine-dr-marc-siegel',
        'https://www.foxnews.com/opinion/tucker-carlson-big-tech-silences-questions-about-covid-vaccine',
        'https://www.foxnews.com/sports/top-ranked-tennis-players-coronavirus-vaccine-trust',
        'https://www.foxnews.com/sports/bills-josh-allen-covid-vaccine-mandate-against-constitution',
        'https://www.foxnews.com/health/pfizer-vaccine-effective-india-variant',
        'https://www.foxnews.com/media/tucker-carlson-mrna-vaccine-inventor',
        'https://www.foxnews.com/opinion/tucker-carlson-democrats-cdc-lying-covid-vaccine',
        'https://www.foxnews.com/health/fauci-study-delta-efficacy-moderna-pfizer-booster',
        'https://www.foxnews.com/sports/phillies-didi-gregorius-covid-vaccine-down-year',
        'https://www.foxnews.com/media/biden-pandemic-vaccine-jesse-watters-the-five',
        'https://www.foxnews.com/health/university-of-oxford-omicron-no-proof-covid-vaccines-wont-prevent-against-severe-disease',
        'https://www.foxnews.com/us/covid-day-us-200m-vaccine-milestone'
    ]

    def parse(self, response, **kwargs):
        """Crawls through article and generates csv file with the articles:
                    - Date
                    - Title
                    - Text
        """
        full_date = response.css('.article-date time::text').get()
        date = full_date.split(' ')[1] + '_' + full_date.split(' ')[2]
        title = response.css('title::text').get()
        text = response.css('.article-body p::text').getall()
        filename = f'fox-news{date}.csv'
        with open(filename, 'w') as f:
            f.write(str(date) + '\n' + str(title) + '\n' + str(text))
