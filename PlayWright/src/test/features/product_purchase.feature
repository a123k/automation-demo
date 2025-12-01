Feature: Product Purchase

@TC-9
Scenario: TC-9 Verify that no of items in cart is updated when adding or removing product from product page.
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I added three products to the cart
    And I verify that items in cart is "3"
    And I removed two products from the cart
    And I verify that items in cart is "1"

@TC-10
Scenario: TC-10 Verify that no of items in cart is updated when adding or removing product from cart page.
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I added three products to the cart
    And I verify that items in cart is "3"
    And I click on the cart icon
    And I removed two products from the cart
    And I verify that items in cart is "1"

@TC-12
Scenario: TC-12 Verify that no of items in cart is correct through the checkout process.
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I added three products to the cart
    And I verify that items in cart is "3"
    And I click on the cart icon
    And I verify that items in cart is "3"
    And I proceed to checkout 
    And I verify that items in cart is "3"
    And I entered checkout details
    And I continued checkout
    And I verify that items in cart is "3"
    And I completed checkout
    And I verify that cart is empty

@TC-13
Scenario: TC-13 Verify that correct products are added to the cart
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I added three products to the cart
    And I verify that items in cart is "3"
    And I click on the cart icon
    And I verify that correct products added to the cart

@TC-14
Scenario: TC-14 Verify the cancellation of checkout from Your information page and overview page
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I added three products to the cart
    And I click on the cart icon
    And I proceed to checkout 
    And I entered checkout details
    And I cancel the checkout
    And I verify that page is redirected to your cart page
    And I proceed to checkout 
    And I entered checkout details
    And I continued checkout
    And I cancel the checkout
    And I verify that page is redirected to product page

@TC-15
Scenario: TC-15 Verify that the price calculated at the checkout is the sum of the product prices added to the cart
    Given I launch the portal
    Then I logged into the portal successfully with username "standard_user" and password "secret_sauce"
    And I added three products to the cart
    And I click on the cart icon
    And I proceed to checkout 
    And I entered checkout details
    And I continued checkout
    And I verify that the item total is the sum of the products prices added to the cart

    



    