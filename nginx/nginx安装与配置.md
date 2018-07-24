1. 环境：ubuntu 16.04

2. 安装：apt install

3. 配置文件：

   **使用apt安装的软件一般在/etc中**

   **配置nginx的配置文件要进入到ubuntu的指定路径下：/etc/nginx/sites-available**

   修改default：vi default

   修改内容如下：

   ```shell
   server {
   	listen 80 default_server;
   	listen [::]:80 default_server;
   	root /var/www/html;
   
   	# Add index.php to the list if you are using PHP
   	index index.html index.htm index.nginx-debian.html;
   
   	server_name _;
   
   	location /tomcat/ {
   		# First attempt to serve request as file, then
   		# as directory, then fall back to displaying a 404.
   		#try_files $uri $uri/ =404;
   		proxy_pass http://127.0.0.1:8080/;
   		#proxy_redirect off;
   		proxy_set_header Host $host;
   		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
   		proxy_set_header X-Real-IP $remote_addr;
   	}
           location /hello/ {
                   # First attempt to serve request as file, then
                   # as directory, then fall back to displaying a 404.
                   #try_files $uri $uri/ =404;
                   proxy_pass http://127.0.0.1:5000/index;
                   #proxy_redirect off;
                   proxy_set_header Host $host;
                   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                   proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

   

4. 修改配置文件后要进行配置文件重载：sudo service nginx reload

5. 启动nginx：sudo service nginx start

6. 关闭nginx：sudo service nginx stop

   

