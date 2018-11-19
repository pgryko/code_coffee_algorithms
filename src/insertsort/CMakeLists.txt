cmake_minimum_required(VERSION 3.12)
project(insertsort)

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Link runTests with what we want to test and the GTest and pthread library
#target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)

set(CMAKE_CXX_STANDARD 17)

add_executable(insertsort main.cpp)

target_link_libraries(insertsort ${GTEST_LIBRARIES} pthread)