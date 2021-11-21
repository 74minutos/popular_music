from google.cloud import bigquery

# upload to BigQuery

def upload_to_bigquery():
    client = bigquery.Client(project='crafty-student-288207')

    table_ref = client.dataset("popular_music").table("popular_music_history")

    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1 # ignore the header
    job_config.field_delimiter = ";"
    job_config.autodetect = True

    with open("popular_music_split.csv", "rb") as source_file:
        job = client.load_table_from_file(
            source_file, table_ref, job_config=job_config
        )

    # job is async operation so we have to wait for it to finish

    job.result()

upload_to_bigquery()
