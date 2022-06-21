"""
This file contains the class responsible for scraping all CNN articles.
"""
import scrapy


class CNNspider(scrapy.Spider):
    """Spider Class for CNN Articles"""
    name = "CNN"
    start_urls = [
        'https://www.cnn.com/2020/12/21/politics/bidens-coronavirus-vaccination/index.html',
        'https://www.cnn.com/2021/01/25/health/anti-vaccine-theories-undermine-vaccination/index.html',
        'https://www.cnn.com/2021/02/18/opinions/pregnant-teacher-covid-19-vaccine-nyczak/index.html',
        'https://www.cnn.com/2021/03/20/health/variant-b117-vaccines-work/index.html',
        'https://www.cnn.com/2021/04/29/health/fda-approval-covid-19-vaccines-explainer/index.html',
        'https://www.cnn.com/2021/05/05/health/young-people-covid-vaccine/index.html',
        'https://www.cnn.com/2021/06/03/politics/free-beer-covid-vaccine-shots-joe-biden/index.html',
        'https://www.cnn.com/2021/07/02/china/vaccines-sinovac-sinopharm-intl-hnk-dst/index.html',
        'https://www.cnn.com/2021/07/31/health/fully-vaccinated-people-breakthrough-hospitalization-death/index.html',
        'https://www.cnn.com/2021/09/16/health/us-coronavirus-thursday/index.html',
        'https://www.cnn.com/2021/10/19/health/pfizer-vaccine-effectiveness-hospitalization-kids/index.html',
        'https://www.cnn.com/2021/11/19/europe/europe-covid-vaccination-rates-fourth-wave-cmd-intl/index.html',
        'https://www.cnn.com/2021/12/07/health/omicron-variant-pfizer-vaccine-south-africa-study/index.html'
    ]

    def parse(self, response, **kwargs):
        """Crawls through article and generates csv file with the articles:
            - Date
            - Title
            - Text
        """
        full_date = response.css('.update-time::text').get()
        date = full_date.split(' ')[5] + '_' + full_date.split(' ')[6] + '_' + full_date.split(' ')[7]
        title = response.css('title::text').get()
        text = response.css('.zn-body__paragraph::text').getall()
        filename = f'CNN{date}.csv'
        with open(filename, 'w') as f:
            f.write(str(date) + '\n' + str(title) + '\n' + str(text))
