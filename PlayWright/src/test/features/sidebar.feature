Feature: Sidebar


@TC-4
Scenario: TC-4 Verify the sidebar option avaialable under the burger menu.
Given I launch the portal
And I logged into the portal successfully with username "standard_user" and password "secret_sauce"
And I click on the burger menu on the top left corner
And I verify the functionality of All Items, About, Logout and Reset App state


@TC-5
Scenario: TC-5 Verify that side bar is closed when clicking on the cross icon to close the burger menu.
Given I launch the portal
And I logged into the portal successfully with username "standard_user" and password "secret_sauce"
And I click on the burger menu on the top left corner
And I click on the cross icon to close the burger menu
And I verify that All Items, About, Logout and Reset App state is not listed

@TC-11
Scenario: TC-11 Verify that side bar is avaibale from all pages.
Given I launch the portal
And I logged into the portal successfully with username "standard_user" and password "secret_sauce"
And I click on the burger menu on the top left corner
And I verify that All Items, About, Logout and Reset App state is listed
And I click on the cart icon
And I click on the burger menu on the top left corner
And I verify that All Items, About, Logout and Reset App state is listed
And I proceed to checkout 
And I click on the burger menu on the top left corner
And I verify that All Items, About, Logout and Reset App state is listed
And I entered checkout details
And I continued checkout
And I click on the burger menu on the top left corner
And I verify that All Items, About, Logout and Reset App state is listed
And I completed checkout
And I click on the burger menu on the top left corner
And I verify that All Items, About, Logout and Reset App state is listed

