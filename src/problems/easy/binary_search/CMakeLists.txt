cmake_minimum_required(VERSION 3.16)
project(binarysearch)

# Locate GTest
find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

# Link runTests with what we want to test and the GTest and pthread library
#target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++2a")
set(CMAKE_BUILD_TYPE Debug)

add_executable(binarysearch main.cpp)

target_link_libraries(binarysearch ${GTEST_LIBRARIES} pthread)