## nginx是什么

> *Nginx* (engine x) 是一个高性能的 [HTTP](https://baike.baidu.com/item/HTTP) 和[反向代理](https://baike.baidu.com/item/%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86/7793488)服务器，也是一个 IMAP/POP3/SMTP [服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8/100571)。 其特点是占有内存少，并发能力强。
>
> ----百度百科

## 为什么

1. 作为 http server
2. 作为反向代理实现负载均衡。

对外部仅暴露一个端口，让用户来访问，然后通过nginx实现端口映射，从而提供不同的服务.

![](https://note.youdao.com/yws/public/resource/a84cb61f17061803a6d37d1450c765de/xmlnote/2BC56AA0EE1442BB91F66408358A3537/3017)

## 怎么用

主要是在配置文件中设置端口映射

在server中通过对不同的location进行配置实现。

```shell
server {
    #对80端口进行监听
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
    
    # 127.0.0.1/tomcat
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
	# 127.0.0.1/hello
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

