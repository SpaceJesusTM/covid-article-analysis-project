"""Data analysis and interactive plot generation file for CSC110 Final Project"""
import csv
import pandas as pd
import plotly.express as px


def clean_raw_csv(filename: str) -> None:
    """Clean the csv files by reordering the columns to match.
    """
    df = pd.read_csv(filename)

    df_reorder = df[['date', 'total_vaccinations', 'people_vaccinated',
                     'people_fully_vaccinated', 'total_boosters', 'location', 'source_url',
                     'vaccine']]
    df_reorder.to_csv('reordered_' + filename, index=False)


def raw_data_reader_per_day(filename: str) -> list[list]:
    """Return a list of lists representing a row with the percent change in vaccination metrics
        (total_vaccinations, ppl_vaccinated, ppl_fully_vaccinated) per day.
        """

    data = []
    header = ['date', 'total_vaccinations', 'ppl_vaccinated', 'ppl_fully_vaccinated']
    data.append(header)

    months = {12: 'Dec', 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul',
              8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov'}

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            if row[1] != '0' and row[2] != '0' and row[3] != '0':
                if 'yesterday' not in locals():
                    yesterday = row.copy()
                else:
                    month = months[int(row[0][5:7])]
                    day = row[0][8:10]
                    year = row[0][0:4]
                    date = month + ' ' + day + ', ' + year

                    total_vacc = int(row[1]) / int(yesterday[1]) - 1.0
                    ppl_vacc = int(row[2]) / int(yesterday[2]) - 1.0
                    ppl_fully = int(row[3]) / int(yesterday[3]) - 1.0
                    data.append([date, total_vacc, ppl_vacc, ppl_fully])

                    yesterday = row.copy()

    return data


def csv_writer(filename: str, data: list[list]) -> None:
    """Write a csv file containing the percent change data named the given filename."""
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerows(data)


def vacc_plot_line(filename: str, country: str) -> None:
    """Plot the percent change in vaccine data from the csv file named filename.

    The graph produced contains percent change of three attributes: total_vaccinations,
    total_vaccinated, total_fully_vaccinated.
    """
    df = pd.read_csv(filename)

    fig = px.line(df, x='date', y=df.columns[1:4], title=country + ' - Vaccine Data - Daily Percent Change')
    fig.show()
    fig.write_html(filename + '.html')


def vacc_plot_bar(filename: str, country: str) -> None:
    """Plot the graph representing the total vaccine metrics directly from the raw csv data."""
    df = pd.read_csv(filename)

    fig = px.bar(df, x='date', y=['total_vaccinations', 'people_vaccinated',
                                  'people_fully_vaccinated'],
                 title=country + ' - Vaccine Data: Total Numbers')
    fig.show()
    fig.write_html(filename + '.html')


def vaccine_dict_to_csv(canada: dict[str, float], us: dict[str, float], filename: str) -> None:
    """Create a csv file named filename containing the given dictionary data.

    Preconditions:
      - all(date in us for date in canada)
    """
    rows = []

    for date in canada:
        rows.append([date, canada[date], us[date]])

    rows.sort()
    rows.insert(0, ['date', 'canada', 'us'])

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)


def vader_dict_to_csv(compound: dict[str, float], positive: dict[str, float],
                      negative: dict[str, float], filename: str) -> None:
    """Create a csv file named filename containing the compiled data from three given dictionaries.

    Preconditions:
      - all(date in positive for date in compound)
      - all(date in negative for date in compound)
    """
    rows = []

    for date in compound:
        rows.append([date, compound[date], positive[date], negative[date]])

    rows.sort()
    rows.insert(0, ['date', 'vader_compound_score', 'vader_positive_ratio', 'vader_negative_ratio'])

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)


def plot_sentiment_analysis(filename: str, title: str) -> None:
    """Plot a vaccine-based or VADER-based sentiment analysis graph.
    """
    df = pd.read_csv(filename)

    fig = px.line(df, x='date', y=df.columns[1:4], title=title)
    fig.show()
    fig.write_html(filename + '.html')


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'csv', 'plotly.express'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
