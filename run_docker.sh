# Build Image
docker build -t wiki_api .

# Verify image 
docker image ls

# Run docker image 
docker run -p 8000:5000 wiki_api