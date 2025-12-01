Feature: Filter

@TC-7
Scenario: TC-7 Verify the filtering of product in alphabetical order.
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I click on the filter icon and select the option "Name (A to Z)"
    And I verify that the productnames are sorted alphabetically in "ascending" order
    And I click on the filter icon and select the option "Name (Z to A)"
    And I verify that the productnames are sorted alphabetically in "descending" order


@TC-8
Scenario: TC-8 Verify the filtering of product in price order.
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I click on the filter icon and select the option "Price (low to high)"
    And I verify that the product prices are sorted in "ascending" order
    And I click on the filter icon and select the option "Price (high to low)"
    And I verify that the product prices are sorted in "descending" order
