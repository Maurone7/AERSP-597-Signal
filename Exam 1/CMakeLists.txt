cmake_minimum_required(VERSION 3.0)
project(Ex5)

find_package(OpenCV REQUIRED)
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable(Ex5 Ex5.cpp)
target_link_libraries(Ex5 ${OpenCV_LIBS})