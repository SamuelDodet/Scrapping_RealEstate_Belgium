# Scrapping_RealEstate_Belgium


[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/samuel-dodet/)


![Logo](https://github.com/SamuelDodet/Scrapping_RealEstate_Belgium/blob/main/image/logo.png)
<!-- PROJECT LOGO -->
<br />
<p align="center">
    

  <h3 align="center">Scrapping Real Estate Belgium</h3>

  <p align="center">
    Project done during BeCode Bootcamp.
    <br />
    <a href="https://becode.org/learn/ai-bootcamp/"><strong> BeCode BootCamp </strong></a>
    <br />
    <br />

  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Conclusion</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


#### Mission
The mission is: To collect as much data as possible about the market price of real estate in Belgium, in order to build
a dataset that can be used later to create an AI.

#### Constraints:
- Get data from all over Belgium.
- Deliver a .CSV file with a minimum of 10 000 entries.
- No empty fields.
- No duplicates.
- Always record numerical values if possible.

#### Objective:
Create a program capable of scraping one (or more ?) real estate websites while respecting all constraints.

#### Solution: 

The bot will work in two phases:

- Creating a base Database of URLs from Immoweb of houses available.
- Scrap this list of Url with all features that light be relevant for the AI price predictor.
- Once the database is created, run update_main.py to update all new houses appearing
on the website based on the last id scrap from the first created DB
  
Note that multithreading will be use in order to optimize time execution
  

### Built With

To achieve this challenge, here are the main framework use in it:

* [Pandas](https://pandas.pydata.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Selenium](https://selenium-python.readthedocs.io/)



<!-- GETTING STARTED -->
## Getting Started



### Installation


1. Clone the repo
   ```sh
   git clone git@github.com:SamuelDodet/Scrapping_RealEstate_Belgium.git
   ```
2. Install NPM packages
   ```sh
   pip install requirement.txt
   ```
   or
   ```sh
   pip3 install requirement.txt
   ```
3. Website Scrapped
   
    * https://www.immoweb.be/fr



<!-- USAGE EXAMPLES -->
## Usage

#### Extract urls:
   * Multi-threading:
     * extract available house from each province in parallel
    
#### Initial Database:
  * Extract features  using multi-thread(20)
    
  * features: 
      * 44 features extract from Price to Cadastral Income (see /extract_urls/utils/needed_list.py)
* Will create your base database containing approximately 50 000 houses(directory : /data_set/db_immoweb.csv)


<!-- ROADMAP -->
## Conclusion

The database generated is a good base to construct a model of price prediction or 
to analyse the state of Belgian Market




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

### Team Members
Samuel Dodet - [@Linkedin](https://www.linkedin.com/in/samuel-dodet/) - samuel.dodet3@gmail.com

Jeremy Lipszic - [@Linkedin](https://www.linkedin.com/in/jeremy-lipszyc/) - jeremylipszyc@gmail.com

Yolann Sabaux - [@Linkedin](https://www.linkedin.com/in/yolannsabaux/) - yolann.sabaux@gmail.com

Clement Hannecourt - [@Linkedin](https://www.linkedin.com/in/haenecour/) - cl.haenecour@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/SamuelDodet/Scrapping_RealEstate_Belgium)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
