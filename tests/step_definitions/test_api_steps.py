from pytest_bdd import scenario, given, when, then


# Scenario is a decorator here
@scenario('../features/cucumber_api_test.feature', 'to verify the api')
def test_api():
    pass


@given("API request")
def api_request():
    assert 1 == 1
