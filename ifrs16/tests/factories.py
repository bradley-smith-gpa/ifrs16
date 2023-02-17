from factory import Factory, LazyFunction
from ifrs16.tests import fake
from ifrs16.core.organisation import Organisation


class OrganisationFactory(Factory):
    class Meta:
        model = Organisation

    name = LazyFunction(fake.company)
