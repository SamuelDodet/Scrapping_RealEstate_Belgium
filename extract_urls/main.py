import concurrent.futures
from utils import needed_list, utils


def multi_extract():

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(utils.extract_urls, needed_list.provinces_house)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(utils.extract_urls, needed_list.provinces_apptmnt)

    folder = "../data_set/temp/"
    utils.sort_merge_urls(folder)

if __name__=="__main__":
    multi_extract()
