"""
Main file for CSC110 Final Project
"""
import sentiment_process as sp
import data_analysis as da

canada_files = ['national-postApr_2021.csv', 'national-postAug_2021.csv',
                'national-postDec_2020.csv', 'national-postDec_2021.csv',
                'national-postFeb_2021.csv', 'national-postJan_2021.csv',
                'national-postJul_2021.csv', 'national-postJun_2021.csv',
                'national-postMar_2021.csv', 'national-postMay_2021.csv',
                'national-postNov_2021.csv', 'national-postOct_2021.csv',
                'national-postSep_2021.csv', 'toronto-starApril_17__2021.csv',
                'toronto-starAug._8__2021.csv', 'toronto-starDec._8__2021.csv',
                'toronto-starDec._14__2020.csv', 'toronto-starFeb._23__2021.csv',
                'toronto-starJan._25__2021.csv', 'toronto-starJuly_30__2021.csv',
                'toronto-starJune_27__2021.csv', 'toronto-starMarch_29__2021.csv',
                'toronto-starMay_11__2021.csv', 'toronto-starNov._25__2021.csv',
                'toronto-starOct._29__2021.csv', 'toronto-starSept._30__2021.csv',
                'vancouver-sunApr_2021.csv', 'vancouver-sunAug_2021.csv',
                'vancouver-sunDec_2020.csv', 'vancouver-sunDec_2021.csv',
                'vancouver-sunFeb_2021.csv', 'vancouver-sunJan_2021.csv',
                'vancouver-sunJul_2021.csv', 'vancouver-sunJun_2021.csv',
                'vancouver-sunMar_2021.csv', 'vancouver-sunMay_2021.csv',
                'vancouver-sunNov_2021.csv', 'vancouver-sunOct_2021.csv',
                'vancouver-sunSep_2021.csv'
                ]

usa_files = ['politico_It_s.csv ', 'politicoAll_ad.csv',
             'politicoAnti-v.csv', 'politicoBiden_.csv',
             'politicoCDC_st.csv', 'politicoDoctor.csv',
             'politicoInfect.csv', 'politicoNew_CD.csv',
             'politicoThe_fi.csv', 'politicoThe_Ho.csv',
             'politicoThe_my.csv', 'CNNApril_30__2021.csv',
             'CNNAugust_2__2021.csv', 'CNNDecember_8__2021.csv',
             'CNNDecember_21__2020.csv', 'CNNFebruary_18__2021.csv',
             'CNNJanuary_25__2021.csv', 'CNNJuly_3__2021.csv',
             'CNNJune_3__2021.csv', 'CNNMarch_20__2021.csv',
             'CNNMay_19__2021.csv', 'CNNNovember_20__2021.csv',
             'CNNOctober_19__2021.csv', 'CNNSeptember_17__2021.csv',
             'fox-newsApril_7.csv', 'fox-newsAugust_15.csv',
             'fox-newsDecember_9.csv', 'fox-newsDecember_22.csv',
             'fox-newsFebruary_9.csv', 'fox-newsJanuary_31.csv',
             'fox-newsJuly_30.csv', 'fox-newsJune_23.csv',
             'fox-newsMarch_30.csv', 'fox-newsMay_23.csv',
             'fox-newsNovember_30.csv', 'fox-newsOctober_26.csv',
             'fox-newsSeptember_17.csv']


