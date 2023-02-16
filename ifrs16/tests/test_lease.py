from datetime import datetime
import pytest
from ifrs16.core.lease import Lease


class TestLease:
    def test_set_dates_strings(self):
        lease = Lease(start_date='01/01/2022', end_date='01/01/2023')
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_set_dates_datetimes(self):
        lease = Lease(
            start_date=datetime(2022, 1, 1), end_date=datetime(2023, 1, 1)
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_set_dates_string_datetime(self):
        lease = Lease(
            start_date='01/01/2022', end_date=datetime(2023, 1, 1)
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_set_dates_datetime_string(self):
        lease = Lease(
            start_date=datetime(2022, 1, 1), end_date='01/01/2023'
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_set_dates_invalid_types(self):
        with pytest.raises(TypeError):
            # incorrect integer `end_date` is neither string or datetime
            Lease(start_date='01/01/2022', end_date=42)

    def test_set_dates_invalid_format(self):
        with pytest.raises(ValueError):
            # incorrect format for `end_date`
            Lease(start_date='01/01/2022', end_date='2023-01-01')
