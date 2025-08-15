import pandas as pd
import fastf1



class LapDataCollector:

    def __init__(self, year: int, event: int|str, session: str, driver: str) -> None:

        self._year = year
        self._event = event
        self._session = session
        self._driver = driver

        if year is None or event is None or session is None or driver is None:
            self._lap_meta_data = pd.DataFrame()
            self._lap_data = pd.DataFrame()
        else:
            with fastf1.Cache.disabled():
                self._session_object = fastf1.get_session(year, event, session)
                self._session_object.load()

                self._lap_meta_data = self._session_object.laps.pick_drivers(driver).pick_fastest()
                self._lap_data = self._lap_meta_data.get_car_data()


    @property
    def lap_data(self) -> pd.DataFrame:
        return self._lap_data

    @property
    def lap_meta_data(self) -> pd.DataFrame:
        return self._lap_meta_data