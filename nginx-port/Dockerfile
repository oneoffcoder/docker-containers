FROM node:lts as BUILDER
COPY ng-app /ng-app
WORKDIR /ng-app
RUN npm install -g @angular/cli@8.0.3
RUN npm install 
RUN ng build

FROM nginx:alpine
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

COPY nginx-default.conf.template /etc/nginx/conf.d/default.conf.template
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
COPY --from=BUILDER /ng-app/dist/ng-app/ /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]