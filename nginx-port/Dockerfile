FROM node:lts as BUILDER
COPY ng-app /ng-app
WORKDIR /ng-app
RUN npm install -g @angular/cli@8.0.3
RUN npm install 
RUN ng build

FROM nginx:alpine
LABEL One-Off Coder "info@oneoffcoder.com"
COPY nginx-default.conf.template /etc/nginx/conf.d/default.conf.template
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
COPY --from=BUILDER /ng-app/dist/ng-app/ /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]