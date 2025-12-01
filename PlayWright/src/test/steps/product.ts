
import { Given, Then } from '@cucumber/cucumber';
import { CustomWorld } from '../../hooks/world';
import { ProductListPage } from '../../pages/ProductListPage';


Then('I click on the filter icon and select the option {string}', async function (this: CustomWorld, option: string) {
  const productListPage = new ProductListPage(this.page, this);
  await productListPage.selectFilterOption(option);
});

Then('I verify that the productnames are sorted alphabetically in {string} order', async function (this: CustomWorld, order: string) {
  const productListPage = new ProductListPage(this.page, this);
  await productListPage.expectProductNamesSorted(order as 'ascending' | 'descending');
});

Then('I verify that the product prices are sorted in {string} order', async function (this: CustomWorld, order: string) {
  const productListPage = new ProductListPage(this.page, this);
  await productListPage.expectProductPricesSorted(order as 'ascending' | 'descending');
});

Then('I added three products to the cart', async function (this: CustomWorld) {
  const productListPage = new ProductListPage(this.page, this);
  await productListPage.addThreeProducts();
});

Then('I removed two products from the cart', async function (this: CustomWorld) {
  const productListPage = new ProductListPage(this.page, this);
  await productListPage.removeTwoProducts();
});

Then('I verify that page is redirected to product page', async function (this: CustomWorld) {
  const productListPage = new ProductListPage(this.page, this);
  await productListPage.checkProductPageURL(this.testURL);
});