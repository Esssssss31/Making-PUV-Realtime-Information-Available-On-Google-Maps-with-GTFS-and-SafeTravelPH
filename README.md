# SafeTravelPH-GTFS-on-Google-Maps-Project

This is an open source project for publishing a General Transit Feed Specification (GTFS) feed for the public transit system in the Philippines. The project consists of Python scripts for ingesting, processing, and storing real-time transit data, as well as generating a GTFS feed that can be published on Google Maps and other transit mapping platforms.

This project of publishing GTFS feeds to Google Maps uses data from a PUV Driver's tracking mobile app via MQTT and Apache Kafka. The mobile app in this case is the SafeTravelPH app (https://play.google.com/store/apps/details?id=ph.safetravel.app&hl=en&gl=US). A case study of this data system is done with Puerto Princesa City's ISTOPP (Information System for Transport Operations in Puerto Princesa) under the NEDA Innovation Grant in 2022.

Contact the SafeTravelPH Mobility Innovations Organization, Inc. and Puerto Princesa City's City Planning and Development Office for more information and collaboration.

## Project Structure

The project is organized into the following directories:

- `config/`: Configuration files for the project, including API keys and database connection settings.
- `data/`: Example data files for testing the ingestion and processing scripts.
- `scripts/`: Python scripts for ingesting, processing, and storing transit data, as well as generating the GTFS feed.
- `tests/`: Unit tests for the Python scripts.

## Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/{username}/{project_name}.git

2. Install the required Python packages by running:

pip install -r requirements.txt

3. Set up the configuration files in the `config/` directory with your API keys and database connection settings.

## Usage

To run the project, follow these steps:

1. Start the data ingestion script to begin receiving real-time transit data:

python scripts/data_ingestion.py

2. Once data is being ingested, start the data processing script to clean and transform the data into a format suitable for the GTFS feed:

python scripts/data_processing.py

3. After the data has been processed, start the data storage script to store the data in a MongoDB database:

python scripts/data_storage.py

4. Finally, run the GTFS feed script to generate the feed file and upload it to the Google Maps Transit API:

python scripts/gtfs_feed.py


## Contributing

Contributions to the project are welcome and encouraged. To contribute, follow these steps:

1. Fork the repository to your GitHub account.

2. Make changes to the codebase and commit them to your forked repository.

3. Submit a pull request to the main repository with a clear explanation of the changes you have made.

## License

This project is licensed under the [LICENSE] License. See the [LICENSE](LICENSE) file for more details.

***
To connect your completed project to Google Maps or Google Transit, you will need to create a Google Cloud project, enable the Google Transit API, and set up the necessary credentials and authentication.

Here are the basic steps you can follow:

1. Go to the Google Cloud Console (console.cloud.google.com) and create a new project.

2. Enable the Google Transit API for your project by navigating to the API Library and searching for "Transit".

3. Set up authentication by creating a service account and generating a private key for your project. This will allow your project to authenticate with the Google Transit API and access the required resources.

4. Update your project's code to use the Google Transit API client library, which provides a set of APIs and tools for interacting with the API.

5. Use the client library to upload your GTFS feeds to Google Transit and update them with real-time information as it becomes available.

6. Test your integration by checking that your GTFS feeds are being displayed correctly on Google Maps and that real-time updates are being processed and displayed correctly.

The specific implementation details will depend on the programming language and framework you are using for your project, as well as the specific requirements of your transit agency and the Google Transit API. You can refer to the official Google Transit API documentation and client libraries for more information and guidance on how to integrate with the API.

## Registration to Google Transit

To use the Google Transit API and publish your transit agency's data on Google Maps, you need to register your transit agency with Google. This registration process involves providing information about your agency, such as its name, location, and contact information, as well as submitting a data feed in the GTFS format.

Once your agency is registered, you will receive a transit-agency-id that you will need to include in your GTFS feed to associate it with your agency. This ID will be used to identify your agency and its data in the Google Transit API.

You do not need to include any information about your registration or certification in your code or repository. The registration process is separate from the development and deployment of your software, and it is managed through the Google Transit Partner program. Once your agency is registered and your data feed is published on Google Maps, your app or software can access the data using the Google Transit API client library and the appropriate credentials and authentication.

***
Here are the general steps you could follow to build the codebase for a bus transit agency to publish GTFS feeds to Google Maps based on real-time data from a mobile app via MQTT and Apache Kafka:

1. Define the data format: Determine the data format and structure of the real-time data being sent by the mobile app. You may need to use a protocol buffer like GTFS Realtime or define your own data schema.

2. Set up the data pipeline: Use Apache Kafka to set up a data pipeline that can receive the real-time data from the mobile app and forward it to the backend system responsible for generating the GTFS feeds. This pipeline should include components for data ingestion, storage, and processing.

3. Generate the GTFS feeds: Use a backend system like Node.js or Python to generate the GTFS feeds based on the real-time data received from the data pipeline. This system should read the data from the Kafka topics and convert it into the appropriate GTFS format.

4. Publish the GTFS feeds: Publish the GTFS feeds to the Google Transit Data Feed using the GTFS API. This can be done using any HTTP client library in your preferred programming language.

5. Monitor and maintain the system: Set up monitoring and alerting systems to detect any issues with the data pipeline or GTFS feed generation. Regularly review the data to ensure that it is accurate and up-to-date.

These are the basic steps involved in building a codebase for a bus transit agency to publish GTFS feeds to Google Maps based on real-time data from a mobile app via MQTT and Apache Kafka. However, this is a complex task and may require additional steps or considerations based on the specific requirements of your project. (ChatGPT)

***
The estimated time of arrival (ETA) of the bus is calculated by Google Maps using the GTFS real-time data that is published by the transit agency. When a user searches for directions using Google Maps, it queries the GTFS API for real-time information about the transit service, including the location and predicted arrival times of the next bus. The GTFS API then calculates the ETA based on the real-time data and other information such as traffic and historical travel times.

In terms of the codebase, the logic for calculating the ETA is typically handled by the GTFS API and not by the scripts in the project. However, you can customize the display of the ETA in the Google Maps interface by modifying the GTFS feed to include additional information such as the number of stops before a particular destination or the expected travel time between stops.
