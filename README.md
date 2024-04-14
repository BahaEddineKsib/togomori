<p align="center">
  <img src="https://github.com/BahaEddineKsib/togomori/assets/61380052/bff23465-a24a-4750-b9e4-bc511a6bdb61" width="270">
</p>

# TOGOMORI
Togomori is a comprehensive solution for *web applications reconnaissance* designed to help on the process of *information gathering* and *data visualization*. 
It comprises three main components: 
* Command-line Application:<br>
  At the core of Togomori is a Python-based command-line application. It is equipped with features, These features serve as the workhorse for gathering information from various sources and give the freedom to hackers to work simultaneously on **Manual/automated** functionalities.
* JSON files/ Flask APIs:<br>
  Within the Command-line Application, an integrated storing system takes charge of managing the data collected. This system organize and structure the information into JSON format. By the help of **Flask** we can enable easy retrieval, and sharing JSONs as an **APIs**.
* Grafana Interface:<br>
  Grafana can serve as the visualization and interpretation hub of the system. It offers an interface that transforms the raw data obtained by the Flask APIs into clear and customized views. These views are personalized, tailored to individual needs, and serve to provide a comprehensive and intelligible perspective on the target. By presenting the data in a visually compelling manner, the Grafana interface empowers users to gain deeper insights into their findings.

------------------------------------------------------------------------------------------------------------------
## Users
* An `organization` can use TOGOMORI to effectivly map their external attack surface. and monitor the information they are putting in public from their web applications
* A `Penetration Tester` can use TOGOMORI to gather information in `Black-box` web pentesting Mission.
* A `Bug Bounty Hunter` can use Togomori to get a clear view about the target and tag what assets are in or out of the scope.

------------------------------------------------------------------------------------------------------------------
## things i want to look for

|Asset              | used tech         |                               explanation                                   |
|:-----------------:|:-----------------:|:---------------------------------------------------------------------------:|
|web Technologies   | python-Wappalyzer | Determine the technologies and framework used in the website's development  |
|Domain Information | whois             | IP address, registration information, and DNS records.                      |
|Open Ports         | python-nmap       | open ports on the target system to understand its potential points of entry.|
|Subdomains         | requests/wordlists| Identify subdomains associated with the target website.                     |
|Server Details     | python-nmap       | server hosting the website, including the operating system and version.     |
|robots.txt         | urllib            | Examine robots.txt to discover hidden resources and potential sensitive data|
|javascript         | htmlsession render| capture javascript files                                                    |
|Fetch apis/XHR     | selenium library  | capture Fetch apis and xmlHttpRequests                                      |
|SSL/TLS Certificate| openSSL           | Analyze SSL/TLS certificates for encryption details and domain validation   |
|Email Addresses    |-------------------| Scrape web pages for email addresses associated with the domain.            |
|GitHub             |Github search API  | Discovery of sensitive information by conducting Git recon                  |
|urls               | wordlists/js scan | look for urls per sub-domain by wordlist or scanning the js files           |
|urls parameters    | requests/wordlists| look for url's parameters                                                   |
|http scenario recrd| mitmweb           | record a scenario  of requests/responses that being send after an action like (button clicking)|
|html inputs        | web scraping      | locate all html inputs in a web page                                        |
|cookies            | cookie jar/records| get websites cookies                                                        |

