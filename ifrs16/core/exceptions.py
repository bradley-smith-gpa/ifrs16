class StartDateAfterEndDateError(Exception):
    '''Lease start date is after the end date.'''
    def __init__(self, dates):
        self.start_date = dates['start_date']
        self.end_date = dates['end_date']
        self.message = (
            f'Lease start date {self.start_date} is after the end date'
            f' {self.end_date}'
        )
        super().__init__(self.message)


class InvalidTenureError(Exception):
    '''Tenure argument provided is not valid.'''
    def __init__(self, tenure, valid_tenure_choices):
        self.tenure = tenure
        self.valid_tenure_choices = valid_tenure_choices
        self.message = (
            f'Given tenure {self.tenure} is invalid. Choose from the following'
            f' choices instead: {self.valid_tenure_choices}'
        )
        super().__init__(self.message)
