from pytest_bdd import scenarios, parsers, given, when, then

from cucumber_basket import CucumberBasket

scenarios('../features/cucumbers.feature')

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


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', EXTRA_TYPES), target_fixture='basket')
def fixture_target_basket(initial): # become the fixture value that the result will be injected when the step call this fixture
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total
