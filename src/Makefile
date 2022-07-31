SYS_NAME=image2music


# Opencv dev path
OPENCV_DEV_PATH := /usr/include/opencv4/

$(SYS_NAME): $(SYS_NAME).cpp
	$(CXX) -Wall -g -I../include $(SYS_NAME).cpp -o $(SYS_NAME) -I $(OPENCV_DEV_PATH) `pkg-config opencv4 --cflags --libs`

clean:
	rm -rf $(SYS_NAME) $(SYS_NAME).dSYM
