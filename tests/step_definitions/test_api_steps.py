from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then

# Scenario is a decorator here
# @scenario('../features/cucumber_api_test.feature', 'to verify the api')
# def test_api():
#     pass

x = 0
y = 0

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'sum_total': int
}
# scenarios('../features/cucumber_api_test.feature')
#
scenarios('../features/cucumber_api_test.feature', example_converters=CONVERTERS)


# parse_num = partial(parsers.cfparse,extra_types=EXTRA_TYPES)
# @when(parse_num('request is equal to "{initial:Number}"'))

@given("API request")
def api_request():
    assert 1 == 1


@when(parsers.cfparse('request is equal to "{initial:Number}"', extra_types=EXTRA_TYPES))
def request_equal(initial):
    assert initial == initial


@given('number one "<initial>"')
def initial_value(initial):
    y = initial
    print(y)
    # assert initial == initial


@when('request add "<some>"')
def step_impl(some):
    print(y)
    x = y + some
    print(x)
    # assert some == some


@then('total add "<sum_total>"')
def step_impl(sum_total):
    assert x == sum_total
    # assert sum_total == sum_total
