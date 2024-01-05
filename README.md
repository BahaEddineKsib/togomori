<p align="center">
  <img src="https://github.com/BahaEddineKsib/togomori/assets/61380052/bff23465-a24a-4750-b9e4-bc511a6bdb61" width="270">
</p>

# TOGOMORI
Togomori is a comprehensive solution for *web applications reconnaissance* designed to simplify the process of *information gathering* and *data visualization*. 
It comprises three main components: 
* Command-line Application:<br>
  At the core of Togomori is a Python-based command-line application. It is equipped with features, These features serve as the workhorse for gathering information from various sources and give the freedom to hackers to work simultaneously on **Manual/automated** functionalities.
* JSON Database:<br>
  Within the Command-line Application, an integrated storing system takes charge of managing the data collected. This system organize and structure the information into JSON format. It not only ensures that data is efficiently stored but also enables easy retrieval, analysis, and sharing.
* Grafana Interface:<br>
  Grafana can serve as the visualization and interpretation hub of the system. It offers an interface that transforms the raw data obtained by the JSON Database into clear and customized views. These views are personalized, tailored to individual needs, and serve to provide a comprehensive and intelligible perspective on the target. By presenting the data in a visually compelling manner, the Grafana interface empowers users to gain deeper insights into their findings.

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
|javascript         | htmlsession render|                                                                             |
|urls               | wordlists/js scan | look for urls per sub-domain by wordlist or scanning the js files           |
|urls parameters    | requests/wordlists| look for url's parameters                                                   |
|http scenario recrd| mitmweb           | record a scenario of requests that being send after an action               |
|html inputs        | web scraping      | locate all html inputs in a web page                                        |
|cookies            | cookie jar/records| get websites cookies                                                        |

---------------------------------------------------------------------------------------------------------------------
## Possible Tables/classes
### WORKSHOP
it contains informations about specific mission.
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the workshop                                                                       |
|`VAR..` name             | Workshop's name                                                                                                |
|`TABLE` domains          | domains table                                                                                                  |
|`TABLE` https_captures   | HTTPS_CAPTURES table                                                                                           |
### DOMAINS
it contain information about a domain/sub-domain.
|      column name        |                                              definition                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------|
|`VAR..` id               | a unique number to identify the domain                                                                         |
|`VAR..` tag              | a unique tag , ***main*** for the main domain ex:www.exemple.com , ***sub*** for sub-domains ex:ftp.exemple.com|
|`VAR..` domain           | the domain                                                                                                     |
|`LIST.` techs            | a list of frameworks and technologies been used in the domain                                                  |
|`FILE.` whois            | a variable that points to a file contains the output of whois                                                  |
|`VAR..` ip               | ip address                                                                                                     |
|`MAP..` ports            | a map list contains the port:protocol                                                                          |
|`FILE.` server           | a variable that points to a file contains the output of nmap scan to exploit the OS                            |
|`FILE.` robots           | a variable that points to a file contains the robots.txt                                                       |
|`LIST.` jsfiles `FILE`   | a list of variables they point to javascript files                                                             |
|`TABLE` urls             | URLS table                                                                                                     |
|`TABLE` cookies          | COOKIES table                                                                                                  |

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
## FEATURES
* **ItAffects** : this column to determinate the feature affects which table(s).
* **TYPE** :
  * *CRUD* : crud is basic feature ( create, read, update, delete ) an object.

|    Command        |      description        |   type  |   ItAffects       |
|-------------------|-------------------------|:-------:|:-----------------:|
|setWorkshop        | set a workshop          |   ---   |        ---        |
|addWorkshop        | add a worshop           |  `CRUD` |   *worshops*      |
|displayWorkshop    | display a worshop       |  `CRUD` |   *worshops*      |
|updateWorkshop     | update a worshop        |  `CRUD` |   *worshops*      |
|deleteWorkshop     | delete a worshop        |  `CRUD` |   *worshops*      |
|addDomain          | add a domain            |  `CRUD` |    *domains*      |
|displayDomain      | display a domain        |  `CRUD` |    *domains*      |
|updateDomain       | update a domain         |  `CRUD` |    *domains*      |
|deleteDomain       | delete a domain         |  `CRUD` |    *domains*      |
|addUrl             | add a url               |  `CRUD` |      *urls*       |
|displayUrl         | display a url           |  `CRUD` |      *urls*       |
|updateUrl          | update a url            |  `CRUD` |      *urls*       |
|deleteUrl          | delete a url            |  `CRUD` |      *urls*       |
|addParameter       | add a parameter         |  `CRUD` |    *parameters*   |
|displayParameter   | display a parameter     |  `CRUD` |    *parameters*   |
|updateParameter    | update a parameter      |  `CRUD` |    *parameters*   |
|deleteParameter    | delete a parameter      |  `CRUD` |    *parameters*   |
|addCookie          | add a cookie            |  `CRUD` |     *cookies*     |
|displayCookie      | display a cookie        |  `CRUD` |     *cookies*     |
|updateCookie       | update a cookie         |  `CRUD` |     *cookies*     |
|deleteCookie       | delete a cookie         |  `CRUD` |     *cookies*     |
|addCapture         | add a capture           |  `CRUD` |     *captures*    |
|displayCapture     | display a capture       |  `CRUD` |     *captures*    |
|updateCapture      | update a capture        |  `CRUD` |     *captures*    |
|deleteCapture      | delete a capture        |  `CRUD` |     *captures*    |
|addTransaction     | add a transaction       |  `CRUD` |   *transactions*  |
|displayTransaction | display a transaction   |  `CRUD` |   *transactions*  |
|updateTransaction  | update a transaction    |  `CRUD` |   *transactions*  |
|deleteTransaction  | delete a transaction    |  `CRUD` |   *transactions*  |

  * *CRAFT* : craft is a more complex feature than a simple crud that requires more sophisticated functions.













