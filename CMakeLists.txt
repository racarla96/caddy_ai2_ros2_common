cmake_minimum_required(VERSION 3.10)
project(caddy_ai2_ros2_common)

find_package(ament_cmake REQUIRED)

add_library(socketcan_interface
  src/socket_can_interface.cpp
)

target_include_directories(socketcan_interface
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

install(
  TARGETS socketcan_interface
  EXPORT export_socketcan_interface
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
)

install(
  DIRECTORY include/
  DESTINATION include
)

ament_export_targets(export_socketcan_interface)
ament_export_include_directories(include)
ament_export_libraries(socketcan_interface)

ament_package()
