import pandas as pd
import fastf1





class LapDataCollector:

    def __init__(self, year, event, session, driver):
        self._year = year
        self._event = event
        self._session = session
        self._driver = driver
        self._lap_data = pd.DataFrame()

        self._session = fastf1.get_session(year, event, session)