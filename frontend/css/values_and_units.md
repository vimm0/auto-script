##### CSS values and units
- Type of Css values and units
    - Numeric values
        - Length and size
            - absolute units: Pixels (px) (1px = 1/96th of 1in)
                - Q, mm, cm, in: Quarter millimeters, millimeters, centimeters, or inches
                    - inches (1in = 96px = 2.54cm)
                - px, pt, pc: Points (1/72 of an inch) or picas (12 points) 
                    - points (1pt = 1/72 of 1in)
                    - picas (1pc = 12 pt)
                - Angle units
                    - deg, grad, rad, turn
                - Time units
                    - s, ms
                - Frequency units
                    - Hz, kHz
                - Resolution unit
                    - dpi(Dots per inch), dpcm(Dots per centimetre), dppx(Dots per px unit), x
            - relative units:
                - em (emphemeral unit), rem (root em)
                - ex, ch, cap, ch, ic, lh, rlh
                - vw, vh, vi, vb, vmin, vmax
        - Unitless values
            - Unitless line height
            - Number of animations
    - Percentages(relative to parent)
    - Colors
        - Hexadecimal values
        - RGB
        - HSL :hsl() function accepts hue, saturation, and lightness
        - RGBA and HSLA
        - Opacity
    - Functions
        - rgb()
        - hsl()
        - url(), linear-gradient(), rotate(), translate(), calc()
- Data types
    - Textual data types
        - `<custom-ident>`
        - `<string>`
        - Pre-defined keyword values
            - Pre-defined keywords as an `<ident>`
            - left | right | none | inline-start | inline-end
        - CSS-wide values
            - initial, inherit, and unset, revert
        - URLs
            - `<url>`
    - Numeric data types
        - `<integer>`
        - `<number>`
        - `<dimension>` / Dimensions:
            - `<length>` (Distance units)
            - `<angle>`
            - `<time>`
            - `<frequency>`
            - `<resolution>`
        - <percentage>
        - Mixing percentages and dimensions
            - `<frequency-percentage>`
            - `<angle-percentage>`
            - `<time-percentage>`
        - Special data types (defined in other specs)
            - `<color>`
            - `<image>`
            - `<position>`
        - Functional notation
            - calc()
            - min()
            - max()
            - clamp()
            - toggle()
            - attr()
- https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Values_and_units
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units