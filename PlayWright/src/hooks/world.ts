import { setWorldConstructor, World } from '@cucumber/cucumber';
import { Browser, BrowserContext, Page } from '@playwright/test';


export class CustomWorld extends World {
  browser!: Browser;
  context!: BrowserContext;
  page!: Page;
  testURL!: string;
  addedProductsName: String[]=[] ;
  addedProductTotalPrices: number = 0;
}

setWorldConstructor(CustomWorld);
