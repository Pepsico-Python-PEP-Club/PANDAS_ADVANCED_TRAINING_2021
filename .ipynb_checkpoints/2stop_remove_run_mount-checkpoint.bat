docker stop dx_pyspark_root

docker rm dx_pyspark_root

docker run -dp 8889:8888 -p 4040:4040 ^
-it --mount type=bind,source=%cd%,target=/home/VOLUMES ^
--name dx_pyspark_root ^
dx/pyspark_root ^
jupyter lab --ip=0.0.0.0 --port=8888 --NotebookApp.token='' --allow-root
pause