---------------------------------------------------------------------------------------------------------------------
## Possible Tables/classes
### WORKSHOP
it contains informations about specific mission.
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the workshop                                                                       |
|`VAR..` path             | Workshop's path                                                                                                |
|`TABLE` domains          | domains table                                                                                                  |
|`TABLE` https_captures   | HTTPS_CAPTURES table                                                                                           |
### DOMAINS
it contain information about a domain/sub-domain.
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` domain           | ex: www.google.com                                                                                                                                                                        |
|`VAR..` sub              | the subdomain ex: www                                                                                                                                                                     |
|`VAR..` main             | the domain name ex: google                                                                                                                                                                |
|`VAR..` tld              | the top level domain ex: com                                                                                                                                                              |
|`VAR..` tags             | tags to identify a domain with something , for example you can tag a domain "out-of-scope" or in-scope so you can include or exclude a domain from an automation test or filtering by tag |
|`LIST.` techs            | a list of frameworks and technologies been used in the domain                                                                                                                             |
|`FILE.` whois_file       | a variable that points to a file contains the output of whois                                                                                                                             |
|`VAR..` ip               | ip address                                                                                                                                                                                |
|`MAP..` ports            | a map list contains the port:protocol                                                                                                                                                     |
|`FILE.` server_file      | a variable that points to a file contains the output of nmap scan to exploit the OS                                                                                                       |
|`FILE.` robots-file      | a variable that points to a file contains the robots.txt                                                                                                                                  |
|`LIST.` js_files `FILE`  | a list of variables they point to javascript files                                                                                                                                        |
|`TABLE` urls             | URLS table                                                                                                                                                                                |
|`TABLE` cookies          | COOKIES table                                                                                                                                                                             |

### URLS
it contain the list of urls per domain
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the url                                                                            |
|`VAR..` url              | the url                                                                                                        |
|`TABLE` domain           | id of the related domain                                                                                       |
|`TABLE` params           | one to many relation with PARAMETERS table                                                                     |

### PARAMETERS
it contains the list of parameters per url
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the parameter                                                                      |
|`LIST.` param            | the parameter   (it's a list for in case a url contains multiple params)                                       |
|`TABLE` url              | id of the related url                                                                                          |
|`VAR..` type             | type of the parameter Path parameter: ***path*** , Query string parameters ***query***, no parameters ***0***  |
|`LIST.` variables        | the variables been found in the parameters                                                                     |
|`FILE.` body             | a variable that points to a file contains response body in html                                                |

### COOKIES
it contain a list of cookies per domain
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the cookie                                                                         |
|`VAR..` cookie           | the cookie                                                                                                     |
|`VAR..` variable         | the variable been found in the cookie                                                                          |
|`TABLE` domain           | id of the related domain                                                                                       |

### HTTPS_CAPTURES
it contains a list of https transaction , tagged with a specific name.
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the capture                                                                        |
|`VAR..` name             | capture's name                                                                                                 |
|`TABLE` transactions     | TRANSACTIONS table                                                                                             |

### TRANSACTIONS
it contains a http requests and the related response.
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the transaction                                                                    |
|`FILE.` request          | a variable that points to a file contains the https request                                                    |
|`FILE.` response         | a variable that points to a file contains the https response                                                   |

---------------------------------------------------------------------------------------------------------------------
## JSON STRUCTURE
*beta model v0*
```json
{
  "WORKSHOP": [
    {
      "id": 1,
      "name": "ReconForEXAMPLE",
      "path": "/home/xib/wkshp1",
      "domains": [
        {
          "id": 101,
          "tag": "main",
          "domain": "www.example.com",
          "techs": ["Python", "Django"],
          "whois": "whois_output.txt",
          "ip": "192.168.1.1",
          "ports": {"80": "HTTP", "443": "HTTPS"},
          "server": "nmap_output.txt",
          "robots": "robots.txt",
          "jsfiles": ["file1.js", "file2.js"],
          "urls": [
            {
              "id": 1001,
              "url": "/page1",
              "params": [
                {
                  "id": 2001,
                  "param": "id",
                  "type": "query",
                  "variables": ["var1", "var2"],
                  "body": "response_body.html"
                }
              ]
            }
          ],
          "cookies": [
            {
              "id": 3001,
              "cookie": "session_token=xyz",
              "variable": "session",
              "domain": 101
            }
          ]
        }
      ],
      "https_captures": [
        {
          "id": 5001,
          "name": "LoginCapture",
          "transactions": [
            {
              "id": 6001,
              "request": "login_request.txt",
              "response": "login_response.txt"
            }
          ]
        }
      ]
    }
  ],
}

