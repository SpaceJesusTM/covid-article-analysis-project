"""
Covid Vaccine Sentiment Analysis
"""
import csv
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Article:
    """A class representing a news article dataclass.

        Instance Attributes:
        - text: the article data in string format
        - title: the article title in string format
        - date: the article date in string format

    >>> news_article = Article('This is an article', 'This is a Title', 'Sept, 12, 2021')
    >>> news_article.title
    'This is a Title'
    """
    text: str
    title: str
    date: str

    def __init__(self, text: str, title: str, date: str) -> None:
        """Initialize this article with the text of the article."""
        self.text = text
        self.title = title
        self.date = date


class VaderSentiment:
    """A class that takes an article and returns results of the
    Vader Sentiment Analysis.

        Instance Attributes:
        - analysis_text: the text to analyze
    """
    analysis_text: Article

    def __init__(self, analysis_text: Article) -> None:
        """Initialize this article with the text of the article."""
        self.analysis_text = analysis_text

    def general_sentiment(self) -> float:
        """Return the compound score of the Vader Sentiment from [-1:1]"""
        article_analyzer = SentimentIntensityAnalyzer()

        article_sentiment = article_analyzer.polarity_scores(self.analysis_text.text)

        return article_sentiment['compound']

    def positive_ratio(self) -> float:
        """Return the positive ratio of the Vader Sentiment from [0:1]"""
        article_analyzer = SentimentIntensityAnalyzer()

        article_sentiment = article_analyzer.polarity_scores(self.analysis_text.text)

        return article_sentiment['pos']

    def negative_ratio(self) -> float:
        """Return the negative ratio of the Vader Sentiment from [0:1]"""
        article_analyzer = SentimentIntensityAnalyzer()

        article_sentiment = article_analyzer.polarity_scores(self.analysis_text.text)

        return article_sentiment['neg']

    def neutral_ratio(self) -> float:
        """Return the neutral ratio of the Vader Sentiment from [0:1]"""
        article_analyzer = SentimentIntensityAnalyzer()

        article_sentiment = article_analyzer.polarity_scores(self.analysis_text.text)

        return article_sentiment['neu']

    def full_analysis(self) -> float:
        """Print and return all scores of the Vader Sentiment."""
        article_analyzer = SentimentIntensityAnalyzer()

        print('Article:', self.analysis_text.title, '-', self.analysis_text.date)
        print()

        article_sentiment = article_analyzer.polarity_scores(self.analysis_text.text)
        print("This articles sentiment dictionary is: ", article_sentiment)
        print()
        print("This article is rated ", article_sentiment['neu'] * 100, "% Neutral")
        print("Therefore the sentiment intensity of this article is rated at",
              (1 - article_sentiment['neu']) * 100, "%")
        print()
        print('Sentiment Breakdown:')
        print("This article is rated ", article_sentiment['neg'] * 100, "% negative and",
              article_sentiment['pos'] * 100, "% positive.")
        print()

        print("This article is overall rated As", end=" ")

        if article_sentiment['compound'] >= 0.05:
            print("POSITIVE.")

        elif article_sentiment['compound'] <= - 0.05:
            print("NEGATIVE.")

        else:
            print("NEUTRAL.")

        return article_sentiment


class PositiveNegativeSentiment:
    """A class that takes an article and returns results if the article
    has a positive or negative sentiment towards a specific topic
    using the provided lexicon.

        Instance Attributes:
        - analysis_text: the text to analyze
        - pos_neg_lexicon: the lexicon corresponding keywords to
        positive ('pos') or negative ('neg')
    """
    analysis_text: Article
    pos_neg_lexicon: dict

    def __init__(self, analysis_text: Article, pos_neg_dict: dict) -> None:
        """Initialize this article with the text of the article."""
        self.analysis_text = analysis_text
        self.pos_neg_lexicon = pos_neg_dict

    def clean_text(self) -> list[str]:
        """Return text as a list of words that have been cleaned up:
            - Punctuation removed
            - Text in lowercase
        """
        punctuation = '!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'

        for p in punctuation:
            text = str.replace(self.analysis_text.text, p, ' ')

        text = str.lower(text)

        return str.split(text)

    def article_sentiment(self) -> tuple[str, int, int]:
        """Return whether article is positive or negative and the number of positive/negative
         words based on given lexicon.
         format: ('pos', positive_count, negative_count)"""
        word_list = self.clean_text()
        positive_count = 0
        negative_count = 0

        for word in self.pos_neg_lexicon:
            if word in word_list:
                if self.pos_neg_lexicon[word] == 'pos':
                    positive_count += 1
                else:
                    negative_count += 1

        if negative_count >= positive_count:
            return 'neg', positive_count, negative_count
        else:
            return 'pos', positive_count, negative_count

    def count_keywords(self) -> dict[str, int]:
        """Return a frequency mapping of the lexicon in text.
        """
        # Accumulator Variable: A mapping of keyword frequencies seen so far
        occurrences_so_far = {}
        word_list = self.clean_text()

        for word in word_list:
            if word in self.pos_neg_lexicon:
                if word not in occurrences_so_far:
                    occurrences_so_far[word] = 0
                    occurrences_so_far[word] = occurrences_so_far[word] + 1
                else:
                    occurrences_so_far[word] = occurrences_so_far[word] + 1

        return occurrences_so_far


def get_lexicon() -> dict:
    """Extract a dictionary mapping keywords to sentiment from the lexicon.json file."""
    with open('lexicon.json') as file:
        data = json.load(file)
    return data


def covid_vac_sentiment(article: Article, covid_keywords: dict) -> tuple[Article, float]:
    """Return articles sentiment score on the Covid-19 Vaccine"""
    vsenti = VaderSentiment(article)
    pnsenti = PositiveNegativeSentiment(article, covid_keywords)

    if pnsenti.article_sentiment()[0] == 'pos':
        sentiment_score = 1 - vsenti.neutral_ratio()
    else:
        sentiment_score = (1 - vsenti.neutral_ratio()) * (- 1)

    return article, sentiment_score


# example_dict = {'safe': 'pos', 'severe': 'neg', ...}


def read_article_csv(file_name: str) -> Article:
    """Returned processed article csv file."""
    article_data = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            article_data.append(row)

    article = dict()

    article['date'] = str_2_date(str(article_data[0]))
    article['title'] = str(article_data[1])
    article['text'] = str(article_data[2])

    return Article(article['text'], article['title'], article['date'])


def str_2_date(date_str: str) -> str:
    """Returned Cleaned Up string date (month and year)

    >>> str_2_date('Sept, 20, 2021')
    '2021/09'
    """
    date = date_str.lower()
    months = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
              'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}

    for month in months:
        if month in date:
            if '2020' in date:
                return_date = '2020/' + months[month]
                return return_date
            else:
                return_date = '2021/' + months[month]
                return return_date


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['vaderSentiment', 'csv', 'json'],  # the names (strs) of imported modules
        'allowed-io': ['full_analysis', 'read_article_csv', 'get_lexicon'],
        # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
