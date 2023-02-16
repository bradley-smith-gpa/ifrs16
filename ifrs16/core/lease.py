from datetime import datetime


class Lease:
    def __init__(self, start_date, end_date):
        self._set_dates(start_date, end_date)

    def _set_dates(self, start_date, end_date):
        raw_dates = {'start_date': start_date, 'end_date': end_date}
        for attr, raw_date in raw_dates.items():
            try:
                date = datetime.strptime(raw_date, '%d/%m/%Y')
            except TypeError as exc:
                if isinstance(raw_date, datetime):
                    date = raw_date
                else:
                    raise exc
            setattr(self, attr, date)
