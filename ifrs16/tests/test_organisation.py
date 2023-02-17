from ifrs16.tests.factories import OrganisationFactory


class TestName:
    def test_name(self):
        organisation = OrganisationFactory(name='Acme Ltd')
        assert organisation.name == 'Acme Ltd'
