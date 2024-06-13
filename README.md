# Spark and Jupyter Docker Compose Setup

This repository provides a Docker Compose configuration to set up an Apache Spark cluster with a Jupyter Notebook for running PySpark jobs.

## Services

The Docker Compose file sets up the following services:
- `spark-master`: The Spark master node.
- `spark-worker0`, `spark-worker1`, `spark-worker2`: Three Spark worker nodes.
- `jupyter`: A Jupyter Notebook server with PySpark integration.

## Directory Structure

```
.
├── data/              # Data directory for Spark jobs
├── notebooks/         # Jupyter notebooks
├── spark_jobs/        # Directory for Spark job scripts
├── docker-compose.yml # Docker Compose configuration file
└── README.md          # This README file
```

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Usage

### Step 1: Build and Start the Cluster

To start the Spark cluster and Jupyter Notebook server, run:

```bash
docker-compose up -d
```

This command will build and start the containers in detached mode.

### Step 2: Access the Services

- **Spark Master UI**: [http://localhost:4040](http://localhost:4040)
- **Jupyter Notebook**: [http://localhost:8888](http://localhost:8888)

### Step 3: Running a Spark Job

To run a Spark job, follow these steps:

1. **Access Spark Master Container**:

    ```bash
    docker exec -it spark_master bash
    ```

2. **Run a Spark Job**:

    Assuming you have a Spark job script located in the `./spark_jobs/` directory, you can run it using `spark-submit`. For example:

    ```bash
    spark-submit /opt/bitnami/spark/jobs/your_spark_job.py
    ```

### Step 4: Viewing Logs

- **Jupyter Logs**:

    To view the logs of the Jupyter service, run:

    ```bash
    docker logs jupyter
    ```

- **Spark Master Logs**:

    To view the logs of the Spark master service, run:

    ```bash
    docker logs spark_master
    ```

- **Spark Worker Logs**:

    To view the logs of the Spark worker services, run:

    ```bash
    docker logs spark_worker0
    docker logs spark_worker1
    docker logs spark_worker2
    ```

### Step 5: Stopping the Cluster

To stop and remove all the containers, run:

```bash
docker-compose down
```

## Assignment

1. **Download Docker**:
   - If you don't already have Docker installed, download and install it from [here](https://www.docker.com/get-started).

2. **Run the Docker Compose File**:
   - Use the provided `docker-compose.yml` file to set up and run the Spark cluster and Jupyter Notebook server.

3. **Connect to a Database**:
   - Connect to any database (e.g., MySQL, PostgreSQL) from your Jupyter notebook. You can use the `pyspark.sql` library to establish the connection.

4. **Read Data**:
   - Read data from the connected database into a Spark DataFrame.

5. **Apply a Simple Transformation**:
   - Perform a simple transformation on the DataFrame, such as filtering, aggregation, or any other basic operation.

6. **Write the Result to Local Machine**:
   - Write the transformed data to your local machine as a CSV file. Save it in the `./data/` directory.

If you face any problems, please ping me, and I'll help.

## Notes

- Ensure that the directories `./data/`, `./notebooks/`, and `./spark_jobs/` exist and have the necessary permissions.
- You can place your data files in the `./data/` directory and access them within the containers at `/opt/bitnami/spark/data/`.
- You can place your Spark job scripts in the `./spark_jobs/` directory and access them within the containers at `/opt/bitnami/spark/jobs/`.
- You can place your Jupyter notebooks in the `./notebooks/` directory and access them within the Jupyter container at `/home/jovyan/work`.

## Troubleshooting

If you encounter any issues, you can check the logs of the respective services for more information.

## License

This project is licensed under the MIT License.
```

To use this `README.md` file:
1. Save it in the root of your project directory (where your `docker-compose.yml` is located).
2. Follow the instructions provided in the README to set up and run your Docker Compose environment.
3. Complete the assignment tasks as specified.