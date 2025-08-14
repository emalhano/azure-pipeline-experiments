from plotly.subplots import make_subplots
import pandas as pd

from utils.classes import LapDataCollector



def create_time_series_plot(*args) -> 'plotly.graph_objects.Figure':

    lap_data_collector = LapDataCollector(*args)

    channels = ["Speed", "Throttle", "Brake", "DRS", "nGear", "RPM"]

    is_data_missing = False
    for channel in channels:
        if channel not in lap_data_collector.lap_data.columns:
            is_data_missing = True
            break


    if is_data_missing:
        fig = make_subplots(rows=1, cols=1)
        fig.add_annotation(
            text="Data not available for the selected parameters.",
            showarrow=False,
            font=dict(size=20),
            align="center"
        )
        return fig
    
    else:

        fig = make_subplots(rows=len(channels), cols=1, shared_xaxes=True, vertical_spacing=0.)

        for channel in channels:
            fig.add_scatter(
                x=lap_data_collector.lap_data['Time'],
                y=lap_data_collector.lap_data[channel],
                mode='lines',
                name=channel,
                row=channels.index(channel)+1,
                col=1
            )

            fig.update_yaxes(title_text=channel, row=channels.index(channel)+1, col=1)

        fig.update_layout(
            height=800
        )

    return fig