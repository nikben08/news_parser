import rusbase_parser
import neurohive_parser
import ai_news_parser
import hi_news_parser
import vc_parser
import time

while True:  # Цикл который по очереди запускает каждый парсер
    rusbase_parser.rusbase_parser()
    neurohive_parser.neurohive_parser()
    ai_news_parser.ai_news_parser()
    hi_news_parser.hi_news_parser()
    vc_parser.vc_parser()
    time.sleep(1800)






