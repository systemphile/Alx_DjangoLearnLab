## 🔒 HTTPS and Security Configuration for LibraryProject

This document outlines the security measures implemented in the `LibraryProject` Django application to ensure safe and secure communication between clients and the server.

---

## 1. HTTPS Enforcement

### Django Settings

- **SECURE_SSL_REDIRECT = True**  
  Forces all HTTP traffic to be redirected to HTTPS.

- **SECURE_HSTS_SECONDS = 31536000**  
  Enables HTTP Strict Transport Security (HSTS) for one year.

- **SECURE_HSTS_INCLUDE_SUBDOMAINS = True**  
  Applies HSTS policy to all subdomains.

- **SECURE_HSTS_PRELOAD = True**  
  Allows the domain to be included in browser preload lists.

---

## 2. Secure Cookies

- **SESSION_COOKIE_SECURE = True**  
  Ensures session cookies are only sent over HTTPS.

- **CSRF_COOKIE_SECURE = True**  
  Ensures CSRF cookies are only sent over HTTPS.

---

## 3. Security Headers

- **X_FRAME_OPTIONS = "DENY"**  
  Prevents clickjacking by blocking rendering in iframes.

- **SECURE_CONTENT_TYPE_NOSNIFF = True**  
  Stops browsers from guessing content types.

- **SECURE_BROWSER_XSS_FILTER = True**  
  Enables basic XSS filtering in browsers that support it.

---

## 4. Deployment Configuration

### Nginx SSL Setup

```nginx
server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name localhost;

    ssl_certificate /etc/letsencrypt/live/localhost/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/localhost/privkey.pem;

    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}
