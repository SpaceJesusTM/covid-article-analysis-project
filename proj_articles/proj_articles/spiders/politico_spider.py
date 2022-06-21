"""
This file contains the class responsible for scraping all Political articles.
"""
import scrapy


class Polispider(scrapy.Spider):
    """Spider Class for Politico Articles"""
    name = "politico"
    start_urls = [
        'https://www.politico.com/news/2020/12/26/coronavirus-vaccines-astrazeneca-johnson-450407',
        'https://www.politico.com/news/2021/01/30/biden-covid-vaccine-states-463953',
        'https://www.politico.com/news/2021/02/15/social-media-anti-vaxxers-468946',
        'https://www.politico.com/newsletters/women-rule/2021/03/26/the-myth-about-women-and-the-covid-19-vaccine-that-wont-die-492263',
        # 'https://www.politico.com/news/2021/04/22/biden-officials-johnson-vaccine-484356'
        # 'https://www.politico.com/news/2021/05/05/moderna-booster-shots-effective-covid-485467',
        'https://www.politico.com/news/2021/06/14/anti-vax-groups-covid-victories-493482',
        'https://www.politico.com/news/2021/07/07/biden-covid-vaccine-push-498479',
        'https://www.politico.com/news/2021/08/24/cdc-studies-vaccine-immunity-506782',
        'https://www.politico.com/news/2021/09/17/cdc-study-finds-moderna-vaccine-is-best-at-preventing-covid-19-hospitalization-512565',
        'https://www.politico.com/newsletters/politico-nightly/2021/10/13/the-hopkins-doc-vs-the-vaccine-consensus-494692',
        'https://www.politico.com/news/2021/11/29/omicron-coronavirus-booster-cdc-523481',
        'https://www.politico.com/newsletters/politico-nightly/2021/12/10/infection-protection-vs-the-vax-495426'
    ]

    # def parse(self, response, **kwargs):
    #     date = response.css('.timestamp time::text').get()
    #     if date is None:
    #         date = response.css('.story-meta__timestamp time::text').get()
    #     yield {
    #         'title': response.css('title::text').get(),
    #         'date': date,
    #         'text': response.css('.story-text p::text').getall()
    #     }

    def parse(self, response, **kwargs):
        """Crawls through article and generates csv file with the articles:
                    - Date
                    - Title
                    - Text
        """
        full_date = response.css('.timestamp time::text').get()

        if full_date is None:
            full_date = response.css('.story-meta__timestamp time::text').get()

        date = full_date.split(' ')[0]
        title = response.css('title::text').get()
        text = response.css('.story-text p::text').getall()
        filename = f'politico{title[0:6]}.csv'
        with open(filename, 'w') as f:
            f.write(str(date) + '\n' + str(title) + '\n' + str(text))

    # test 1 date comes out as str
    # def parse(self, response, **kwargs):
    #     date = response.css('.timestamp time::text').get()
    #     yield {
    #         'title': response.css('title::text').get(),
    #         'date': date,
    #         'text': response.css('.story-text p::text').getall()
    #     }

    # test 2 date come out as str
    # def parse(self, response, **kwargs):
    #     date = response.css('.story-meta__timestamp time::text').get()
    #     yield {
    #         'title': response.css('title::text').get(),
    #         'date': date,
    #         'text': response.css('.story-text p::text').getall()
    #     }
