from dotenv import load_dotenv
import os

load_dotenv()
def main()-> None:
    BOT_KEY=os.getenv("BOT_KEY")
    print(BOT_KEY)


main()
