# Airbyte
Data Integration was done using Airbyte.
Airbyte is an open source tool with easy integration with dbt and Airflow.

The primary reason I chose Airbyte is to learn a new tool, so that integration with multiple data sources is possible.

# Starting Airbyte
- We first clone the Airbyte repo which contains the Airbyte Docker file.
```
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
```
- Now to run Airbyte, simply execute the following:
```
./run-ab-platform.sh 
```

# Local file integration
Since we are running Airbyte on Docker, our local files need to transferred to the Docker volume.
From this Docker volume, the data will be transferred to the Destination (Postgres in this case).

However, there are some issues when dealing with Airbyte Docker.
In case of a locally stored file, it's necessary to change the values for `LOCAL_ROOT`, `LOCAL_DOCKER_MOUNT` and `HACK_LOCAL_ROOT_PARENT` in the `.env` file to an existing absolute path on your machine (colons in the path need to be replaced with a double forward slash, `//`).
`LOCAL_ROOT` & `LOCAL_DOCKER_MOUNT` should be the same value, and `HACK_LOCAL_ROOT_PARENT` should be the parent directory of the other two.

By default, the `LOCAL_ROOT` env variable in the `.env` file is set to `/tmp/airbyte_local`.
Also, by default, this volume is mounted from `/tmp/airbyte_local` on the host machine (my system).

The local mount is mounted by Docker onto `LOCAL_ROOT`. This means the `/local` is substituted by `/tmp/airbyte_local` by default.

Therefore, when you write the location of the source, you need not write `/path/to/file.csv` (over here: `/tmp/airbyte_local/source.csv`) but instead `/local/source.csv`

This is because, If you setup a pipeline using one of the local File based destinations (CSV or JSON), Airbyte is writing the resulting files containing the data in the special `/local/` directory in the container.

## TLDR:
- Change `LOCAL_ROOT` and `LOCAL_DOCKER_MOUNT` in the `.env` file to the directory where your file is located.
- Change `HACK_LOCAL_ROOT_PARENT`  in the `.env` file to the parectory directory of the above directory.
- In **Airbyte**, under `Sources` the location would be `/local/<filename>.csv`

So you need to navigate to this local folder on the filesystem of the machine running the Airbyte deployment to retrieve the local data files.

