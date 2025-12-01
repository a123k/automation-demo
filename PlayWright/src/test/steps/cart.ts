import { Given, Then } from '@cucumber/cucumber';
import { CustomWorld } from '../../hooks/world';
import { CartPage } from '../../pages/CartPage';


Then('I verify that items in cart is {string}', async function (this: CustomWorld, count: string) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.expectCartCount(count);
});

Then('I click on the cart icon', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.openCart();
});

Then('I proceed to checkout', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.goToCheckout();
});

Then('I continued checkout', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.continueCheckout();
});

Then('I entered checkout details', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.getfirstName().fill('Sara')
  await cartPage.getlastName().fill('Logan')
  await cartPage.getzipCode().fill('XX11 8DT')
});

Then('I completed checkout', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.finishCheckout();
});

Then('I verify that cart is empty', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.expectCartEmpty();
});

Then('I verify that correct products added to the cart', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.verifyCartItems();
  
});

Then('I cancel the checkout', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.cancelCheckout();
  
});

Then('I verify that page is redirected to your cart page', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.verifyCartURL(this.testURL);
  
});

Then('I verify that the item total is the sum of the products prices added to the cart', async function (this: CustomWorld) {
  const cartPage = new CartPage(this.page, this);
  await cartPage.verifyItemTotal()
});
