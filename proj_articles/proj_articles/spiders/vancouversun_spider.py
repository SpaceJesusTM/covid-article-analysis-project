"""
This file contains the class responsible for scraping all Vancouver Sun articles.
"""
import scrapy


class VSspider(scrapy.Spider):
    """Spider Class for Vancouver Sun Articles"""
    name = "vancouversun"
    start_urls = [
        'https://vancouversun.com/news/provincial/toronto-health-care-workers-to-receive-first-covid-19-vaccines-today/wcm/36dccb78-88d1-4972-8f97-0df1b88c7603',
        'https://vancouversun.com/health/covid-19-vaccine-not-mandatory-health-care-workers-encouraged-to-get-it',
        'https://vancouversun.com/news/canada/reason-to-celebrate-early-evidence-suggests-vaccines-halting-covid-outbreaks-in-nursing-homes/wcm/05efd26a-1674-4301-b8d1-932bdfb83c4a',
        'https://vancouversun.com/news/canada/trudeau-assures-that-astrazeneca-vaccine-is-safe-as-germany-italy-france-join-countries-halting-its-use',
        'https://vancouversun.com/news/covid-19-most-unvaccinated-canadians-uncomfortable-with-astrazeneca-shot-poll-shows',
        'https://vancouversun.com/news/local-news/covid-19-b-c-man-hospitalized-with-astrazeneca-vaccine-induced-blood-clot',
        'https://vancouversun.com/news/unvaccinated-the-implications-of-covid-19-vaccine-hesitancy',
        'https://vancouversun.com/news/six-people-injected-with-saline-instead-of-covid-vaccine-at-niagara-clinic',
        'https://vancouversun.com/news/with-the-rise-of-delta-are-vaccines-still-enough-to-end-the-pandemic',
        'https://vancouversun.com/news/mixing-covid-vaccines-offer-high-level-of-protection-bccdc-data',
        'https://vancouversun.com/news/world/study-suggests-pfizer-biontech-antibodies-disappear-in-many-by-seven-months/wcm/29e31d0f-a20a-4d94-bea4-fef6e23826c5',
        'https://vancouversun.com/news/local-news/covid-19-children-between-five-and-11-are-eligible-for-vaccinations-starting-monday',
        'https://vancouversun.com/news/what-does-omicron-mean-for-canadas-vaccinated-majority/wcm/b5cf53ae-426d-46f5-8a5f-eddfc427decb'
    ]

    # def parse(self, response, **kwargs):
    #     yield {
    #         'title': response.css('title::text').get(),
    #         'date': response.css('.published-date__since::text').get(),
    #         'text': response.css('.article-content__content-group p::text').getall()
    #     }

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
        filename = f'vancouver-sun{date}.csv'
        with open(filename, 'w') as f:
            f.write(str(date) + '\n' + str(title) + '\n' + str(text))
