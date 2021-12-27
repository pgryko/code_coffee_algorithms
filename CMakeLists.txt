cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(self_study)

enable_language(C)
enable_language(CXX)



if(CMAKE_CXX_COMPILER_ID MATCHES GNU)
    set(CMAKE_CXX_FLAGS         "-Wall -Wno-unknown-pragmas -Wno-sign-compare -Woverloaded-virtual -Wwrite-strings -Wno-unused")
    set(CMAKE_CXX_FLAGS_DEBUG   "-O0 -g3")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage -std=gnu++17")
endif()

include_directories(
    ${PROJECT_SOURCE_DIR}/src
    ${PROJECT_SOURCE_DIR}/src/example
        ${PROJECT_SOURCE_DIR}/src/algorithms/sorting/insertsort
        ${PROJECT_SOURCE_DIR}/src/algorithms/sorting/selectsort
        ${PROJECT_SOURCE_DIR}/src/algorithms/sorting/mergesort
        ${PROJECT_SOURCE_DIR}/src/algorithms/sorting/heapsort
        ${PROJECT_SOURCE_DIR}/src/algorithms/sorting/quicksort
        ${PROJECT_SOURCE_DIR}/src/datastructures/linkedlist
        ${PROJECT_SOURCE_DIR}/src/datastructures/dictionary
        ${PROJECT_SOURCE_DIR}/src/problems/easy/binarysearch
        ${PROJECT_SOURCE_DIR}/src/problems/medium/lrucache
)

add_library(
    example
    src/example/example.cpp
)

set(GOOGLETEST_ROOT external/googletest/googletest CACHE STRING "Google Test source root")

include_directories(
    ${PROJECT_SOURCE_DIR}/${GOOGLETEST_ROOT}
    ${PROJECT_SOURCE_DIR}/${GOOGLETEST_ROOT}/include
    )

set(GOOGLETEST_SOURCES
    ${PROJECT_SOURCE_DIR}/${GOOGLETEST_ROOT}/src/gtest-all.cc
    ${PROJECT_SOURCE_DIR}/${GOOGLETEST_ROOT}/src/gtest_main.cc
    )

foreach(_source ${GOOGLETEST_SOURCES})
    set_source_files_properties(${_source} PROPERTIES GENERATED 1)
endforeach()

add_library(googletest ${GOOGLETEST_SOURCES})

add_executable(
    unit_tests
    test/main.cpp
    test/example_add.cpp
    test/example_subtract.cpp
    test/test_insertsort.cpp
    test/test_selectsort.cpp
    test/test_mergesort.cpp
    test/test_heapsort.cpp
    test/test_quicksort.cpp
    test/test_linkedlist.cpp
    test/test_lrucache.cpp
    test/test_hashchaining.cpp
    test/test_binarysearch.cpp
)

add_dependencies(unit_tests googletest)

target_link_libraries(
    unit_tests
    googletest
    example
    pthread
    )


include(CTest)
enable_testing()

add_test(unit ${PROJECT_BINARY_DIR}/unit_tests)


