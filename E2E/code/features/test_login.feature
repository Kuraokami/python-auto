Feature: SauceDemo

  Scenario: I can login with valid user
    Given I enter login page
    When I try to login with standardUser
    Then I can see the products page