import numpy as np
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair

def outbreak(plot_type, r, month, countries, social_distancing):
    months = ["January", "February", "March", "April", "May"]
    m = months.index(month)
    start_day = 30 * m
    final_day = 30 * (m + 1)
    x = np.arange(start_day, final_day + 1)
    pop_count = {"USA": 350, "Canada": 40, "Mexico": 300, "UK": 120}
    if social_distancing:
        r = sqrt(r)
    df = pd.DataFrame({"day": x})
    for country in countries:
        df[country] = x ** (r) * (pop_count[country] + 1)

    if plot_type == "Matplotlib":
        fig = plt.figure()
        plt.plot(df["day"], df[countries].to_numpy())
        plt.title("Outbreak in " + month)
        plt.ylabel("Cases")
        plt.xlabel("Days since Day 0")
        plt.legend(countries)
        return fig
    elif plot_type == "Plotly":
        fig = px.line(df, x="day", y=countries)
        fig.update_layout(
            title="Outbreak in " + month,
            xaxis_title="Cases",
            yaxis_title="Days Since Day 0",
        )
        return fig
    elif plot_type == "Altair":
        df = df.melt(id_vars="day").rename(columns={"variable": "country"})
        fig = altair.Chart(df).mark_line().encode(x="day", y='value', color='country')
        return fig
    else:
        raise ValueError("A plot type must be selected")