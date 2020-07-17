FROM buildkite/puppeteer
RUN npm i whatsapp-web.js
RUN npm i qrcode-terminal
RUN npm i crummydb
ADD whatsapp-web.js
CMD node whatsapp-web.js