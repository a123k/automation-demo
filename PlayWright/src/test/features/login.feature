Feature: User login

@TC-1
Scenario Outline: TC-1 Verify the login with valid credentials.
Given I launch the portal
Then I provided username "<username>" and password "secret_sauce"
Then I click on login button
And I verify login is successful
Examples: Valid usernames
|username               |
|standard_user          |
|problem_user           |
|error_user             |
|visual_user            |


@TC-2
Scenario: TC-2 Verify that locked user is restricted from login.
Given I launch the portal
Then I provided username "locked_out_user" and password "secret_sauce"
Then I click on login button
And I verify login is not successful
And I verify that error message "Epic sadface: Sorry, this user has been locked out." is displayed to show the login failure


@TC-3
Scenario: TC-3 Verify that invalid user is restricted from login.
Given I launch the portal
Then I provided username "test" and password "secret_sauce"
Then I click on login button
And I verify login is not successful
And I verify that error message "Epic sadface: Username and password do not match any user in this service" is displayed to show the login failure