FROM mcr.microsoft.com/playwright:v1.57.0-jammy
RUN apt-get update && \
    apt-get install -y openjdk-17-jre wget unzip && \
    wget https://github.com/allure-framework/allure2/releases/download/2.34.1/allure-2.34.1.zip && \
    unzip allure-2.34.1.zip -d /opt && \
    ln -s /opt/allure-2.34.1/bin/allure /usr/local/bin/allure
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci # clean install
COPY . .
RUN rm -rf /app/allure-results && mkdir -p /app/allure-results
RUN npx playwright install --with-deps chromium
ENV HEADLESS=true
ENV CI=true
CMD ["npm", "test"]
