##### Cascade and inheritance
- The cascade (indicates that the order of CSS rules matter)
    - Importance(!important)
        - Conflicting declarations
            - Declarations in user agent style sheets (e.g. the browser's default styles, used when no other styling is set).
            - Normal declarations in user style sheets (custom styles set by a user).
            - Normal declarations in author style sheets (these are the styles set by us, the web developers).
            - Important declarations in author style sheets
            - Important declarations in user style sheets
    - Specificity(measure of how specific a selector is — how many elements it could match.)
            - inline styles(1000)
            - ID selector(100)
            - class selector, attribute selector, or pseudo-class contained inside the overall selector(10)
            - element selector or pseudo-element(1)
            -  Universal selector (*), combinators (+, >, ~, ' ') and negation pseudo-class (:not) have no effect on specificity.
    - Source order(if multiple competing selectors have the same importance and specificity, the third factor that comes into play to help decide which rule wins is source order — later rules will win over earlier rules. )
    - A note on rule mixing
        - all this happens at the property level — properties override other properties, but you don't get entire rules overriding other rules. When several CSS rules match the same element, they are all applied to that element. Only after that are any conflicting properties evaluated to see which individual styles will win over others.
- Inheritance
    - Controlling inheritance
        - inherit, initial, unset, revert
    - Resetting all property values
        - all


