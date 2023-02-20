from datetime import datetime
from dateutil.relativedelta import relativedelta
from ifrs16.core.exceptions import (
    StartDateAfterEndDateError, InvalidTenureError
)


class Lease:
    '''Basic lease object.'''
    valid_tenure_choices = ('leasehold', 'freehold')

    def __init__(self, start_date, end_date, tenure):
        '''Initialise lease object along with validation of args.'''
        self._set_dates(start_date, end_date)
        self.term = self.end_date - self.start_date
        self._set_tenure(tenure)

    def _set_dates(self, start_date, end_date):
        '''Set date attributes as datetimes if they are valid.'''
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

    def _set_tenure(self, tenure):
        '''Set tenure attributes if it is valid.'''
        if tenure in self.valid_tenure_choices:
            self.tenure = tenure
        else:
            raise InvalidTenureError(tenure, self.valid_tenure_choices)

    def is_short_term(self):
        '''Return `True` if lease duration is 12 months or less.'''
        threshold_date = self.end_date - relativedelta(months=12)
        is_short_term = (self.start_date >= threshold_date)
        return is_short_term