```

---------------------------------------------------------------------------------------------------------------------
## FEATURES
* **ItAffects** : this column to determinate the feature affects which table(s).
* **TYPE** :
  * *CRUD* : crud is basic feature ( create, read, update, delete ) an object.

|    Command        |      description        |   type  |   ItAffects       |RELATED ISSUE
|-------------------|-------------------------|:-------:|:-----------------:|:------------:
|setWorkshop        | set a workshop          |   ---   |        ---        |[#3](https://github.com/BahaEddineKsib/togomori/issues/3)
|addWorkshop        | add a worshop           |  `CRUD` |   *worshops*      |[#3](https://github.com/BahaEddineKsib/togomori/issues/3)
|displayWorkshop    | display a worshop       |  `CRUD` |   *worshops*      |[#3](https://github.com/BahaEddineKsib/togomori/issues/3)
|updateWorkshop     | update a worshop        |  `CRUD` |   *worshops*      |[#3](https://github.com/BahaEddineKsib/togomori/issues/3)
|deleteWorkshop     | delete a worshop        |  `CRUD` |   *worshops*      |[#3](https://github.com/BahaEddineKsib/togomori/issues/3)
|addDomain          | add a domain            |  `CRUD` |    *domains*      |[#4](https://github.com/BahaEddineKsib/togomori/issues/4)
|displayDomain      | display a domain        |  `CRUD` |    *domains*      |[#4](https://github.com/BahaEddineKsib/togomori/issues/4)
|updateDomain       | update a domain         |  `CRUD` |    *domains*      |[#4](https://github.com/BahaEddineKsib/togomori/issues/4)
|deleteDomain       | delete a domain         |  `CRUD` |    *domains*      |[#4](https://github.com/BahaEddineKsib/togomori/issues/4)
|addUrl             | add a url               |  `CRUD` |      *urls*       |[#5](https://github.com/BahaEddineKsib/togomori/issues/5)
|displayUrl         | display a url           |  `CRUD` |      *urls*       |[#5](https://github.com/BahaEddineKsib/togomori/issues/5)
|updateUrl          | update a url            |  `CRUD` |      *urls*       |[#5](https://github.com/BahaEddineKsib/togomori/issues/5)
|deleteUrl          | delete a url            |  `CRUD` |      *urls*       |[#5](https://github.com/BahaEddineKsib/togomori/issues/5)
|addParameter       | add a parameter         |  `CRUD` |    *parameters*   |[#6](https://github.com/BahaEddineKsib/togomori/issues/6)
|displayParameter   | display a parameter     |  `CRUD` |    *parameters*   |[#6](https://github.com/BahaEddineKsib/togomori/issues/6)
|updateParameter    | update a parameter      |  `CRUD` |    *parameters*   |[#6](https://github.com/BahaEddineKsib/togomori/issues/6)
|deleteParameter    | delete a parameter      |  `CRUD` |    *parameters*   |[#6](https://github.com/BahaEddineKsib/togomori/issues/6)
|addCookie          | add a cookie            |  `CRUD` |     *cookies*     |[#7](https://github.com/BahaEddineKsib/togomori/issues/7)
|displayCookie      | display a cookie        |  `CRUD` |     *cookies*     |[#7](https://github.com/BahaEddineKsib/togomori/issues/7)
|updateCookie       | update a cookie         |  `CRUD` |     *cookies*     |[#7](https://github.com/BahaEddineKsib/togomori/issues/7)
|deleteCookie       | delete a cookie         |  `CRUD` |     *cookies*     |[#7](https://github.com/BahaEddineKsib/togomori/issues/7)
|addCapture         | add a capture           |  `CRUD` |     *captures*    |[#8](https://github.com/BahaEddineKsib/togomori/issues/8)
|displayCapture     | display a capture       |  `CRUD` |     *captures*    |[#8](https://github.com/BahaEddineKsib/togomori/issues/8)
|updateCapture      | update a capture        |  `CRUD` |     *captures*    |[#8](https://github.com/BahaEddineKsib/togomori/issues/8)
|deleteCapture      | delete a capture        |  `CRUD` |     *captures*    |[#8](https://github.com/BahaEddineKsib/togomori/issues/8)
|addTransaction     | add a transaction       |  `CRUD` |   *transactions*  |[#9](https://github.com/BahaEddineKsib/togomori/issues/9)
|displayTransaction | display a transaction   |  `CRUD` |   *transactions*  |[#9](https://github.com/BahaEddineKsib/togomori/issues/9)
|updateTransaction  | update a transaction    |  `CRUD` |   *transactions*  |[#9](https://github.com/BahaEddineKsib/togomori/issues/9)
|deleteTransaction  | delete a transaction    |  `CRUD` |   *transactions*  |[#9](https://github.com/BahaEddineKsib/togomori/issues/9)

  * *Automation command* / *CRAFT* : craft is a more complex feature than a simple crud that requires more sophisticated functions.

|         Command        |                           description                                   |   type  |   ItAffects       |RELATED ISSUE
|------------------------|-------------------------------------------------------------------------|:-------:|:-----------------:|:------------:
|getTechnologies         |Determine the technologies and framework used in the domain development  | `CRAFT` |           *domains*               |
|whois                   |IP address, registration information, and DNS records.                   | `CRAFT` |           *-------*               |
|getPorts                |open ports on the target system and potential points of entry.           | `CRAFT` |           *domains*               |
|getSubdomains           |Identify subdomains associated with the target website.                  | `CRAFT` | *domains* - *urls* - *parameters* |
|getServerDetails        |server hosting the website, including the operating system and version.  | `CRAFT` |           *domains*               |
|getRobots               |Examine robots.txt to get hidden resources and potential sensitive data  | `CRAFT` | *domains* - *urls* - *parameters* |
|getJavascripts          |Examine the website and fetch its js files                               | `CRAFT` |           *domains*               |
|getUrls                 |look for urls per sub-domain                                             | `CRAFT` |     *urls* - *parameters*         |
|captureHttpTransactions |record a scenario of requests that being send after an action            | `CRAFT` |              *ALL*                |
|getHtmlInputs           |locate all html inputs in a web page                                     | `CRAFT` |            undefined              |
|getCookies              |get websites cookies                                                     | `CRAFT` |            *captures*             |

---------------------------------------------------------------------------------------------------------------------
## Grafana interface
  * *beta idea* still under development




