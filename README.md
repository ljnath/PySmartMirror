# PySmartMirror
### Version : 1.0.0


Author : Lakhya Jyoti Nath (ljnath)<br>
Date : June 2021<br>
Email : ljnath@ljnath.com<br>
Website : https://www.ljnath.com


[![GitHub license](https://img.shields.io/github/license/ljnath/PySmartMirror)](https://github.com/ljnath/PySmartMirror/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ljnath/PySmartMirror)](https://github.com/ljnath/PySmartMirror/stargazers)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ljnath/PySmartMirror.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ljnath/PySmartMirror/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ljnath/PySmartMirror.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ljnath/PySmartMirror/context:python)

</br>

## INTRODUCTION

PySmartMirror is a simple smart mirror project written in python3 around Tkinter library.
This is a light weight project and can run on raspberry pi as well.

It can display current time, weather and latest news feeds.
It sports a configuration file `config.json` in the root directory, using which user can customize it to meet their needs.

PySmartMirror uses two web-service viz. darksky.net and opencagedata.com for fetching the weather and location details.
User has to enter the latitude and longitude of their city in the `config.json` file; based on which the weather and location information will be automatically retrived from respective web-services.

User also needs to register in both of these services and obtain the free API key, which they need to specify in the `config.json` file.


## DEVELOPMENT

Incase user wants to use different service for fetching weather and location information.
User can write static methods in the `NetworkHandler` which will make the API call, parse the result and save it in the PySmartMirror compatible `Weather` or `Location` model
    
## Give a Star! ⭐️

If you find this repository useful, please give it a star.
Thanks in advance !


## License

Copyright © 2021 [Lakhya's Innovation Inc.](https://github.com/ljnath/) under the [MIT License](https://github.com/ljnath/PySmartMirror/blob/master/LICENSE).