# Use an official Python runtime as a parent image
FROM python:latest
# Set the working directory to /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential gcc \
    cmake \
    python3-pip \
    python3-scipy \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip wheel setuptools

COPY requirements.txt /requirements/requirements.txt
RUN pip3 install -r /requirements/requirements.txt


# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt

RUN rm -rf build
RUN mkdir build
RUN cmake -H. -Bbuild
RUN cd build; make
RUN ./build/unit_tests --gtest_output="xml:cpp_junit.xml"
RUN pytest --junitxml=build/pytest.xml --cov=src/
CMD ./build/unit_tests && pytest
