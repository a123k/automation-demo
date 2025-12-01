import { Page, Locator, expect } from '@playwright/test';
import { CustomWorld } from '../hooks/world';

export class CartPage {
  private locators: { [key: string]: Locator };

  constructor(private page: Page, private world: CustomWorld) {
    this.locators = {
      shoppingCart: page.locator('.shopping_cart_link'),
      checkoutButton: page.locator('#checkout'),
      continueShoppingButton: page.locator('#continue-shopping'),
      cartItems: page.locator('.cart_item'),
      continueButton:page.locator('#continue'),
      firstName:page.locator('#first-name'),
      lastName:page.locator('#last-name'),
      zipCode:page.locator('#postal-code'),
      finishCheckout:page.locator('#finish'),
      cancelButton:page.locator('#cancel'),
      itemPrice:page.locator('.inventory_item_price')
    };
  }

  get(name: keyof typeof this.locators): Locator {
    return this.locators[name];
  }

  async openCart() {
    await this.get('shoppingCart').click();
  }

  async expectCartCount(count: string) {
    const actual = await this.get('shoppingCart').innerText();
    expect(actual).toBe(count);
  }

  async expectCartEmpty() {
    const actual = await this.get('shoppingCart').innerText();
    expect(actual).toBe("");
  }

  async goToCheckout() {
    await this.get('checkoutButton').click();
  }

  async continueShopping() {
    await this.get('continueShoppingButton').click();
  }

  async continueCheckout() {
    await this.get('continueButton').click();
  }
  
  async finishCheckout() {
    await this.get('finishCheckout').click();
  }

  async cancelCheckout() {
    await this.get('cancelButton').click();
  }


  getfirstName(){
     return this.get('firstName');
  }

   getlastName(){
     return this.get('lastName');
  }
  getzipCode(){
     return this.get('zipCode');
  }

  async getCartItemNames(): Promise<string[]> {
    const items = await this.get('cartItems').locator('.inventory_item_name').allTextContents();
    return items;
}
 async verifyCartItems() {
  const actualNames = await this.getCartItemNames();
  console.log(actualNames);
  const expectedProducts = this.world.addedProductsName;
  console.log(expectedProducts);
  expect(actualNames).toEqual(expectedProducts);
}
async verifyCartURL(baseUrl: string){
  const expectedUrl = new URL('cart.html', baseUrl).toString();
  await expect(this.page).toHaveURL(expectedUrl);
}
async verifyItemTotal(){
  const prices = await this.get('itemPrice').allTextContents();
  console.log('Item Prices', prices)
  const totalPrice = prices.map(price=>parseFloat(price.replace('$',''))).reduce((sum,value)=>sum+value,0);
  expect(totalPrice).toBe(this.world.addedProductTotalPrices);

}

}

