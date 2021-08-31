from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then


# Scenario is a decorator here
# @scenario('../features/cucumber_api_test.feature', 'to verify the api')
# def test_api():
#     pass

scenarios('../features/cucumber_api_test.feature')


EXTRA_TYPES = {
    'Number': int,
}

# parse_num = partial(parsers.cfparse,extra_types=EXTRA_TYPES)
# @when(parse_num('request is equal to "{initial:Number}"'))

@given("API request")
def api_request():
    assert 1 == 1


@when(parsers.cfparse('request is equal to "{initial:Number}"', extra_types=EXTRA_TYPES))
def request_equal(initial):
    assert initial == initial
