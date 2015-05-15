docker build -t &lt;whatever&gt; .

docker run -d -p 3000:3000 -e PORT=3000 --name hello-flask &lt;whatever&gt;
