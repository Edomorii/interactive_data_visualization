import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
import json

def read_csv_file(file_path):
    return pd.read_csv(file_path)

def first_vis():
    # CLIMATE CHANGE , source : https://climatedata.imf.org/pages/climatechange-data
    file_path = 'climate_change.csv'
    climate_data = read_csv_file(file_path)
    years = []
    for i in range(1961,2023,1) :
        years.append('F'+str(i))

    climate_data = climate_data[years]
    average_data = []
    for i in years:
        average_data.append(climate_data[i].mean())
    def plot_line_chart(x_data, y_data, title="Global Annual Change in Surface Temperature (°C)"):
        plt.figure(figsize=(15, 10))
        plt.plot(x_data, y_data, linewidth = 2.5, color = '#2F4858')
        plt.title(title, fontsize = 20)
        plt.axhline(0, color='#86BBD8', linewidth=1.25, linestyle='--')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='both', length=0)
        ax.set_xlim(0, len(x_data))
        ax.xaxis.set_major_locator(MultipleLocator(10)) 
        plt.show()
    plot_line_chart(x_data = [i.split('F')[1] for i in years], y_data=average_data)

def second_vis():
    # BLACK AND WHITE, source : https://data.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?locations=IT
    inflation_raw_data = read_csv_file('inflation.csv')
    inflation_data_italy = inflation_raw_data[inflation_raw_data['Country Code']== 'ITA']
    years = [str(i) for i in range(1961,2023,1)]
    inflation_data_italy = inflation_data_italy[years]
    inflation = [inflation_data_italy[i] for i in years]
    def plot_line_chart(x_data, y_data, title="Annual Inflation Rate in Italy"):
        plt.figure(figsize=(15, 10), facecolor = 'black')
        plt.axes(facecolor='black')
        plt.plot(x_data, y_data, linewidth = 2.5, color = '#FFFFFF')
        plt.title(title, fontsize = 20, color ='#FFFFFF')
        plt.xticks(color ='#FFFFFF')
        plt.yticks(color ='#FFFFFF')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.tick_params(axis='both', length=0)
        ax.set_xlim(0, len(x_data))
        ax.xaxis.set_major_locator(MultipleLocator(10)) 
        plt.show()
    plot_line_chart(x_data = years, y_data=inflation)

def third_vis():
    # COLOR AS AN IMPORTANT AESTETHICS, source = https://finance.yahoo.com/quote/ARKK/holdings/
    labels = ['Technology', 'Healthcare', 'Communication Services', 'Financial Services','Other']
    data = [32.99, 25.02, 16.15, 14.53,11.31] 
    def plot_pie_chart(labels, data, title="ARKK ETF Allocation by Sector"):
        plt.figure(figsize=(15, 10))
        plt.pie(
            data, 
            labels=labels, 
            colors=['red', 'green', 'blue', 'yellow','purple'], 
            wedgeprops=dict(edgecolor='white', linewidth=2),
        )

        plt.title(title, fontsize=20)

        fig = plt.gcf()

        plt.axis('equal')  

        plt.show()

    plot_pie_chart(labels=labels,data=data)

