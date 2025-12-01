import { Page, Locator, expect } from '@playwright/test';
import { CustomWorld } from '../hooks/world';

export class ProductListPage {
  private locators: { [key: string]: Locator };
  

  constructor(private page: Page, private world: CustomWorld) {
    this.locators = {
      filterIcon: page.locator('.product_sort_container'),
      productNames: page.locator('.inventory_item_name'),
      productPrices: page.locator('.inventory_item_price'),
      product:page.locator('.inventory_item'),
      addCartOnesie: page.locator('#add-to-cart-sauce-labs-onesie'),
      addCartBikeLight: page.locator('#add-to-cart-sauce-labs-bike-light'),
      addCartBoltTShirt: page.locator('#add-to-cart-sauce-labs-bolt-t-shirt'),
      removeBikeLight: page.locator('#remove-sauce-labs-bike-light'),
      removeBoltTShirt: page.locator('#remove-sauce-labs-bolt-t-shirt'),
    };
  }

  get(name: keyof typeof this.locators): Locator {
    return this.locators[name];
  }

  async selectFilterOption(option: string) {
    await this.get('filterIcon').selectOption({ label: option });
  }
 
  async expectProductNamesSorted(order: 'ascending' | 'descending') {
    const names = await this.get('productNames').allTextContents();
    const sorted = [...names].sort((a, b) =>
      order === 'ascending' ? a.localeCompare(b) : b.localeCompare(a)
    );
    expect(names).toEqual(sorted);
  }

  async expectProductPricesSorted(order: 'ascending' | 'descending') {
    const prices = (await this.get('productPrices').allTextContents())
      .map(text => parseFloat(text.replace('$', '')));
    const sorted = [...prices].sort((a, b) =>
      order === 'ascending' ? a - b : b - a
    );
    expect(prices).toEqual(sorted);
  }

  async getProductDetailsByName(productName: string){
      const product = this.page.locator('.inventory_item').filter({ has: this.page.locator('.inventory_item_name', { hasText: productName }) });
      const name = (await product.locator('.inventory_item_name').textContent())?.trim() ?? '';
      const priceText = (await product.locator('.inventory_item_price').textContent())?.trim() ?? '';
      const price = parseFloat(priceText.replace('$', ''));
      return { name, price };

  }

  async addThreeProducts() {
    await this.get('addCartOnesie').click();
    const onesieDetails = await this.getProductDetailsByName('Sauce Labs Onesie');
    this.world.addedProductsName.push(onesieDetails.name);
    this.world.addedProductTotalPrices += onesieDetails.price;

    await this.get('addCartBikeLight').click();
    const bikeLightDetails = await this.getProductDetailsByName('Sauce Labs Bike Light');
    this.world.addedProductsName.push(bikeLightDetails.name);
    this.world.addedProductTotalPrices += bikeLightDetails.price;

    await this.get('addCartBoltTShirt').click();
    const boltTShirtDetails = await this.getProductDetailsByName('Sauce Labs Bolt T-Shirt');
    this.world.addedProductsName.push(boltTShirtDetails.name);
    this.world.addedProductTotalPrices += boltTShirtDetails.price
    
}

  async removeTwoProducts() {
    await this.get('removeBikeLight').click();
    await this.get('removeBoltTShirt').click();
  }

  async checkProductPageURL(baseUrl: string) {
    const expectedUrl = new URL('inventory.html', baseUrl).toString();
    await expect(this.page).toHaveURL(expectedUrl);
  }
  async expectedPriceTotal() {
    return this.world.addedProductTotalPrices
  }

  async getAddedProductNames() {
    return this.world.addedProductsName;
  }

   async getProductNames(){
      const names = await this.get('productNames').allTextContents();
      return names;
  }

}
