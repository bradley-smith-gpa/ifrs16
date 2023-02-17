from ifrs16.core.organisation import Organisation


class TestName:
    def test_name(self):
        organisation = Organisation(name='Acme Ltd')
        assert organisation.name == 'Acme Ltd'
