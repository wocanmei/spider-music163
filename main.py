from get_artists import get_artists
from get_songs import get_all_songs
from get_comments import get_hot_comments
from Utils.mysql import MysqlHelper

if __name__ == "__main__":
    get_artists()
    get_all_songs()
    mydb = MysqlHelper('127.0.0.1',3306,'root','123456','spider')
    get_hot_comments(mydb)

