import {defineConfig,devices} from '@playwright/test';
export default defineConfig({
  testDir:'./specs',workers:1,retries:0,
  reporter:[['list'],['html',{outputFolder:'../../quality-results/portfolio-html',open:'never'}],['junit',{outputFile:'../../quality-results/portfolio.xml'}]],
  outputDir:'../../quality-results/portfolio-artifacts',
  use:{baseURL:'http://127.0.0.1:4174',reducedMotion:'reduce',screenshot:'only-on-failure',trace:'retain-on-failure'},
  webServer:{command:'python -m http.server 4174 --bind 127.0.0.1 --directory ../..',url:'http://127.0.0.1:4174',reuseExistingServer:false},
  projects:[{name:'desktop',use:{...devices['Desktop Chrome']}},{name:'mobile',use:{...devices['Pixel 7']}}]
});
