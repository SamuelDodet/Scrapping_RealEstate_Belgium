import concurrent.futures
from utils import utils


if __name__=="__main__":
    
    list_threads = list(range(1, 21))
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(utils.parsing_page, list_threads)