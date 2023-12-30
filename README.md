# togomori
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
|`TABLE` urls             | one to many relation with URLS table                                                                           |
|`TABLE` cookies          | one to many relation with COOKIES table                                                                        |

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

### 



















