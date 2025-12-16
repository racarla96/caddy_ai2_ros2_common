cmake_minimum_required(VERSION 3.10)
project(caddy_ai2_ros2_common)

# Establecer el estándar C++20 para todo el proyecto
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

find_package(ament_cmake REQUIRED)

# Build as SHARED library (required for use in ROS 2 plugins)
add_library(socketcan_interface SHARED
  src/socket_can_interface.cpp
)

target_include_directories(socketcan_interface
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# Install the shared library and its export
install(
  TARGETS socketcan_interface
  EXPORT export_${PROJECT_NAME}  # Use consistent export name
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib  # kept for completeness (used on Windows)
  RUNTIME DESTINATION bin  # for Windows DLLs
)

install(
  DIRECTORY include/
  DESTINATION include
)

# Export for downstream packages
ament_export_targets(export_${PROJECT_NAME})  # Match export name above
ament_export_include_directories(include)
ament_export_libraries(socketcan_interface)

ament_package()