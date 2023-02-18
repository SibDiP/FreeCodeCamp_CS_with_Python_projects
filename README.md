<h1>Polygon Area Calculator</h1>
<p>This is a 4/5 training <a href="https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator">project</a> for the <a href="https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects">freeCodeCamp: Scientific Computing with Python</a> course.</p>
<h2>Task Description:</h2>
<p>You will be <a href="https://replit.com/github/freeCodeCamp/boilerplate-polygon-area-calculator" target="_blank" rel="noopener noreferrer nofollow">working on this project with our Replit starter code</a>.</p>
<ul>
<li>Start by importing the project on Replit.</li>
<li>Next, you will see a <code>.replit</code> window.</li>
<li>Select <code>Use run command</code> and click the <code>Done</code> button.</li>
</ul>
<hr><div><section id="instructions">
<p>In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.</p>
<h2>Rectangle class</h2>
<p>When a Rectangle object is created, it should be initialized with <code>width</code> and <code>height</code> attributes. The class should also contain the following methods:</p>
<ul>
<li><code>set_width</code></li>
<li><code>set_height</code></li>
<li><code>get_area</code>: Returns area (<code>width * height</code>)</li>
<li><code>get_perimeter</code>: Returns perimeter (<code>2 * width + 2 * height</code>)</li>
<li><code>get_diagonal</code>: Returns diagonal (<code>(width ** 2 + height ** 2) ** .5</code>)</li>
<li><code>get_picture</code>: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (<code>\n</code>) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".</li>
<li><code>get_amount_inside</code>: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.</li>
</ul>
<p>Additionally, if an instance of a Rectangle is represented as a string, it should look like: <code>Rectangle(width=5, height=10)</code></p>
<h2>Square class</h2>
<p>The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The <code>__init__</code> method should store the side length in both the <code>width</code> and <code>height</code> attributes from the Rectangle class.</p>
<p>The Square class should be able to access the Rectangle class methods but should also contain a <code>set_side</code> method. If an instance of a Square is represented as a string, it should look like: <code>Square(side=9)</code></p>
<p>Additionally, the <code>set_width</code> and <code>set_height</code> methods on the Square class should set both the width and height.</p>
<h2>Usage example</h2>
<pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">rect <span class="token operator">=</span> shape_calculator<span class="token punctuation">.</span>Rectangle<span class="token punctuation">(</span><span class="token number">10</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>rect<span class="token punctuation">.</span>get_area<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
rect<span class="token punctuation">.</span>set_height<span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>rect<span class="token punctuation">.</span>get_perimeter<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>rect<span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>rect<span class="token punctuation">.</span>get_picture<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

sq <span class="token operator">=</span> shape_calculator<span class="token punctuation">.</span>Square<span class="token punctuation">(</span><span class="token number">9</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>sq<span class="token punctuation">.</span>get_area<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
sq<span class="token punctuation">.</span>set_side<span class="token punctuation">(</span><span class="token number">4</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>sq<span class="token punctuation">.</span>get_diagonal<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>sq<span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>sq<span class="token punctuation">.</span>get_picture<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

rect<span class="token punctuation">.</span>set_height<span class="token punctuation">(</span><span class="token number">8</span><span class="token punctuation">)</span>
rect<span class="token punctuation">.</span>set_width<span class="token punctuation">(</span><span class="token number">16</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>rect<span class="token punctuation">.</span>get_amount_inside<span class="token punctuation">(</span>sq<span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<p>That code should return:</p>
<pre class="language-bash" tabindex="0" role="region" aria-label=" code example"><code class="language-bash">50
26
Rectangle(width=10, height=3)
**********
**********
**********<br>
81
5.656854249492381
Square(side=4)
****
****
****
****

8
</code></pre>
<p>The unit tests for this project are in <code>test_module.py</code>.</p>
<h2>Development</h2>
<p>Write your code in <code>shape_calculator.py</code>. For development, you can use <code>main.py</code> to test your <code>shape_calculator()</code> function. Click the "run" button and <code>main.py</code> will run.</p>
<h2>Testing</h2>
<p>We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.</p></code></pre></code></pre></section></div>