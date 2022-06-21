"""
This file contains the class responsible for scraping all Toronto Star articles.
"""
import scrapy


class TSspider(scrapy.Spider):
    """Spider Class for Toronto Star Articles"""
    name = "torontostar"
    start_urls = [
        'https://www.thestar.com/news/canada/2020/12/14/todays-coronavirus-news-quebec-to-begin-inoculating-against-covid-19-as-first-vaccines-arrive.html',
        'https://www.thestar.com/opinion/contributors/2021/01/19/my-mom-says-shell-refuse-the-covid-19-vaccine-why-shes-was-once-neglected-by-canadas-health-system-when-she-almost-lost-her-life-how-can-she-trust-them-now.html',
        'https://www.thestar.com/news/city_hall/2021/02/23/tale-of-two-vaccine-roll-outs-covid-19-numbers-plummet-in-torontos-long-term-care-homes-while-ontarios-remain-stubbornly-high.html',
        'https://www.thestar.com/politics/federal/2021/03/29/canada-to-issue-new-guidelines-for-use-of-astrazenecas-covid-19-vaccine.html',
        'https://www.thestar.com/opinion/contributors/2021/04/17/understanding-the-blood-clot-issue-behind-the-astrazeneca-vaccine-and-its-safety.html',
        'https://www.thestar.com/opinion/contributors/2021/05/11/why-pregnant-people-should-consider-getting-the-covid-19-vaccine.html',
        'https://www.thestar.com/politics/political-opinion/2021/06/27/health-care-workers-who-dont-believe-in-vaccines-are-in-the-wrong-job.html',
        'https://www.thestar.com/entertainment/opinion/2021/07/30/sharon-stone-and-sean-penn-are-correct-getting-vaccinated-against-covid-19-isnt-about-personal-freedom-its-about-community-safety.html',
        'https://www.thestar.com/news/gta/2021/08/08/should-covid-19-vaccines-be-mandatory-inside-our-contentious-history-with-forced-immunization.html',
        'https://www.thestar.com/news/canada/2021/09/30/covid-19-vaccines-highly-effective-over-time-according-to-new-quebec-study.html',
        'https://www.thestar.com/news/world/2021/10/29/is-the-covid-19-vaccine-safe-for-children.html',
        'https://www.thestar.com/news/canada/2021/11/25/have-a-safe-christmas-by-getting-vaccinated-says-indigenous-health-expert.html',
        'https://www.thestar.com/life/health_wellness/2021/12/08/vaccine-protection-against-omicron-variant-still-largely-unknown-experts.html'
    ]

    def parse(self, response, **kwargs):
        """Crawls through article and generates csv file with the articles:
                    - Date
                    - Title
                    - Text
        """
        full_date = response.css('.article__published-date::text').get()
        date = full_date.split(' ')[1] + '_' + full_date.split(' ')[2] + '_' + full_date.split(' ')[3]
        title = response.css('title::text').get()
        text = response.css('.c-article-body__content  p::text').getall()
        filename = f'toronto-star{date}.csv'
        with open(filename, 'w') as f:
            f.write(str(date) + '\n' + str(title) + '\n' + str(text))
