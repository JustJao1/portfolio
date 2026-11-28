import {test,expect} from '@playwright/test';
test.beforeEach(async({page})=>{
  await page.route('**/*',route=>new URL(route.request().url()).origin==='http://127.0.0.1:4174'?route.continue():route.abort());
  await page.goto('/');
  await expect(page.locator('html')).toHaveAttribute('data-lang','pt');
});
test('engineering evidence is bilingual and linked',async({page})=>{
  const section=page.locator('#engineering');
  await expect(section.locator('.eng-card')).toHaveCount(10);
  await expect(section.locator('.eng-card a[href$="/docs/engineering-quality.md"]')).toHaveCount(10);
  await expect(section.locator('h2')).toHaveText(/Qualidade de software/);
  await expect(section.locator('h2 span[lang="pt-BR"]')).toBeVisible();
  await page.locator('[data-language=en]').click();
  await expect(page.locator('html')).toHaveAttribute('lang','en');
  await expect(section.locator('h2 span[lang=en]')).toBeVisible();
  await expect(section.locator('h2 span[lang="pt-BR"]')).toBeHidden();
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-lang','en');
});
test('responsive layout, theme and project filters remain usable',async({page})=>{
  await expect(page.locator('html')).toHaveAttribute('data-theme','dark');
  await page.locator('#themeControl').click();
  await expect(page.locator('html')).toHaveAttribute('data-theme','light');
  await page.locator('[data-filter=automation]').click();
  await expect(page.locator('[data-filter=automation]')).toHaveAttribute('aria-pressed','true');
  await expect(page.locator('[data-pinned=true]').first()).toBeVisible();
  await page.locator('[data-filter=all]').click();
  await expect(page.locator('[data-filter=all]')).toHaveAttribute('aria-pressed','true');
  await page.locator('#engineering').scrollIntoViewIfNeeded();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+5)).toBeTruthy();
  await expect(page.locator('#engineering .eng-card').last()).toBeVisible();
  await page.screenshot({path:test.info().outputPath('engineering-section.png'),fullPage:true});
});
