from factory import Factory, LazyFunction, LazyAttribute, SubFactory
from factory.fuzzy import FuzzyChoice
from ifrs16.tests import fake
from ifrs16.core.organisation import Organisation
from ifrs16.core.lease import Lease


class OrganisationFactory(Factory):
    class Meta:
        model = Organisation

    name = LazyFunction(fake.company)


class LeaseFactory(Factory):
    class Meta:
        model = Lease

    start_date = LazyFunction(fake.date_time)
    end_date = LazyAttribute(
        lambda obj: fake.date_time_between(start_date=obj.start_date)
    )
    tenure = FuzzyChoice(choices=('leasehold', 'freehold'))
    organisation = SubFactory(OrganisationFactory)
