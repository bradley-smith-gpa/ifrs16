class StartDateAfterEndDateError(Exception):
    '''Lease start date is after the end date'''
    def __init__(self, dates):
        self.start_date = dates['start_date']
        self.end_date = dates['end_date']
        self.message = (
            f'Lease start date {self.start_date} is after the end date'
            f' {self.end_date}'
        )
        super().__init__(self.message)
