"""
# https://edabit.com/challenge/mZqMnS3FsL2MPyFMg
<h1>Numbers to English</h1>
<p>Write a function that accepts a positive integer between 0 and 999 inclusive and 
returns a string representation of that integer written in English.</p>
<pre><code>
num_to_eng(0) ➞ "zero"

num_to_eng(18) ➞ "eighteen"

num_to_eng(126) ➞ "one hundred twenty six"

num_to_eng(909) ➞ "nine hundred nine"

</code></pre>
<h3><span>Notes</span></h3>
<ul><li><span>There are no hyphens used (e.g. "thirty five" not "thirty-five").</span></li>
<li><span>The word "and" is not used (e.g. "one hundred one" not "one hundred and one").</span></li></ul>
"""

def num_to_eng(num):
    eng=['zero','one','two','three','four','five','six','seven','eight','nine',
        'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    digits = str(num)
    return eng[num]