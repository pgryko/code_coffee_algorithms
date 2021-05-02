cmake_minimum_required(VERSION 2.8)
project(hash_with_chaining)

# Locate GTest
find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

# Link runTests with what we want to test and the GTest and pthread library
#target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Debug)

add_executable(hash_with_chaining main.cpp)

target_link_libraries(hash_with_chaining ${GTEST_LIBRARIES} pthread)
