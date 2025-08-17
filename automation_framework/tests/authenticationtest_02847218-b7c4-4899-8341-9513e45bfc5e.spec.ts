
import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('AuthenticationTest_2025-08-16', async ({ page, context }) => {
  
    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('[data-test="username"]', 'standard_user');

    // Fill input field
    await page.fill('[data-test="password"]', 'secret_sauce');

    // Click element
    await page.click('[data-test="login-button"]');

    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('[data-test="username"]', 'standard_use');

    // Fill input field
    await page.fill('[data-test="password"]', 'secret_sauce');

    // Click element
    await page.click('[data-test="login-button"]');
});