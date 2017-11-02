from freshen import *

from lab1.calc import Calculator

@Before
def before(sc):
    scc.calc = Calculator()
    scc.result = None

@Given("I have entered (\d+) into the calculator")
def enter(num):
    scc.calc.push(int(num))

@When("I press (\w+)")
def press(button):
    op = getattr(scc.calc, button)
    scc.result = op()

@Then("the result should be (.*) on the screen")
def check_result(value):
    assert_equal(str(scc.result), value)
