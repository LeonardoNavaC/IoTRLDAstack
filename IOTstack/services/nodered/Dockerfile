FROM nodered/node-red:latest-12
USER root
RUN apk update && apk add --no-cache eudev-dev
USER node-red

RUN cd /usr/src/node-red && npm install --save  node-red-configurable-ping
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-boolean-logic
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-influxdb
RUN cd /usr/src/node-red && npm install --save  node-red-dashboard
RUN cd /usr/src/node-red && npm install --save  node-red-node-pi-gpiod
RUN cd /usr/src/node-red && npm install --save  node-red-node-rbe

