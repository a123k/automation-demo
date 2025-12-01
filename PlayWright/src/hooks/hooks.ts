import * as dotenv from 'dotenv';
import { BeforeAll, AfterAll, Before, After, Status } from '@cucumber/cucumber';
import { Browser, chromium, firefox, webkit } from '@playwright/test';
import { CustomWorld } from './world';

let browser: Browser;

function getBrowserEngine(name: string) {
  switch (name.toLowerCase()) {
    case 'firefox':
      return firefox;
    case 'webkit':
      return webkit;
    default:
      return chromium;
  }
}

BeforeAll(async function () {
 
  const env = process.env.ENV || 'staging';
  dotenv.config({
    path: `env/.env.${env}`,
    override: true
  });

  const browserName = process.env.BROWSER || 'chromium';
  const headless = process.env.HEADLESS !== 'false'; // default true

  const engine = getBrowserEngine(browserName);
  browser = await engine.launch({ headless });
});

Before(async function (this: CustomWorld, scenario) {
  
  this.context = await browser.newContext({ recordVideo: { dir: 'videos/' } });
  this.page = await this.context.newPage();

  this.testURL = process.env.TEST_URL || '';
  if (!this.testURL.trim()) {
    throw new Error('TEST_URL is required but not set.');
  }

  console.log('Navigating to URL:', this.testURL);
  await this.page.goto(this.testURL);
});

After(async function (this: CustomWorld, scenario) {
  if (scenario.result?.status === Status.FAILED) {

    const screenshot = await this.page.screenshot();
    await this.attach(screenshot, 'image/png');

    const videoPath = await this.page.video()?.path();
    if (videoPath) {
      const fs = require('fs');
      const video = fs.readFileSync(videoPath);
      await this.attach(video, 'video/webm');
    }

    await this.attach(JSON.stringify(scenario.result), 'application/json');
  }

  await this.context.close();
});

AfterAll(async function () {
  await browser.close();
});
