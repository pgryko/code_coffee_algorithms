# Use an official Python runtime as a parent image
FROM gcc
# Set the working directory to /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    cmake \
    python3-pip

RUN pip3 install --upgrade pip wheel setuptools

COPY requirements.txt /requirements
RUN pip3 install -r /requirements/requirements.txt


# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt

RUN rm -rf build
RUN mkdir build
RUN cmake -H. -Bbuild
RUN cd build; make
RUN ./build/unit_tests --gtest_output="xml:cpp_junit.xml"
RUN pytest --junitxml=build/pytest.xml
CMD ./build/unit_tests && pytest
