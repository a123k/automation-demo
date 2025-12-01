import { Given, Then } from '@cucumber/cucumber';
import { CustomWorld } from '../../hooks/world';
import { LoginPage } from '../../pages/LoginPage';

Given('I launch the portal', async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.goto(this.testURL);
});

Then('I provided username {string} and password {string}', async function (this: CustomWorld, username: string, password: string) {
  const loginPage = new LoginPage(this.page);
  await loginPage.fillCredentials(username, password);
});

Then('I click on login button', async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.submit();
});

Then('I verify login is successful', async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.expectLoginSuccess(this.testURL);
});

Then('I verify login is not successful', async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.expectLoginFailure(this.testURL);
});

Then('I verify that error message {string} is displayed to show the login failure', async function (this: CustomWorld, errorMessage: string) {
  const loginPage = new LoginPage(this.page);
  await loginPage.expectErrorMessage(errorMessage);
});

Given('I logged into the portal successfully with username {string} and password {string}', async function (this: CustomWorld, username: string, password: string) {
  const loginPage = new LoginPage(this.page);
  await loginPage.login(username, password);
  await loginPage.expectLoginSuccess(this.testURL);
});
