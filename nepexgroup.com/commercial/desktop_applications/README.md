#####  Prob;em during desktop application
- Securing the Django/Python code
    - stop reverse engineering
    - you can compile python to the PYC by doing
        ```
        import compileall
        
        compileall.compile_dir('Lib/', force=True)
        ```
    - we had to modify django to allow for the pyc files
    - we encrypted all the html files so our customer cannot modify them.
    - we did this by creating our own "template loader"
    
- finding a django web server that could be embedded into c++
    - we tried the django development web server(single threaded)
        - bad idea!
    - we tried a C++ web server
        - too slow
    - we settled on cherrypy which is a multi threaded web server. the django project is called django-cpserver.    
- finding a database that is easy to install
    - we tried a number of database engines
        - `PostgreSQL`: hard to install on windows machine
        - `SQLite3`: Not good for networks
    - So the one we choose was `firebird`
        - easy to install
        - open source
        - works with django using third party plugin
- finding a browser that could be embedded into c++
    - we tried to embed microsoft internet explorer and ran a mile!
    - so we went for CEF (Chromium Embedded Framework) basically it's Google Chrome.
    - why CEF
        - open source
        - cross platform
        - used in many big applications
            - spotify
            - steam client
            - github for window
            - Adobe Dreamweaver CC
- Testing
    - selemium didn't work with the CEF version we are using. So we had to use a different testing tool. We settled on sikuli.
    - so how does sikuli works
        by image recognition        
- Reports
    - we needed away of generating PDF's so we chose reportlab
    - written in python
    - not very well coded
        - written like a old style c program
    - hard to understand
    
- why did we choose django for a desktop application?
    - future proof(cloud computing)
    - faster writing in python than C++
    - html can look beetter than normal microsof dialog boxes
    - network compatible
- [Thomas Turner - Using Django in a desktop application, at DjangoCon Europe 2015, Cardiff](https://vimeo.com/133547028)
