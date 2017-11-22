FROM nginx

# Set up shop
WORKDIR /usr/share/nginx

# Install basics
RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get install -y curl \
    && apt-get install -y gnupg2 \
    && apt-get install apt-transport-https ca-certificates

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get -y install yarn

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && apt-get install -y build-essential

# Use Yarn to install globals
RUN yarn global add npm@5 gulp

# Set up node modules
COPY ./package.json ./package-lock.json ./yarn.lock ./
RUN yarn

# Add the rest of our site files
COPY . .

# Build the site
RUN gulp build
RUN rm -rf html && ln -s /usr/share/nginx/build /usr/share/nginx/html
