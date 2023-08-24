# Deploy Springboot to Azure VM

### Create Springboot as HTTP
- http because upto server(vm), it is https.
- terminate the SSL at server level, redirect the request with incoming headers to port(8080, used by springboot)
- indirectly https request accepted by springboot


## Create the certificate and key files
### Create the self-signed certificate using keytool(included in java)
```bash
    # create the jks keystore file
    keytool -genkey -alias selfsigned -storetype PKCS12 -keyalg RSA -keysize 2048 -keystore mykeystore.jks -validity 365


    # Export the jks keystore file to crt
    keytool -exportcert -alias selfsigned -file certificate.crt -keystore mykeystore.jks

    # Convert the .crt file to .pem file
    openssl x509 -inform DER -in certificate.crt -out certificate.pem
```

### Extract the key from the jks file using openssl
```bash
    openssl pkcs12 -in mykeystore.jks -nocerts -nodes -out private.key
```

### Convert the ".key" file to ".pem" file
```bash
    openssl rsa -in private.key -out private.pem
```

### Install nginx on the system
```bash
    sudo apt update
    sudo apt install nginx
```

### Create a "ssl" directory in /etc/nginx/ssl, and move the two .pem files 
```bash
    sudo mv certificate.pem private.pem /etc/nginx/ssl/
```

### Update the contents in "/etc/nginx/sites-available/default" to new config
```bash
    # Open the file
    sudo vim /etc/nginx/sites-available/default

    # Update the file to be
    # SSL configuration
    listen 443 ssl;
    server_name _;  # Listen on any hostname (wildcard)

    ssl_certificate /etc/nginx/ssl/certificate.pem;
    ssl_certificate_key /etc/nginx/ssl/private.pem;

    location / {
            proxy_pass http://127.0.0.1:8080;  # Forward to Spring Boot
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

    }

    # Remove the existing location / route, otherwise error will show up.

    # restart the nginx server
    sudo service nginx restart
```














