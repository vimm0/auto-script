##### MaintainableCSS
- Introduction
    - Modular
        - A module is a distinct, independent unit that can be combined with other modules to create a more complex structure.
    - Scalable
        - as CSS increases in size, it's still easy to maintain.
    - Maintainable
        - Maintainable CSS makes it easy to make styling changes without worrying about accidentally causing problems elsewhere.
- Semantics
    - As Phil Karton says, “there are only two hard things in Computer Science: cache invalidation and naming things.”
    - Semantic classes usually work best.
        1. Because they are readable
        2. Because it's easier to build responsive sites
        3. Because they are easier to find
        4. Because they eliminate the risk of regression
        5. Because visual classes aren't worth it
        6. Because they provide hooks for automated tests
        7. Because they provide hooks for JavaScript
        8. Because they don't need maintaining
        9. Because they are easier to debug
        10. Because the standards recommend it
        11. Because styling state is easier
        12. Because they produce a small HTML footprint
- Reuse
    - As Harry Roberts says, “DRY is often misinterpreted as the necessity to never repeat the exact same thing twice. This is impractical and usually counterproductive, and can lead to forced abstractions, over-thought and over-engineered code.”
- Modules
    - component
- State
- Modifiers
- Versioning
- Organisation
    1. CSS in a single folder

    ```
    path/to/css/
      vendor/
        some3rdParty.css
        someOther3rdParty.css
      yourApp/
        some.css
        global.css
        basket.css
    ```
    2. CSS in a module folder
    ```
    global/
        css/
            resetPerhaps.css
            global.css
            etc.css
    basket/
      controllers/
        ...
      templates/
        basket.html
        emptyBasket.html
      partials/
        basketHeader.html
        basketSummary.html
      js/
        ...
      css/
        basket.css
    header/
    ...
    ```
    3. Use less than 32 CSS files
