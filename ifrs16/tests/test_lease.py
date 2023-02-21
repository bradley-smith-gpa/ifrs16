from datetime import datetime
import pytest
from ifrs16.core.exceptions import (
    StartDateAfterEndDateError, InvalidTenureError
)
from ifrs16.tests.factories import LeaseFactory, OrganisationFactory


class TestSetDates:
    def test_both_strings(self):
        '''
        Lease date arguments passed in as correctly formatted strings are both
        set as datetime attributes.
        '''
        lease = LeaseFactory(start_date='01/01/2022', end_date='01/01/2023')
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_both_datetimes(self):
        '''
        Lease date arguments both passed in as datetimes are both set as
        datetime attributes.
        '''
        lease = LeaseFactory(
            start_date=datetime(2022, 1, 1), end_date=datetime(2023, 1, 1)
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_string_and_datetime(self):
        '''
        Lease date arguments where start date is a string but end date is a
        datetime are both set as datetime attributes.
        '''
        lease = LeaseFactory(
            start_date='01/01/2022', end_date=datetime(2023, 1, 1)
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_datetime_and_string(self):
        '''
        Lease date arguments where start date is a datetime but end date is a
        string are both set as datetime attributes.
        '''
        lease = LeaseFactory(
            start_date=datetime(2022, 1, 1), end_date='01/01/2023'
        )
        assert isinstance(lease.start_date, datetime)
        assert isinstance(lease.end_date, datetime)

    def test_invalid_types(self):
        '''Lease date argument of wrong type raises `TypeError`.'''
        with pytest.raises(TypeError):
            # incorrect integer `end_date` is neither string or datetime
            LeaseFactory(start_date='01/01/2022', end_date=42)

    def test_invalid_date_format(self):
        '''Lease date string with incorrect format raises `ValueError`.'''
        with pytest.raises(ValueError):
            # incorrect format for `end_date`
            LeaseFactory(start_date='01/01/2022', end_date='2023-01-01')

    def test_start_after_end_date(self):
        '''Start date after end date raises `StartDateAfterEndDateError`.'''
        with pytest.raises(StartDateAfterEndDateError):
            LeaseFactory(start_date='02/01/2023', end_date='01/01/2023')


class TestTerm:
    def test_get_term(self):
        '''Lease term is duration from start date to end date.'''
        lease = LeaseFactory(start_date='01/01/2022', end_date='01/01/2023')
        expected_term = lease.end_date - lease.start_date
        assert lease.term == expected_term


class TestShortTerm:
    def test_exact_short_term(self):
        '''Lease is short term when dates are exactly 12 months apart.'''
        lease = LeaseFactory(start_date='01/01/2022', end_date='01/01/2023')
        assert lease.is_short_term()

    def test_comfortably_short_term(self):
        '''
        Lease is short term when dates are clearly less than 12 months apart.
        '''
        lease = LeaseFactory(start_date='01/01/2022', end_date='01/05/2022')
        assert lease.is_short_term()

    def test_nearly_short_term(self):
        '''
        Lease is not short term when dates are slightly over 12 months apart.
        '''
        lease = LeaseFactory(start_date='31/12/2021', end_date='01/01/2023')
        assert not lease.is_short_term()

    def test_comfortably_not_short_term(self):
        '''
        Lease is not short term when dates are clearly over 12 months apart.
        '''
        lease = LeaseFactory(start_date='01/01/2022', end_date='01/01/2024')
        assert not lease.is_short_term()


class TestTenure:
    def test_leasehold(self):
        '''Valid leasehold tenure string is set as tenure attribute.'''
        lease = LeaseFactory(tenure='leasehold')
        assert lease.tenure == 'leasehold'

    def test_freehold(self):
        '''Valid freehold tenure string is set as tenure attribute.'''
        lease = LeaseFactory(tenure='freehold')
        assert lease.tenure == 'freehold'

    def test_invalid_tenure(self):
        '''Invalid tenure string raises `InvalidTenureError`.'''
        with pytest.raises(InvalidTenureError):
            LeaseFactory(tenure='invalid_tenure')


class TestLessor:
    def test_lessor(self):
        '''Organisation instance is set as lessor attribute.'''
        lessor = OrganisationFactory()
        lease = LeaseFactory(lessor=lessor)
        assert lease.lessor == lessor


class TestLessee:
    def test_lessee(self):
        '''Organisation instance is set as lessee attribute.'''
        lessee = OrganisationFactory()
        lease = LeaseFactory(lessee=lessee)
        assert lease.lessee == lessee
