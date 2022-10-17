# Build Image
docker build -t wiki_api .

# Verify image 
docker image ls

# Run docker image 
# docker run -p 5000:5000 wiki_api
docker run -p 127.0.0.1:5000:5000 wiki_api