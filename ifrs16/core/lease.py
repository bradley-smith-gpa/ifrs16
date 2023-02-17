from datetime import datetime
from ifrs16.core.exceptions import StartDateAfterEndDateError


class Lease:
    def __init__(self, start_date, end_date):
        self._set_dates(start_date, end_date)
        self.term = self.end_date - self.start_date

    def _set_dates(self, start_date, end_date):
        raw_dates = {'start_date': start_date, 'end_date': end_date}
        dates = {}
        for attr, raw_date in raw_dates.items():
            try:
                date = datetime.strptime(raw_date, '%d/%m/%Y')
            except TypeError as exc:
                if isinstance(raw_date, datetime):
                    date = raw_date
                else:
                    raise exc
            dates.update({attr: date})
        if dates['start_date'] > dates['end_date']:
            raise StartDateAfterEndDateError(dates)
        for attr, date in dates.items():
            setattr(self, attr, date)
