cmake_minimum_required(VERSION 2.8)
project(lrucache)

# Locate GTest
find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

# Link runTests with what we want to test and the GTest and pthread library
#target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Debug)

add_executable(lrucache lrucache.cpp)

target_link_libraries(lrucache ${GTEST_LIBRARIES} pthread)
