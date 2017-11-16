Feature: BDD testing

  Scenario: Division
    Given I have entered 3 into the calculator
    And I have entered 2 into the calculator
    When I press divide
    Then the result should be 1.5 on the screen

  Scenario: Add
    Given I have entered 5 into the calculator
    And I have entered 3 into the calculator
    When I press add
    Then the result should be 8 on the screen
