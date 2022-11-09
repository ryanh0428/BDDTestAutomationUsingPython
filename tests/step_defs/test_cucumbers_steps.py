from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then

from cucumber_basket import CucumberBasket



# @scenario('../features/cucumbers.feature', 'Add cucumbers to a basket') # (feature file path, name of the scenatio)
# def test_add(): # whatever put into the scenario function will be executed after all the scenario steps
#     pass
#
#
# @scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket')
# def test_remove():
#     pass

EXTRA_TYPES={
    'Number':int
}

CONVERTERS = {
    'initial':int,
    'some': int,
    'total': int
}

scenarios('../features/cucumbers.feature')

#partial function will cause the Gerkin statment fail to recognise the respective method
parse_num = partial(parsers.cfparse, extra_types= EXTRA_TYPES)


@given(parse_num('the basket has "{initial:Number}" cucumbers'), target_fixture='basket')
@given('the basket has "<initial>" cucumbers', converters=CONVERTERS) #<---different from the video, converter should included in the fixture instead of scenarios method
def fixture_target_basket(initial): # become the fixture value that the result will be injected when the step call this fixture
    return CucumberBasket(initial_count=initial)


@when(parse_num('"{some:Number}" cucumbers are added to the basket'))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)


@when(parse_num('"{some:Number}" cucumbers are removed from the basket'))
@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parse_num('the basket contains "{total:Number}" cucumbers'))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total
