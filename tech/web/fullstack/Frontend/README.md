Frontend Technologies
```
- HTML/CSS
- Javascript/Jquery
- Css and Javascript Framework
- Css Preprocessing
	- SASS
	- LESS
	- Stylus
- Responsive Design
- Testing/Debugging
- Browser Development Tools
- Building Automatic Tools
	- Gulp
	- Grunt
	- Webpack

```

##### Introduction to CSS
- How CSS works
- CSS syntax
- Selectors
- CSS values and units
- Cascade and inheritance
- The box model
- Debugging CSS
##### Styling text
- Fundamental text and font styling
    - Fonts
        - Color
        - Font families
            - Web safe fonts
            - Font stacks
                - `  font-family: Helvetica, Arial, sans-serif;`
        - Font size
        - Font style: `normal| italic| oblique`
        - Font weight: `normal, bold, lighter, bolder, 100–900`
        - Text transform: `none, uppercase, lowercase, capitalize, full-width`
        - Text decoration: `none, underline, overline, line-through`
        - Text drop shadows: `text-shadow`
        - Text layout
            - Text alignment
                -  text-align: `left, right, center, justify`
            - Line height(line-height)
            - Letter and word spacing(letter-spacing and word-spacing)
      
    - Other properties worth looking at:
        - Font styles
            - font-variant
            - font-kerning
            - font-feature-settings
            - font-variant-alternates
            - font-variant-capS
            - font-variant-east-asian
            - font-variant-ligatures
            - font-variant-numeric
            - font-variant-position
            - font-size-adjust
            - font-stretch
            - text-underline-position
            - text-rendering
        - Text layout styles
            - text-indent
            - text-overflow
            - white-space
            - word-break: Specify whether to break lines within words.
            - direction
            - hyphens
            - line-break
            - text-align-last
            - text-orientation
            - word-wrap
            - writing-mode
    - Font shorthand
        - `font: italic normal bold normal 3em/1.5 Helvetica, Arial, sans-serif;`
        ```
        [ [ <'font-style'> || <font-variant-css21> || <'font-weight'> || <'font-stretch'> ]? <'font-size'> [ / <'line-height'> ]? <'font-family'> ] | caption | icon | menu | message-box | small-caption | status-bar
        where 
        <font-variant-css21> = [ normal | small-caps ]
        ```
- Styling lists 
    - List-specific styles
        - list-style-type
        - list-style-position
        - list-style-image
        - list-style shorthand
            - list-style: square url(example.png) inside;
    - Controlling list counting
        - start
        - reversed
        - value 
- Styling links
    - Link states
        - Link (unvisited)
        - Visited
        - Hover
        - Focus
        - Active
- Web fonts
    - @font-face
    
##### Styling boxes
- Box model
    - max-width, min-height, and max-height
    - display
    - padding, border
- Backgrounds
    - background-color: Sets a solid color for the background.
    - background-image: Specifies a background image to appear in the background of the element. This can be a static file, or a generated gradient.
    - background-position: Specifies the position that the background should appear inside the element background.
    - background-repeat: Specifies whether the background should be repeated (tiled) or not.
    - background-attachment: Specifies the behaviour of an element's background when its content scrolls, e.g. does it scroll with the content, or is it fixed?
    - background: Shorthand for specifying the above five properties on one line.
    - background-size: Allows a background image to be resized dynamically
- Borders
    - Border shorthand
        ```
        <line-width> || <line-style> || <color>
        ```
    - Border radius
        - border-top-left-radius, border-top-right-radius, border-bottom-left-radius, and border-bottom-right-radius.
    - Border images
        - border-image-source 
        - border-image-slice
        - border-image-repeat
        - border-image-width
        - border-image-outset
        - shorthand
            `border-image: url(border-image.png) 40 round;`
    - Borders vs. outlines
- Styling tables
    - Spacing and layout
    - typography
    - Graphics and colors
    - Zebra striping
- Advanced box effects
    - Box shadows
        -  text-shadow
    - Multiple box shadows
    - Filters
        - `filter: drop-shadow(5px 5px 1px rgba(0,0,0,0.7));`
    - Blend modes
        - background-blend-mode
        - mix-blend-mode
##### CSS layout
- Introduction to CSS layout
- Normal Flow
- Flex box
- Grids
- Floats
- Positioning
- Multiple-column layout
- Legacy layout methods
- Supporting older browsers
- Fundamental Layout Comprehension

##### Responsive design (TBD)

##### Reference
- https://www.mozilla.org/en-US/styleguide/
