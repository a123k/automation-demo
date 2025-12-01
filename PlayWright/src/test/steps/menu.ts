import { Given, Then } from '@cucumber/cucumber';
import { CustomWorld } from '../../hooks/world';
import { MenuPage } from '../../pages/MenuPage';


Then('I click on the burger menu on the top left corner', async function (this: CustomWorld) {
  const menuPage = new MenuPage(this.page);
  await menuPage.openMenu();
});

Then('I verify the functionality of All Items, About, Logout and Reset App state', async function (this: CustomWorld) {
  const menuPage = new MenuPage(this.page);
  await menuPage.expectMenuItemsVisible();

  // Example navigation checks
  const currentUrl = this.page.url();
  await menuPage.clickallItems();
  await this.page.waitForURL(currentUrl);

  await menuPage.clickabout();
  await this.page.waitForURL('https://saucelabs.com/');
  await this.page.goBack();

  await menuPage.openMenu();
  await menuPage.clickresetAppState();
  await this.page.waitForURL(currentUrl);

  await menuPage.clicklogout();
  await this.page.waitForURL(this.testURL);
});

Then('I click on the cross icon to close the burger menu', async function (this: CustomWorld) {
  const menuPage = new MenuPage(this.page);
  await menuPage.closeMenu();
});

Then('I verify that All Items, About, Logout and Reset App state is not listed', async function (this: CustomWorld) {
  const menuPage = new MenuPage(this.page);
  await menuPage.expectMenuItemsHidden();
});

Then('I verify that All Items, About, Logout and Reset App state is listed', async function (this: CustomWorld) {
  const menuPage = new MenuPage(this.page);
  await menuPage.expectMenuItemsVisible();
});