from pytest_bdd import scenario, given, when, then


# Scenario is a decorator here
@scenario('../features/api_test.feature', 'Validation')
def test_add():
    pass


@given("API request")
def api_request():
    assert 1 == 1
