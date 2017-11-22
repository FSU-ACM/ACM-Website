FROM nginx

# Set up shop
WORKDIR /usr/share/nginx

# Install basics
RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get install -y curl \
    && apt-get install -y gnupg2

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && apt-get install -y build-essential

# Set up npm libs
RUN npm install -g gulp \
    && npm install node-sass

# Because node-sass sucks
RUN npm rebuild node-sass --force

# Add the rest of our site files
COPY . /usr/share/nginx
RUN npm install

# Build the site
RUN gulp build
RUN rm -rf html && ln -s /usr/share/nginx/build /usr/share/nginx/html