if __name__ == '__main__':
    ################################################################################################
    # Initialize Article class and create list of all articles
    print('Initializing Articles...')
    print()
    # CANADA ARTICLES
    canada_articles = []
    for title in canada_files:
        canada_articles.append(sp.read_article_csv(title))

    # USA ARTICLES
    usa_articles = []
    for title in usa_files:
        usa_articles.append(sp.read_article_csv(title))

    ################################################################################################
    # CANADA VADER COMPOUND SENTIMENT SCORES
    canada_sentiment = []
    for idx in range(len(canada_articles)):
        canada_sentiment.append((canada_articles[idx].date,
                                 (sp.VaderSentiment(canada_articles[idx]).general_sentiment())))

    canada_average_compound = dict()

    for article in canada_sentiment:
        if article[0] not in canada_average_compound:
            canada_average_compound[article[0]] = []
        canada_average_compound.setdefault(article[0], []).append(article[1])

    for sentiment_scores in canada_average_compound:
        canada_average_compound[sentiment_scores] = sum(canada_average_compound[sentiment_scores]) \
                                                    / len(canada_average_compound[sentiment_scores])

    print('10% Loaded...')
    print('Canada Vader Compound Sentiment Scores')
    print(canada_average_compound)
    print()

    # CANADA VADER POSITIVE RATIO
    canada_sentiment = []
    for idx in range(len(canada_articles)):
        canada_sentiment.append((canada_articles[idx].date,
                                 (sp.VaderSentiment(canada_articles[idx]).positive_ratio())))

    canada_average_positive = dict()

    for article in canada_sentiment:
        if article[0] not in canada_average_positive:
            canada_average_positive[article[0]] = []
        canada_average_positive.setdefault(article[0], []).append(article[1])

    for sentiment_scores in canada_average_positive:
        canada_average_positive[sentiment_scores] = sum(canada_average_positive[sentiment_scores])\
                                                    / len(canada_average_positive[sentiment_scores])

    print('20% Loaded...')
    print('Canada Vader Positive Ratio')
    print(canada_average_positive)
    print()

    # CANADA VADER NEGATIVE RATIO
    canada_sentiment = []
    for idx in range(len(canada_articles)):
        canada_sentiment.append((canada_articles[idx].date,
                                 (sp.VaderSentiment(canada_articles[idx]).negative_ratio())))

    canada_average_negative = dict()

    for article in canada_sentiment:
        if article[0] not in canada_average_negative:
            canada_average_negative[article[0]] = []
        canada_average_negative.setdefault(article[0], []).append(article[1])

    for sentiment_scores in canada_average_negative:
        canada_average_negative[sentiment_scores] = sum(canada_average_negative[sentiment_scores]) \
                                                    / len(canada_average_negative[sentiment_scores])

    print('30% Loaded...')
    print('Canada Vader Negative Ratio')
    print(canada_average_negative)
    print()

    ################################################################################################
    # USA VADER COMPOUND SENTIMENT SCORES
    usa_sentiment = []
    for idx in range(len(usa_articles)):
        usa_sentiment.append((usa_articles[idx].date,
                              (sp.VaderSentiment(usa_articles[idx]).general_sentiment())))

    usa_average_compound = dict()

    for article in usa_sentiment:
        if article[0] not in usa_average_compound:
            usa_average_compound[article[0]] = []
        usa_average_compound.setdefault(article[0], []).append(article[1])

    for sentiment_scores in usa_average_compound:
        usa_average_compound[sentiment_scores] = sum(usa_average_compound[sentiment_scores]) / \
                                                 len(usa_average_compound[sentiment_scores])

    print('40% Loaded...')
    print('USA Vader Compound Sentiment Scores')
    print(usa_average_compound)
    print()

    # USA VADER POSITIVE RATIO
    usa_sentiment = []
    for idx in range(len(usa_articles)):
        usa_sentiment.append((usa_articles[idx].date,
                              (sp.VaderSentiment(usa_articles[idx]).positive_ratio())))

    usa_average_positive = dict()

    for article in usa_sentiment:
        if article[0] not in usa_average_positive:
            usa_average_positive[article[0]] = []
        usa_average_positive.setdefault(article[0], []).append(article[1])

    for sentiment_scores in usa_average_positive:
        usa_average_positive[sentiment_scores] = sum(usa_average_positive[sentiment_scores]) / \
                                                 len(usa_average_positive[sentiment_scores])

    print('50% Loaded...')
    print('USA Vader Positive Ratio')
    print(usa_average_positive)
    print()

    # USA VADER NEGATIVE RATIO
    usa_sentiment = []
    for idx in range(len(usa_articles)):
        usa_sentiment.append((usa_articles[idx].date,
                              (sp.VaderSentiment(usa_articles[idx]).negative_ratio())))

    usa_average_negative = dict()

    for article in usa_sentiment:
        if article[0] not in usa_average_negative:
            usa_average_negative[article[0]] = []
        usa_average_negative.setdefault(article[0], []).append(article[1])

    for sentiment_scores in usa_average_negative:
        usa_average_negative[sentiment_scores] = sum(usa_average_negative[sentiment_scores]) / \
                                                 len(usa_average_negative[sentiment_scores])

    print('60% Loaded...')
    print('USA Vader Negative Ratio')
    print(usa_average_negative)
    print()

    ################################################################################################
    # CANADA VACCINE SENTIMENT SCORES
    canada_sentiment = []
    for idx in range(len(canada_articles)):
        canada_sentiment.append((canada_articles[idx].date,
                                 (sp.covid_vac_sentiment(canada_articles[idx],
                                                         sp.get_lexicon())[1])))

    canada_average_cvac = dict()

    for article in canada_sentiment:
        if article[0] not in canada_average_cvac:
            canada_average_cvac[article[0]] = []
        canada_average_cvac.setdefault(article[0], []).append(article[1])

    for sentiment_scores in canada_average_cvac:
        canada_average_cvac[sentiment_scores] = sum(canada_average_cvac[sentiment_scores]) / \
                                                len(canada_average_cvac[sentiment_scores])

    print('70% Loaded...')
    print('Canada Vaccine Sentiment Scores')
    print(canada_average_cvac)
    print()

    # USA VACCINE SENTIMENT SCORES
    usa_sentiment = []
    for idx in range(len(usa_articles)):
        usa_sentiment.append((usa_articles[idx].date,
                              (sp.covid_vac_sentiment(usa_articles[idx],
                                                      sp.get_lexicon())[1])))
    usa_average_cvac = dict()

    for article in usa_sentiment:
        if article[0] not in usa_average_cvac:
            usa_average_cvac[article[0]] = []
        usa_average_cvac.setdefault(article[0], []).append(article[1])

    for sentiment_scores in usa_average_cvac:
        usa_average_cvac[sentiment_scores] = sum(usa_average_cvac[sentiment_scores]) / \
                                             len(usa_average_cvac[sentiment_scores])

    print('80% Loaded...')
    print('USA Vaccine Sentiment Scores')
    print(usa_average_cvac)
    print()

    ################################################################################################
    # Sentiment Dictionaries to Graphs
    # cleaned csv files have prefix 'reordered_'
    da.clean_raw_csv('Canada.csv')
    da.clean_raw_csv('United States.csv')

    da.vacc_plot_bar('Canada.csv', 'Canada')
    da.vacc_plot_bar('United States.csv', 'US')

    canada_vacc_data = da.raw_data_reader_per_day('reordered_Canada.csv')
    us_vacc_data = da.raw_data_reader_per_day('reordered_United States.csv')

    da.csv_writer('cananda_vacc_data.csv', canada_vacc_data)
    da.csv_writer('us_vacc_data.csv', us_vacc_data)

    da.vacc_plot_line('cananda_vacc_data.csv', 'Canada')
    da.vacc_plot_line('us_vacc_data.csv', 'US')

    da.vaccine_dict_to_csv(canada_average_cvac, usa_average_cvac, 'our_sentiment.csv')

    da.vader_dict_to_csv(canada_average_compound, canada_average_positive, canada_average_negative,
                         'canada_vader.csv')
    da.vader_dict_to_csv(usa_average_compound, usa_average_positive, usa_average_negative,
                         'us_vader.csv')

    da.plot_sentiment_analysis('our_sentiment.csv', 'Average Article Vaccine Sentiment per Month')
    da.plot_sentiment_analysis('canada_vader.csv', 'Canada - VADER sentiment analysis')
    da.plot_sentiment_analysis('us_vader.csv', 'US - VADER sentiment analysis')

    print('100% Loaded...')
    print('Please check your browser for the graphs.')
    print()

    ################################################################################################
    # Example Calls of sentiment_process module functions
    for idx in range(len(canada_articles)):
        print('canada_articles[' + str(idx) + ']:', canada_articles[idx].title, '-',
              canada_articles[idx].date)

    for idx in range(len(usa_articles)):
        print('usa_articles[' + str(idx) + ']:', usa_articles[idx].title, '-',
              usa_articles[idx].date)
    print()

    # Example of Vader Sentiment call
    vader_art = sp.VaderSentiment(canada_articles[0])
    vader_art.full_analysis()

    # Example of Covid Vaccine Sentiment call
    print()
    print(sp.covid_vac_sentiment(canada_articles[0], sp.get_lexicon())[0].title)
    print('Vaccine Sentiment Score:', sp.covid_vac_sentiment(canada_articles[0], sp.get_lexicon())[1])

    # For a different article use 'canada_articles[x]' or 'usa_articles[y]'
    # where 0 <= x <= 38 and 0 <= y <= 36

