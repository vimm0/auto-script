##### The box model
- Box properties
    - width and height
    - padding
    - border
    - margin
        - margin collapsing(When two boxes touch against one another, the distance between them is the value of the largest of the two touching margins, and not their sum.)
- Advanced box manipulation
    - Overflow
        - auto, hidden, visible
    - Background clip
    - Outline
- Types of CSS boxes
    - block: box that's stacked upon other boxes 
    - inline: it flows with the document's text (i.e. it will appear on the same line as surrounding text and other inline elements, and its content will break with the flow of the text, like lines of text in a paragraph.) 
    - inline-block: It flows with surrounding text and other inline elements without creating line breaks before and after it unlike a block box and maintains its block integrity like a block box. 
- https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Box_model
- Block formatting context
    - Margin collapsing
    - Floats
    - Text Wrapping
    - Multi-column Layouts

- Visual formatting model
    - Box generation
        - Block-level elements and block boxes
            - Anonymous block boxes
        - Inline-level elements and inline boxes
            - Anonymous inline boxes
    - Other types of boxes
        - Line boxes
        - Run-in boxes
        - Model-induced boxes
        - Positioning schemes
            - Normal flow
            - Floats
            - Absolute positioning