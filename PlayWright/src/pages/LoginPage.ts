import { Page, Locator, expect } from '@playwright/test';

export enum LoginField {
  Username = 'username',
  Password = 'password',
}

export enum LoginElement {
  LoginButton = 'loginButton',
  ErrorMessage = 'errorMessage',
}

export class LoginPage {
  private locators: { [key: string]: Locator };

  constructor(private page: Page) {
    this.locators = {
      username: page.locator('#user-name'),
      password: page.locator('#password'),
      loginButton: page.locator('#login-button'),
      errorMessage: page.locator('.error-message-container.error'),
    };
  }

  get(name: keyof typeof this.locators): Locator {
    return this.locators[name];
  }

  async goto(url: string) {
    await this.page.goto(url);
    await expect(this.page).toHaveTitle('Swag Labs');
  }

  async fillCredentials(username: string, password: string) {
    await this.get(LoginField.Username).fill(username);
    await this.get(LoginField.Password).fill(password);
  }

  async submit() {
    await this.get(LoginElement.LoginButton).click();
  }

  async login(username: string, password: string) {
    await this.fillCredentials(username, password);
    await this.submit();
  }

  async expectLoginSuccess(baseUrl: string) {
    const expectedUrl = new URL('inventory.html', baseUrl).toString();
    await expect(this.page).toHaveURL(expectedUrl);
  }

  async expectLoginFailure(baseUrl: string) {
    await expect(this.page).toHaveURL(baseUrl);
  }

  async expectErrorMessage(message: string) {
    const errorLocator = this.get(LoginElement.ErrorMessage);
    await expect(errorLocator).toBeVisible();
    await expect(errorLocator).toHaveText(message);
  }
}
