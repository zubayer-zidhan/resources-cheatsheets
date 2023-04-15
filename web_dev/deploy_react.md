# Copy SSH credentials


```bash
    ssh root@"ip_address"   # ip = The ip address of your website
    ssh root@"domain_name"  # domain_name = The domain name of your website
```


# Open Command Promt/Terminal on host


```bash
    ssh root@"ip_address"\
    # Are you sure you want to continue? yes
    # Enter your password
    
```



# To disable root user, and create a user account with super user priveleges

```bash
    apt update      # update packages
    apt upgrade     # upgrade packages
    dpkg-reconfigure tzdata - set timezone   # to update timezone data

    add user uname  # create user with username = uname

    add user uname sudo   # adds "uname" to the super user group, granting it super user priveleges


    exit            # end the ssh session


    # login as uname
    ssh uname@ip

    sudo passwd -d root     # remove password from root user
    sudo passwd -l root     # lock the password for root user

    # Now cannot sign in as "root" user
```


# Installing "nginx", and setting it up


```bash
    sudo apt install nginx

    # Make folder where src code will reside
    # Replace {ip} with IP address of server, or, domain name of the server
    sudo mkdir /var/www/{ip}

    # Change permissions of the directory
    sudo chmod 755 -R /var/www/{ip}/

    # Change the ownership of the directory to be owned my user "uname"
    sudo chown -R uname:www-data /var/www/{ip}/



    # Create config file for nginx, and link it
    sudo nano /etc/nginx/sites-available/{ip}


    # The above file opens in nano, insert the following code:
    server {
        listen 80;
        listen [::]:80;

        root /var/www/{ip}
        index index.html;
    }
    # save the file


    # Unlink the default nginx config
    sudo unlink /etc/nginx/sites-enabled/default
    

    # Link to the config file we created
    sudo ln -s /etc/nginx/sites-available/{ip} /etc/nginx/sites-enabled/


    # Test to see if it works
    sudo nginx -t

    # Restart nginx
    sudo systemctl restart nginx

    # Test again to see if it works
    sudo nginx -t

```


# Deploy code from local machine to server


- <strong>Everything below is for the host machine</strong>
- In case of windows, use git-bash to run the following commands.
- In case of linux/mac, base terminal will work.

<br>

- Make sure to have <code>"build": "react-scripts build"</code> in your "package.json" -> "scripts"

<br>

- Create a new file "deploy.sh" in your app folder
- This script will be run everytime we want to deploy to server, after making changes
- Add the following code in your "deploy.sh" file



```bash
    echo "Switching to branch, master"
    git checkout master

    echo "Building app..."
    npm run build

    echo "Deploying files to server..."
    scp -r build/* uname@{ip}:/var/www/{ip}/

    echo "Done"
```

Open git-bash to run the following command, and grant execution priveleges to the file

```bash
    # cd to the directory of the react app
    cd {path}
    chmod u+x deploy.sh

    # And now run "deploy.sh" to deploy to server
    ./deploy.sh

```

<br><br>

<h1> *******************************************************    END    *******************************************************