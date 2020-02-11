

1. install

 pip3 install pycrypto --user
 pip3 install pymysql --user

2. mysql setting
   support chinese
   db : 'spider' 
   table : 'music163_comments'
   struct : 
    CREATE TABLE `music163_comments` (
    `id` int(20) NOT NULL,
    `artistname` varchar(50) NOT NULL,
    `songname` varchar(100) DEFAULT NULL,
    `comment` varchar(1000) NOT NULL,
    `support` int(10) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

3. run
 python3 ./main.py



