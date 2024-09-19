cmake_minimum_required(VERSION 3.0.2)
project(power_bridge)

add_compile_options(-std=c++17)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 11)

set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)

find_package(Boost REQUIRED)
find_library(BOOST_STACKTRACE_BACKTRACE_LIBRARY NAMES boost_stacktrace_backtrace)

if(DEFINED ENV{<CYPHAL_DIR>})
    set(CYPHAL_DIR $ENV{CYPHAL_DIR})
else()
    get_filename_component(CYPHAL_DIR
                           "external/libcyphal"
                           ABSOLUTE)
endif()
message("${CMAKE_CURRENT_LIST_DIR} | Using <${CYPHAL_DIR}> as directory of libcyphal")

add_subdirectory(${CYPHAL_DIR} ${PROJECT_BINARY_DIR}/build/libcyphal)

file(GLOB_RECURSE SOURCES "src/*.cpp")

find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  roscpp
  sensor_msgs
  std_msgs
  mors
)

## Generate messages in the 'msg' folder
# add_message_files(FILES
#    HMILed.msg
#    HMIBeeper.msg
#    PowerButtons.msg
# )
# add_service_files(FILES
#     PowerReset.srv
# )
 generate_messages(
   DEPENDENCIES
   std_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories(
  include
  external/libcyphal
  ${catkin_INCLUDE_DIRS}
  ${Eigen_INCLUDE_DIRS}
  ${CYPHAL_DIR}
  ${COMMON_LIBS_DIR}
  ${Boost_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME}_node ${SOURCES})
target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES} libcyphal dl)

install(TARGETS libcyphal
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)

install(TARGETS ${PROJECT_NAME}_node
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)