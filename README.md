docker build -t <whatever> .

docker run -d -p 3000:3000 -e PORT=3000 --name hello-flask <whatever>