def forth_vis():
    # MERGED DATA, sources = https://fred.stlouisfed.org/series/FEDFUNDS , https://finance.yahoo.com/quote/SPY?p=SPY
    interest_raw_data = read_csv_file('FEDFUNDS.csv')
    sp500_raw_data = read_csv_file('SPY.csv')

    dates = [i for i in sp500_raw_data['Date']]
    sp_data = [i for i in sp500_raw_data['Adj Close']]
    interest_data = [interest_raw_data['fed'][i] for i in range(len(dates)) ]
    def plot_financial_data(dates, sp_data, interest_data):
        fig, ax1 = plt.subplots()
        plt.figure(figsize=(15, 10))
        color = 'tab:red'
        ax1.set_ylabel('SPY Price (US Dollars)', color=color)
        ax1.plot(dates, sp_data, color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax2 = ax1.twinx()  
        color = 'tab:blue'
        ax2.set_ylabel('Fed Interest Rate (Percentage)', color=color)
        ax2.plot(dates, interest_data, color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        ax1.xaxis.set_major_locator(MultipleLocator(60)) 
        fig.tight_layout()
        ax1.spines['top'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax1.tick_params(axis='both', length=0)
        ax2.tick_params(axis='both', length=0)
        plt.show()
    plot_financial_data(dates,sp_data,interest_data)

def fifth_vis():
    # DATA TO INK RATIO source : https://www.imf.org/external/datamapper/NGDPDPC@WEO/OEMDC/ADVEC/WEOWORLD
    countries = ['Luxembourg','Ireland','Switzerland','Norway','Singapore','Iceland','Qatar','United States','Denmark','Macao SAR']
    gdp_per_capita = [140.31, 117.98, 110.25, 102.46, 91.73, 87.87, 84.9, 83.06, 72.94, 70.13]
    def plot_bar_chart(countries, gdp_per_capita):
        colors = ['gray' if country != 'Switzerland' else 'skyblue' for country in countries]
        plt.figure(figsize=(15, 10))
        bars = plt.barh(countries, gdp_per_capita, color=colors)

        plt.grid(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(True)
        ax = plt.gca()
        ax.tick_params(axis='both', length=0)
        plt.gca().axes.get_xaxis().set_visible(False)

        for bar in bars:
            plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height() / 2,
                    f'{bar.get_width():.2f}', va='center', ha='right', color='white', fontsize=10)

        plt.title('GDP per Capita by Country (Thousand US Dollars)')
        plt.show()

    plot_bar_chart(countries,gdp_per_capita)

def sixth_vis():
    # Different Chart, source = https://data.worldbank.org/indicator/SI.DST.FRST.20?locations=CH
    labels = np.array(['          Fifth 20%', '      Fourth 20%', 'Third 20%          ', 'Second 20%           ', '      First 20%'])
    stats = np.array([7.5, 22.5, 16.8, 12.4, 40.8])
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats = np.concatenate((stats, [stats[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='skyblue', alpha=0.25)
    ax.plot(angles, stats, color='blue', linewidth=1)
    ax.set_yticklabels([])
    ax.set_ylim(0, max(stats) + 20) 
    ax.set_rlabel_position(90)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels, color='blue', fontsize=15)
    for angle, stat in zip(angles, stats[:-1]):
        ax.text(angle, stat + 10, str(stat)+'%', ha='center', va='center', fontsize=12, color='blue')
    plt.title('Income Share by Percentile in Switzerland', fontsize = 20, pad=30)
    plt.show()

def seventh_vis():
    # MAP, source = https://data.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?locations=IT
    data = read_csv_file('inflation.csv')
    fig = px.choropleth(data, locations='Country Code', color='2022', hover_name='Country Name',
                        projection='natural earth', 
                        title='Annual Inflation Rate by Country, 2022')
    fig.show()

def eighth_vis():
    # SWISS OPEN DATA, source = https://data.tg.ch/api/v2/catalog/datasets/dfs-ga-1/exports/json
    url = 'https://data.tg.ch/api/v2/catalog/datasets/dfs-ga-1/exports/json'
    dates = []
    cumulative_cases = []
    
    # Assuming the 'swiss_open_data.json' file is in the same directory as this script
    with open('swiss_open_data.json', 'r') as f:
        data = json.load(f)
        for i in data:
            dates.append(i['date'])
            cumulative_cases.append(i['ncumul_conf'])

    def plot_area_chart(x_data, y_data, title="Thurgau Canton Cumulative Covid-19 Cases"):
        plt.figure(figsize=(15, 10))
        plt.fill_between(x_data, y_data, color='green', alpha=0.7)
        plt.plot(x_data, y_data, color='darkgreen', linewidth=2.5)
        plt.title(title, fontsize=20)
        
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='both', length=0)
        ax.set_xlim(0, len(x_data))
        ax.xaxis.set_major_locator(MultipleLocator(90))
        
        plt.show()

    plot_area_chart(x_data=dates, y_data=cumulative_cases)

eighth_vis()

def ninth_vis():
    # INTERACTIVE CHART, source : https://finance.yahoo.com/quote/NESN.SW/history?p=NESN.SW
    nestle_data = pd.read_csv('NESN.SW.csv')
    
    nestle_data['Date'] = pd.to_datetime(nestle_data['Date'])
    fig = px.line(nestle_data, x='Date', y='Adj Close', title='Nestlé S.A. Stock Price')

    fig.update_traces(mode='lines', hoverinfo='x+y')

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Close Price (CHF)',
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
        plot_bgcolor='white',   
        paper_bgcolor='white',  
        xaxis_showgrid=False,   
        yaxis_showgrid=False,
        xaxis_linecolor='black', 
        yaxis_linecolor='black', 
        xaxis_ticks='outside',  
        yaxis_ticks='outside' 
    )

    fig.show()

ninth_vis()

def fromBad_ToGood():
    #improve a bad visualization
    countries = ['Netherlands', 'Average height in the World', 'Guatemala']
    values = [1.70, 1.59, 1.51]
    
    plt.figure(figsize=(6, 10))
    ax = plt.gca()
    
    plt.bar(countries, values, color='pink')
    
    plt.xlabel('Countries')
    plt.ylabel('Values (in meters)')
    plt.title('Tallest vs Shortest women in the World')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='both', length=0)
    
    # Set y-axis scale to 0.1
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7])
    
    plt.tight_layout()
    plt.show()

fromBad_ToGood()