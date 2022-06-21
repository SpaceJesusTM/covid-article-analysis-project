"""
This file contains the class responsible for scraping all National Post articles.
"""
import scrapy


class NPspider(scrapy.Spider):
    """Spider Class for National Post Articles"""
    name = "nationalpost"
    start_urls = [
        'https://nationalpost.com/news/unease-amid-the-joy-most-canadians-willing-to-get-covid-19-vaccine-but-some-worry-about-side-effects',
        'https://nationalpost.com/news/a-quarter-of-canadians-dont-want-the-covid-19-vaccine-we-asked-the-experts-why',
        'https://nationalpost.com/news/canada/reason-to-celebrate-early-evidence-suggests-vaccines-halting-covid-outbreaks-in-nursing-homes',
        'https://nationalpost.com/news/local-news/dr-henry-says-oxford-astrazeneca-vaccine-is-safe-despite-reports-of-blood-clots/wcm/418d9855-2d97-4aa7-aef9-ca6b0bab04d9',
        'https://nationalpost.com/news/canada/officials-seek-to-convince-skeptical-public-of-vaccine-safety',
        'https://nationalpost.com/opinion/confused-about-vaccine-safety-and-efficacy-an-infectious-disease-expert-answers-some-common-questions',
        'https://nationalpost.com/news/canada/vaccine-advisers-set-to-provide-guidance-on-mixing-astrazeneca-mrna-vaccines-today',
        'https://nationalpost.com/news/canada/unvaccinated-albertans-are-majority-of-covid-cases-hospitalizations-deaths-hinshaw',
        'https://nationalpost.com/news/world/the-vaccinated-are-worried-and-scientists-dont-have-answers',
        'https://nationalpost.com/news/world/prince-harry-slams-mass-scale-misinformation-about-covid-19-vaccines/wcm/ef4c482c-5b5d-45ac-88b2-c266d22981f3',
        'https://nationalpost.com/news/canada/not-everyone-wants-a-pfizer-or-moderna-covid-vaccine-why-not-offer-them-something-else',
        'https://nationalpost.com/health/why-it-can-be-hard-to-prove-a-vaccine-caused-a-bad-outcome',
        'https://nationalpost.com/news/what-does-omicron-mean-for-canadas-vaccinated-majority'
    ]

    def parse(self, response, **kwargs):
        """Crawls through article and generates csv file with the articles:
                    - Date
                    - Title
                    - Text
        """
        full_date = response.css('.published-date__since::text').get()
        date = full_date.split(' ')[0] + '_' + full_date.split(' ')[2]
        title = response.css('title::text').get()
        text = response.css('.article-content__content-group p::text').getall()
        filename = f'national-post{date}.csv'
        with open(filename, 'w') as f:
            f.write(str(date) + '\n' + str(title) + '\n' + str(text))
