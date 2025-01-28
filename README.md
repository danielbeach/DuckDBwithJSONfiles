### DuckDB + JSON Files (in S3)

This repo goes along with a Substack post that explores using
`DuckDB` with `JSON` files in `S3`.

https://dataengineeringcentral.substack.com/p/duckdb-processing-remote-s3-json


#### To build and deploy the Docker image to assist with DuckDB Dev ...
```
docker build \
  --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  --platform linux/amd64 \
  -t duckjson .
```

To drop into that Docker container ...
```
docker run -it duckjson /bin/bash 
```
