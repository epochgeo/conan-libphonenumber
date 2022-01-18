cmake_minimum_required(VERSION 3.1)
project(cmake_wrapper)

message("########################")
include(conanbuildinfo.cmake)
conan_basic_setup()

message(${CONAN_INCLUDE_DIRS})
message(${CONAN_LIB_DIRS})
include_directories(BEFORE ${CONAN_INCLUDE_DIRS})
link_directories(BEFORE ${CONAN_LIB_DIRS})
link_libraries(${CONAN_LIBS} ${CONAN_SYSTEM_LIBS})

set(CMAKE_PREFIX_PATH ${CONAN_ICU_ROOT}/bin ${CMAKE_PREFIX_PATH})

#message(${CONAN_ICU_ROOT})

add_subdirectory("source_subfolder/cpp")
