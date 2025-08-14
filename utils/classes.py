import pandas as pd
import fastf1





class LapDataCollector:

    def __init__(self, year, event, session, driver):

        self._year = year
        self._event = event
        self._session = session
        self._driver = driver

        if year is None or event is None or session is None or driver is None:
            self._lap_data = pd.DataFrame()
        else:
            self._session_object = fastf1.get_session(year, event, session)
            self._session_object.load()

            self._lap_meta_data = self._session_object.laps.pick_drivers(driver).pick_fastest()
            self._lap_data = self._lap_meta_data.get_car_data()


    @property
    def lap_data(self):
        return self._lap_data

    @property
    def lap_meta_data(self):
        return self._lap_meta_data