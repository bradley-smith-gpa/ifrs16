from datetime import datetime
import pytest
from ifrs16.core.lease import Lease
from ifrs16.core.exceptions import StartDateAfterEndDateError


class TestSetDates:
    def test_both_strings(self):
        lease = Lease(start_date='01/01/2022', end_date='01/01/2023')
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_both_datetimes(self):
        lease = Lease(
            start_date=datetime(2022, 1, 1), end_date=datetime(2023, 1, 1)
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_string_and_datetime(self):
        lease = Lease(
            start_date='01/01/2022', end_date=datetime(2023, 1, 1)
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_datetime_and_string(self):
        lease = Lease(
            start_date=datetime(2022, 1, 1), end_date='01/01/2023'
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_invalid_types(self):
        with pytest.raises(TypeError):
            # incorrect integer `end_date` is neither string or datetime
            Lease(start_date='01/01/2022', end_date=42)

    def test_invalid_date_format(self):
        with pytest.raises(ValueError):
            # incorrect format for `end_date`
            Lease(start_date='01/01/2022', end_date='2023-01-01')

    def test_start_after_end_date(self):
        with pytest.raises(StartDateAfterEndDateError):
            Lease(start_date='02/01/2023', end_date='01/01/2023')


class TestTerm:
    def test_get_term(self):
        lease = Lease(start_date='01/01/2022', end_date='01/01/2023')
        expected_term = lease.end_date - lease.start_date
        assert lease.term == expected_term
