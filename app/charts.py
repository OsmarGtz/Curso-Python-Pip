import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import plotly.express as px
import pandas as pd

plt.style.use('ggplot')

def generate_bar_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.title(title)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y:,.0f}'))
    plt.savefig(f'{title}.png')
    plt.close()

def generate_pie_chart(labels, values, title):
    df = pd.DataFrame({'labels': labels, 'values': values})
    fig = px.pie(df, names='labels', values='values', title=title)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.write_html(f'{title}.html')

if __name__ == "__main__":
    generate_bar_chart(['A', 'B', 'C'], [10, 20, 15], 'Bar Chart Example')
    generate_pie_chart(['A', 'B', 'C'], [10, 20, 15], 'Pie Chart Example')