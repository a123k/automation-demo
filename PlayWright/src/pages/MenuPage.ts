import { Page, Locator, expect } from '@playwright/test';

export class MenuPage {
  private locators: { [key: string]: Locator };

  constructor(private page: Page) {
    this.locators = {
      burgerMenu: page.locator('#react-burger-menu-btn'),
      burgerMenuClose: page.locator('#react-burger-cross-btn'),
      allItems: page.locator('#inventory_sidebar_link'),
      about: page.locator('#about_sidebar_link'),
      logout: page.locator('#logout_sidebar_link'),
      resetAppState: page.locator('#reset_sidebar_link'),
    };
  }

  get(name: keyof typeof this.locators): Locator {
    return this.locators[name];
  }

  async openMenu() {
    await this.get('burgerMenu').click();
  }

  async closeMenu() {
    await this.get('burgerMenuClose').click();
  }

  async clickresetAppState() {
    await this.get('resetAppState').click();
  }

  async clickabout() {
    await this.get('about').click();
  }
  
   async clickallItems() {
    await this.get('allItems').click();
  }

  async clicklogout() {
    await this.get('logout').click();
  }

  async expectMenuItemsVisible() {
    await expect(this.get('allItems')).toBeVisible();
    await expect(this.get('about')).toBeVisible();
    await expect(this.get('logout')).toBeVisible();
    await expect(this.get('resetAppState')).toBeVisible();
  }

  async expectMenuItemsHidden() {
    await expect(this.get('allItems')).toBeHidden();
    await expect(this.get('about')).toBeHidden();
    await expect(this.get('logout')).toBeHidden();
    await expect(this.get('resetAppState')).toBeHidden();
  }
}
