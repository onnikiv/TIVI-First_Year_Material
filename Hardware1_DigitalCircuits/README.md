## !Latex doesn't render correctly on all of the equations on Github!

### Content
This repository contains assignments and exercises from the Digital Circuits sub-course of the Hardware 1 course in the Information and Communication Technology Engineer program at Metropolia University of Applied Sciences. 
___
### How To (Note for myself)
 
 - Export Markdown to HTML
 - Add script to HTML.
 - Print HTML to PDF.



```html
 </style>

<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script>
<!--ADD THESE so the equations render correctly in HTML-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>
<script type="text/javascript">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']]
        }
    });
</script>

</head>
<body>
```
___
